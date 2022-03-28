# Down Dog Kodi addon

![Down Dog](./plugin.video.downdog/resources/icon.png)

[Down Dog](downdogapp.com/) video addon.

## Installing the addon


### Dependencies

On some distribution, it may be needed to manually install the *InputStream Adaptive* addon.

InputStream Adaptive installation example On debian based OS:

```bash
$ sudo apt install kodi-inputstream-adaptive
```

### Installation from zip

Creating a zip that can be installed in Kodi:

```bash
./make.sh build_video_addon <VERSION>
```

Copy the zip in Kodi, and go to **Add-ons** -> **Add-on browser** -> **Install from zip file** and select the zip.

### Installation from the repo

TODO


### To Do after the installation

1. Enter the downdog account credentials in the add-on settings under the **API** tab
2. Start a new session:
  * start the add-on
  * choose "new session" when asked
  * configure the session settings
3. Browse the previous sessions:
  * The playback URL of the sessions done are saved and can be replayed (Only the playback URL, not the Video)
  * Set the previous sessions **Order** to **Descending** to see the last sessions first


## Addon development

Addon structure:

```
TODO: Tree
```


TODO


