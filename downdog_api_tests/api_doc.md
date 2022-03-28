# Downdog app

### Login

POST https://www.downdogapp.com/json/login

* Request:
  
  ```
  email=joachim-b@hotmail.fr
  password=pouet
  deviceDescription=Firefox 90.0
  osVersion=Linux
  timeZone=Europe/Zurich
  locale=en-US
  timestamp=1630771753319
  languageOption
  cred=A0SKCRZLL9Q-AAJAF97C34I-cfkcjk9j3j0275sptg28lhu3t2
  ```

* Response:
  
  ```
  {"cred":"A1M2JRLK6DI-AAJAF97C34I-cfkcjk9j3j0275sptg28lhu3t2","type":"SUCCESS"}
  ```

Cookie:

```json
{
    "cred": "A1M2JRLK6DI-AAJAF97C34I-cfkcjk9j3j0275sptg28lhu3t2",
    "G_ENABLED_IDPS": "google"
}
```

### Endpoints

* POST https://www.downdogapp.com/manifest: Pleins de métadata
  
  * Request: 
    
    ```
    deviceDescription=Firefox 90.0
    osVersion=Linux
    timeZone=Europe/Zurich
    locale=en-US
    timestamp=1630768851924
    languageOption
    cred=A1M2JRLK6DI-ALSCIIJKJ04-cgtv84d8ijdmdnr4p57ulhsk2t
    ```
  
  * Response:
    
    ```
    
    ```

* POST https://www.downdogapp.com/json/lengthOptions: Durées de session disponibles
  
  * Request:
    
    ```
    settings={"16":0,"17":5,"15":3,"8":15,"18":1,"1":0,"3":0,"2":0,"6":8,"0":0}
    deviceDescription=Firefox 90.0
    osVersion=Linux
    timeZone=Europe/Zurich
    locale=en-US
    timestamp=1630768852676
    languageOption
    cred=A1M2JRLK6DI-ALSCIIJKJ04-cgtv84d8ijdmdnr4p57ulhsk2t
    ```
  
  * Response:
    
    ```
    lengthOptionIds: [5, 6, 7, 8, ...]
    ```

* POST https://www.downdogapp.com/json/history: Historiques des sessions
  
  * Request:
    
    ```
    deviceDescription=Firefox 90.0
    osVersion=Linux
    timeZone=Europe/Zurich
    locale=en-US
    timestamp=1630768852698
    languageOption
    cred=A1M2JRLK6DI-ALSCIIJKJ04-cgtv84d8ijdmdnr4p57ulhsk2t
    ```
  
  * Response:
    
    ```json
    {
      "items": [
        {
          "sequenceId":"AHFJLA1PBWZ",
          "poseListItems":[
            {
              "name":"Child's Pose",
              "sanskritName":"Balasana",
              "imageUrlSuffix":"GTycorIz_1_1_7/180.jpg"
            },
            {
              "name":"Baby Camel Hips on Heels",
              "imageUrlSuffix":"vdYhq8rF_607_0_7/180.jpg"
            },
            ...
          ],
          "displayStart": true,
          "displaySave": true,
          "songs": [
            {
              "id": "AWVDMR9H9CU",
              "title": "Hypnotica - Alpha (relaxed/reflecting)",
              "artist": "Christopher Lloyd Clarke",
              "artwork": "royalty_free.jpg",
              "previewUrl": "https://media.downdogapp.com/song_samples/3756.mp4"
            }
          ],
          "selectors": [
            {
              "type": "CATEGORY",
              "label": "Full Practice"
            },
            {
              "type": "LEVEL",
              "label": "Intermediate 1"
            },
            {
              "type": "LENGTH",
              "label": "18 Minutes"
            }
          ],
          "primaryText": "18 Minutes - Sun Aug 08",
          "date": "Sun Aug 08",
          "timestamp": {
            "seconds": 1.628439356072E9
           },
           "practiceId": "AT13V2ZOCDM",
           "appType": "ORIGINAL",
           "totalTime": {
             "seconds": 1259.9999999999998
           },
           "proportionCompleted": 1.0
        },
        { ... }
      ]
    }
    ```

* POST https://www.downdogapp.com/json/generate: Générer une session
  
  * Request:
    
    ```
    settings={"16":0,"17":5,"15":3,"8":15,"18":1,"1":0,"3":0,"2":0,"6":8,"0":0}
    deviceDescription=Firefox 90.0
    osVersion=Linux
    timeZone=Europe/Zurich
    locale=en-US
    timestamp=1630768934476
    languageOption
    cred=A1M2JRLK6DI-ALSCIIJKJ04-cgtv84d8ijdmdnr4p57ulhsk2t
    ```
  
  * Response:
    
    ```json
    {
      "sequence": {
        "sequenceId": "AIKYLS9RYDJ",
        "poseListItems": [
          {
            "imageUrlSuffix": "JzKl1c3g_597_0_7/180.jpg"
          },
          {
            "name": "Supine Bent Knees",
            "imageUrlSuffix": "WlkJgpSW_93_0_7/180.jpg"
          },
          {
            "name": "Easy Seat",
            "sanskritName": "Sukhasana",
            "imageUrlSuffix": "eGOXdB71_0_0_7/180.jpg"
          }
          // { ... }
        ],
        "poseListItemTimes": [
          {
            "seconds": 12.50163219468852
          },
          {
            "seconds": 50.312107315628396
          },
          {
            "seconds": 55.40373951031691
          }
          // { ... }
        ],
        "snapTimes": [
          {
            "seconds": 0.0
          },
          {
            "seconds": 50.312107315628396
          },
          {
            "seconds": 55.40373951031691
          },
          {
            "seconds": 65.23305755750815
          }
          // { ... }
        ],
        "postPracticeMessage": "Thank you for practicing with Down Dog!",
        "trackerLabel": "Full Practice (Beginner 1)",
        "readyOverlayStrings": [],
        "totalTime": {
          "seconds": 1080.0000000000005
        },
        "supportsPoseNames": true,
        "supportsSanskritNames": true,
        "supportsClosedCaptions": true,
        "supportsCountdown": true,
        "supportsOverlay": false,
        "supportsMirror": true,
        "supportsPoseTimeline": true
      },
      "playlist": {
        "playlistId": "ADY99K45TXQ",
        "songs": [
          {
            "id": "AX2OSRGZR3I",
            "title": "Lately (Interlude)",
            "artist": "City Fidelia",
            "artwork": "3636.jpg",
            "itunesUrl": "https://geo.itunes.apple.com/us/album/id1124202812?i=1124202982&mt=1&app=music",
            "spotifyUrl": "https://open.spotify.com/track/3mZg4qv8X55kolcHiQw2hy",
            "amazonUrl": "https://www.amazon.com/dp/B01H4GEKJO",
            "previewUrl": "https://media.downdogapp.com/song_samples/3636.mp4"
          }
          // { ... }
        ],
        "startTimes": [
          {
            "seconds": 0.0
          },
          {
            "seconds": 51.005
          },
          {
            "seconds": 162.95644263994475
          }
          // { ... }
        ],
        "playlistTypeId": 0
      }
    }
    ```

* POST https://www.downdogapp.com/json/playbackUrl: Récupérer l'URL de la vidéo
  
  * Request:
    
    ```
    sequenceId=AIKYLS9RYDJ
    playlistId=ADY99K45TXQ
    videoOffsetTime=0
    audioBalance=0.65
    includeCountdown=true
    includeOverlay=false
    includePoseNames=true
    includeSanskritNames=false
    includeClosedCaptions=false
    mirrorVideo=false
    videoQualityId=5
    cellularConnection=false
    deviceDescription=Firefox 90.0
    osVersion=Linux
    timeZone=Europe/Zurich
    locale=en-US
    timestamp=1630768935740
    languageOption
    cred=A1M2JRLK6DI-ALSCIIJKJ04-cgtv84d8ijdmdnr4p57ulhsk2t
    ```
  
  * Response:
    
    ```json
    {     
      "url":"https://stitched.downdogapp.com/master_xvTiycRL_AIKYLS9RYDJ.m3u8",
        "videoOffsetTime":{
       "seconds":0.0
     }
    }
    ```

* GET https://stitched.downdogapp.com/master_xvTiycRL_AIKYLS9RYDJ.m3u8: Get video and audio base URLs
  
  * Response (vnd.apple.mpegurl):
    
    ```
    #EXTM3U
    #EXT-X-VERSION:6
    #EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="group_audio",NAME="audio_1",DEFAULT=YES,LANGUAGE="en",URI="1_xvTiycRL_AIKYLS9RYDJ.m3u8"
    #EXT-X-STREAM-INF:BANDWIDTH=792000,RESOLUTION=1280x720,CODECS="avc1.4d401f,mp4a.40.2",AUDIO="group_audio"
    0_xvTiycRL_AIKYLS9RYDJ.m3u8 => GET on this to get video URLs list
    ```

* GET https://stitched.downdogapp.com/0_xvTiycRL_AIKYLS9RYDJ.m3u8: Get video stream URLs:
  * Response:
    
    ```
    #EXTM3U
    #EXT-X-VERSION:6
    #EXT-X-TARGETDURATION:6
    #EXT-X-MEDIA-SEQUENCE:0
    #EXT-X-PLAYLIST-TYPE:EVENT
    #EXT-X-START:TIME-OFFSET=0
    #EXT-X-INDEPENDENT-SEGMENTS
    #EXTINF:6.000000,
    https://stitched.downdogapp.com/0000_0_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:6.000000,
    https://stitched.downdogapp.com/0001_0_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:6.000000,
    https://stitched.downdogapp.com/0002_0_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:6.000000,
    https://stitched.downdogapp.com/0003_0_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:6.000000,
    https://stitched.downdogapp.com/0004_0_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:6.000000,
    https://stitched.downdogapp.com/0005_0_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:6.000000,
    https://stitched.downdogapp.com/0006_0_xvTiycRL_AIKYLS9RYDJ.ts
    [....]
    https://stitched.downdogapp.com/blackfGHTOZsD_0_382.ts
    #EXTINF:6.000000,
    https://stitched.downdogapp.com/blackfGHTOZsD_0_383.ts
    #EXTINF:6.000000,
    https://stitched.downdogapp.com/blackfGHTOZsD_0_384.ts
    #EXTINF:6.000000,
    https://stitched.downdogapp.com/blackfGHTOZsD_0_385.ts
    #EXT-X-ENDLIST
    ```
    
    
    
* GET https://stitched.downdogapp.com/1_xvTiycRL_AIKYLS9RYDJ.m3u8: Get audio stream URLs
  * Response:
  * ```
    #EXTM3U
    #EXT-X-VERSION:6
    #EXT-X-TARGETDURATION:6
    #EXT-X-MEDIA-SEQUENCE:0
    #EXT-X-PLAYLIST-TYPE:EVENT
    #EXT-X-START:TIME-OFFSET=0
    #EXTINF:6.013967,
    https://stitched.downdogapp.com/0000_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:5.990756,
    https://stitched.downdogapp.com/0001_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:6.013967,
    https://stitched.downdogapp.com/0002_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:5.990744,
    https://stitched.downdogapp.com/0003_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:5.990756,
    https://stitched.downdogapp.com/0004_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:6.013967,
    https://stitched.downdogapp.com/0005_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:5.990744,
    https://stitched.downdogapp.com/0006_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:6.013967,
    https://stitched.downdogapp.com/0007_1_xvTiycRL_AIKYLS9RYDJ.ts
    [...]
    #EXTINF:6.013967,
    https://stitched.downdogapp.com/0378_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:5.990744,
    https://stitched.downdogapp.com/0379_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:5.990744,
    https://stitched.downdogapp.com/0380_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:6.013978,
    https://stitched.downdogapp.com/0381_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:5.990744,
    https://stitched.downdogapp.com/0382_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:5.990744,
    https://stitched.downdogapp.com/0383_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:6.013967,
    https://stitched.downdogapp.com/0384_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXTINF:5.990756,
    https://stitched.downdogapp.com/0385_1_xvTiycRL_AIKYLS9RYDJ.ts
    #EXT-X-ENDLIST
    ```
    
    
    
* 