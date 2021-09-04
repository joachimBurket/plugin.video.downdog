
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

### Installing the kodi extension

