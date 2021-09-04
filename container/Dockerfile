# from https://blog.misharov.pro/2021-02-14/conkodi

# Team Kodi officially supports ppa for Ubuntu
FROM ubuntu:20.04

# Packages installation should be unattended
ARG DEBIAN_FRONTEND=noninteractive
# YOu can specify a version of Kodi to install as build arg
ARG KODI_VERSION=18.9

# This needed for running VNC
ENV DISPLAY=:99 \
    HOME=/home/kodi

# Adding ppa and install dependencies
RUN apt update && \
    apt install -y --no-install-recommends software-properties-common && \
    add-apt-repository -y ppa:team-xbmc/ppa && \
    apt -y purge openssl software-properties-common && \
    apt install -y --no-install-recommends dumb-init \
                                           # Without pulseaudio Kodi logs are unreadble and useless
                                           pulseaudio \
                                           # This needs for establishing SSL connections 
                                           ca-certificates \
                                           # Tigervnc implements an X server and provides VNC access
                                           tigervnc-standalone-server \
                                           tigervnc-xorg-extension \
                                           kodi && \
                                           #kodi=2:${KODI_VERSION}+* && \
    apt -y --purge autoremove

COPY start.sh /
COPY guisettings.xml /home/kodi/.kodi/userdata/guisettings.xml

# Various permission tweaks
RUN chmod +x /start.sh && \
    touch /home/kodi/.Xauthority && \
    chgrp -R 0 /home/kodi/ && \
    chmod -R g=u /home/kodi/

WORKDIR /home/kodi

# VNC port
EXPOSE 5999
# HTTP port
EXPOSE 8080
# EventServer port
EXPOSE 9777/udp

# It always a good practice to run applications in the container under some user
USER 1001
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/start.sh"]
