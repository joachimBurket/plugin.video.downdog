
### Build a container image:

```bash
podman build -t kodi -f Dockerfile .
```

### Run it:

```bash
podman run --rm -p 5999:5999 -p 8080:8080 localhost/kodi
```

### Use any VNC viewer to get access to X session, e.g.:

```bash
vncviewer 127.0.0.1:5999
```

### Running the Kodi extension on the container

Start the container and mount the in development extension folder in the `~/.kodi/addons/` folder:

```bash
# Go to the extension directory (e.g. plugin.video.hello/, or script.hello/)
cd <EXTENSION_DIR>

# Run the container and mount the extension in the addons folder
pd run --rm --name kodi -p 5999:5999 -p 8080:8080 -v $(pwd):/home/kodi/.kodi/addons/$(basename $(pwd)):z localhost/kodi
```

We can then work on the addon from the host and test it in live with VNCViewer:

```bash
vncviewer 127.0.0.1:5999 &
```

