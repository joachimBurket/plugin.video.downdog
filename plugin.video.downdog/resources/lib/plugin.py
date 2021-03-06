import json
import sys
from urllib.parse import urlencode, parse_qsl

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcvfs
import inputstreamhelper

from resources.lib.logger import Logger
from resources.lib.settings import Settings
from resources.lib.client import DownDogApiClient

class DownDogSessionParameters:

    IDS_MAP = {
        "session_type": {
            "Full Practice": 0,
            "Cardio Flow": 36,
            "Flexibility Flow": 101,
            "Slow Flow": 3,
            "Gentle": 8,
            "Restorative": 1,
            "Quick Flow": 2,
            "No Warmup": 5,
            "Yin": 9,
            "Chair Yoga": 7,
            "Ashtanga": 11,
            "Sun Salutations": 6,
            "Yoga Nidra": 20,
            "Hot 26": 27,
        },
        "session_level": {
            "Beginner 1": 0,
            "Beginner 2": 1,
            "Intermediate 1": 2,
            "Intermediate 2": 4,
            "Advanced": 3,
        },
        "pace": {
            "Slowest": 2,
            "Slow": 0,
            "Normal": 4,
            "Fast": 1,
            "Fastest": 3,
        },
        "playlist_type": {
            "None": -1,
            "Alt Beats": 1,
            "Acoustic": 2,
            "Piano and Strings": 3,
            "Ambient": 4,
            "Spiritual": 5,
            "Nature Sounds": 6,
            "Brain Waves": 7,
        },
        "voice_actor": {
            "Mars": 3,
            "Isaiah": 4,
            "Xinia": 5,
            "Chad": 7,
            "Alana": 109,
            "Fiona": 111,
            "Selama": 113,
            "Alberto": 122,
        },
        "instruction_verbosity": {
            "Full Explanation": 0,
            "Default": 1,
            "Default plus Silence": 2,
            "Least Explanation plus Breaths": 3,
            "Least Explanation plus Silence": 4,
        },
        "video_quality": {
            "Auto": 5,
            "HD": 4,
            "High": 3,
            "Low": 2,
            "Standard": 1,
        },
    }

    def __init__(self, plugin):
        self._plugin = plugin

    def parse_addon_settings(self):
        """Parsing parameters from the addon settings"""
        settings = self._plugin.settings
        self.session_type = settings.session_type
        self.session_length = settings.session_length
        self.savasana_length = settings.savasana_length
        self.session_level = settings.session_level
        self.pace = settings.pace
        self.playlist_type = settings.playlist_type
        self.voice_actor = settings.voice_actor
        self.instruction_verbosity = settings.instruction_verbosity
        self.video_quality = settings.video_quality
        self.audio_balance = settings.audio_balance
        self.enable_captions = True if settings.enable_captions == "true" else False

    def get_session_settings(self) -> str:
        """Returns the formatted session settings to be passed to the API"""
        session_settings = {
            "0": self.IDS_MAP["session_type"][self.session_type],
            "1": 0,     # focus_area default None
            "2": self.IDS_MAP["session_level"][self.session_level],
            "3": self.IDS_MAP["pace"][self.pace],
            "6": self.IDS_MAP["voice_actor"][self.voice_actor],
            "8": int(self.session_length),
            "15": int(self.savasana_length),
            "16": self.IDS_MAP["playlist_type"][self.playlist_type],
            "18": self.IDS_MAP["instruction_verbosity"][self.instruction_verbosity],
        }
        return json.dumps(session_settings)

    def get_video_settings(self) -> dict:
        """Returns a dictionary containing the video settings to be passed to the API"""
        return {
            "audioBalance": self.audio_balance,
            "videoQualityId": self.IDS_MAP["video_quality"][self.video_quality],
            "includeClosedCaptions": self.enable_captions,
        }


class Plugin(object):
    ADDON = xbmcaddon.Addon()
    KODI_VERSION_MAJOR = int(xbmc.getInfoLabel("System.BuildVersion").split('.')[0])
    PLUGIN_ID = ADDON.getAddonInfo("id")
    PLUGIN_URL = f"plugin://{PLUGIN_ID}"
    DOWNDOG_BASE_URL = "https://www.downdogapp.com"
    HANDLE = int(sys.argv[1])
    settings = Settings()
    try:
        USERDATA_PATH = xbmcvfs.translatePath(ADDON.getAddonInfo('profile')).decode('utf-8')
    except AttributeError:
        USERDATA_PATH = xbmcvfs.translatePath(ADDON.getAddonInfo('profile'))
    

    def __init__(self):
        # strings translation
        self.tr = self.ADDON.getLocalizedString

        self.logger = Logger(self)
        self._create_dir_if_doesnt_exists(self.USERDATA_PATH)
        self.session_params = DownDogSessionParameters(self)

        # Check that DownDog account credentials are passed
        while self.settings.username == "" or self.settings.password == "":
            xbmcgui.Dialog().ok(self.tr(31001), self.tr(31002))
            self.ADDON.openSettings()

        self.api_client = DownDogApiClient(
            self,
            self.DOWNDOG_BASE_URL,
            {"username": self.settings.username, "password": self.settings.password}
        )

    def _create_dir_if_doesnt_exists(self, dir_path: str):
        """Creates a folder if it doesnt exists"""
        if dir_path[-1] != '/':
            dir_path += '/'

        if not xbmcvfs.exists(dir_path):
            self.logger.info(f"Creating folder {dir_path}")
            xbmcvfs.mkdirs(dir_path)

    def _url(self, **kwargs):
        """Constructs the plugin's URL"""
        return f"{self.PLUGIN_URL}?{urlencode(kwargs)}"

    def _session_config_dialog(self):
        self.logger.debug("Opening session config dialog")
        self.ADDON.openSettings()
        self.session_params.parse_addon_settings()
        self.logger.debug(f"Session settings: {self.session_params.get_session_settings()}")
        self.logger.debug(f"Video settings: {self.session_params.get_video_settings()}")

    def new_session(self):
        """Creating a new session"""
        self.logger.info("Creating a new session")
        
        # Open dialog to get the session configuration
        self._session_config_dialog()

        # TODO: Catch client exceptions
        res = self.api_client.generate_session(self.session_params.get_session_settings())
        sequence_id = res["sequence"]["sequenceId"]
        playlist_id = res["playlist"]["playlistId"]
        
        res = self.api_client.playback_url(sequence_id, playlist_id, self.session_params.get_video_settings())
        url = res["url"]
        self.logger.debug(f"Playback URL: {url}")
        
        session_name = f"{self.session_params.session_type} session"
        session_li = xbmcgui.ListItem(label=session_name)
        session_li.setInfo("video", {"title": session_name,
                                    "mediatype": "video"}
        )
        session_li.setProperty("IsPlayable", "true")
        xbmcplugin.addDirectoryItem(self.HANDLE, self._url(action="play", video=url), session_li, isFolder=False)
        xbmcplugin.endOfDirectory(self.HANDLE)
        # self.start_session(url)   # TODO: Find a way to start session directly (without showing directory first)

    def start_session(self, video: str):
        """Start playing a session"""
        self.logger.info(f"Starting session {video}")

        is_helper = inputstreamhelper.Helper("hls")
        if is_helper.check_inputstream():
            play_item = xbmcgui.ListItem(path=video, offscreen=True)
            play_item.setContentLookup(False)
            play_item.setMimeType("application/vnd.apple.mpegurl")
            play_item.setProperty("inputstream", is_helper.inputstream_addon)
            play_item.setProperty("inputstream.adaptive.manifest_type", "hls")
            play_item.setProperty("isPlayable", "true")
            xbmcplugin.setResolvedUrl(self.HANDLE, True, play_item)

    def router(self, paramstring):
        params = dict(parse_qsl(paramstring))
        if params:
            if params["action"] == "play":
                self.start_session(params["video"])
            else:
                raise ValueError(f"Invalid paramstring {paramstring}!")
        else:
            # Called without params
            self.new_session()

    def run(self):
        self.logger.debug("Starting plugin DownDog!")
        self.logger.debug(f"Argv: {sys.argv}, type argv[2]: {type(sys.argv[2])}")

        self.router(sys.argv[2][1:])

        self.logger.info("End of plugin DownDog!")
