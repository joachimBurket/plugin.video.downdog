import os
import pickle
import requests
from requests import Response
from datetime import datetime, timezone


class DownDogApiClient:

    EXPIRE_FORMAT = "%Y%m%dT%H%M%S"
    AUTH_COOKIE_FILE = "auth_cookie"

    def __init__(self, plugin, base_url: str, creds: dict, verify: bool = True):
        self._base_url = base_url
        self._plugin = plugin
        self.logger = plugin.logger

        if not creds["username"] or not creds["password"]:
            raise Exception("DownDogApiClient creds must contain a 'username' and 'password' fields")
        self._username = creds["username"]
        self._password = creds["password"]

        self._verify = verify
        self.session = requests.Session()

        # logging in
        self._login()

    def _get_metadata(self):
        return self._get("manifest")

    def _login(self):
        """Logs to the API
        A token is stored in the session cookies
        """
        auth_cookie_path = os.path.join(self._plugin.USERDATA_PATH, self.AUTH_COOKIE_FILE)
        
        # Checking if the auth token cookie is still valid
        if os.path.exists(auth_cookie_path):
            with open(auth_cookie_path, "rb") as f:
                auth_cookie = pickle.load(f)
                now = datetime.now(timezone.utc)
                expires = datetime.fromtimestamp(auth_cookie.expires, timezone.utc)
                if now < expires:
                    # Reload cookies in session
                    self.logger.debug(f"Auth cookie still valid until {expires}")
                    self.session.cookies.set_cookie(auth_cookie)
                    return

        # getting the API metadata and the cred cookie
        self._get_metadata()

        data = {
            "email": self._username,
            "password": self._password,
        }
        res = self._post("json/login", data=data)

        for cookie in res.cookies:
            if cookie.name == "cred":
                # Saving cookie in userdata for cache
                with open(auth_cookie_path, "wb") as f:
                    pickle.dump(cookie, f)

    def generate_session(
            self,
            session_settings: str,
        ):
        """Generates a session
        :param sessin_settings: A string containing the session parameters in the form of a json dumped:
            e.g.: '{"16":0,"17":5,"15":3,"8":15,"18":1,"1":0,"3":0,"2":0,"6":8,"0":0}'
        """
        data = {
            "settings": session_settings,
        }
        return self._post("json/generate", data=data).json()

    def playback_url(self, sequence_id: str, playlist_id: str, video_settings: dict):
        """Retrieves the media playback URL
        :param sequence_id: The ID of the session
        :param playlist_id: The ID of the musics
        :param video_settings: a dict containing the video settings: audioBalance, includeClosedCaptions, videoQualityId
        """
        data = {
            "sequenceId": sequence_id,
            "playlistId": playlist_id,
            "includeCountdown": True,
            "includeOverlay": False,
            "includePoseNames": True,
            "includeSanskritNames": False,
            "mirrorVideo": False,
            "cellularConnection": "false",
	        "chromecast": "false",
	        "airplay": "false",
            "videoOffsetTime": 0,
        }
        data = {**data, **video_settings}
        return self._post("json/playbackUrl", data=data).json()


    # =============================== Generic http methods ==============================

    def _get(self, path: str, **kwargs) -> Response:
        return self._generic_http_method_request("get", path, **kwargs)
    
    def _post(self, path: str, **kwargs) -> Response:
        return self._generic_http_method_request("post", path, **kwargs)


    def _generic_http_method_request(self, method: str, path: str, **kwargs) -> Response:
        http_method = getattr(self.session, method)
        return http_method(
            os.path.join(self._base_url, path),
            **kwargs,
            verify=self._verify,
        )
