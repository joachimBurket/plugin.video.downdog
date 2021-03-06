#!/bin/sh
pulseaudio > /dev/null 2>&1 &

vncserver $DISPLAY -noxstartup \
                   -securitytypes=none \
                   -geometry=1600x900 \
                   -depth=24 \
                   -alwaysshared \
                   -localhost=0 \
                   --I-KNOW-THIS-IS-INSECURE

kodi --standalone --debug  > /dev/null 2>&1 &

while [ ! -f ".kodi/temp/kodi.log" ]; do
    sleep 0.1
done

tail -f .kodi/temp/kodi.log