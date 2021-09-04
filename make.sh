#!/bin/bash

PLUGIN_NAME=plugin.video.downdog

function check_version() {
    if [[ "$#" -eq 1 ]]; then
        VERSION="$1"
    elif [[ -d .git ]]; then
        VERSION=$(git tag --sort=committerdate -l | tail -n1)
    elif [[ "$#" -eq 0 ]]; then
        echo "Current directory is not a git repository."
        echo "Provide a version as an argument."
        exit 1
    fi
    DIR="$PLUGIN_NAME"-"$VERSION"
}

function build_video_addon() {
    check_version $1
    echo "Creating video.kino.pub add-on archive"
    echo "======================================"
    mkdir "$DIR"
    VERSION="$VERSION" envsubst < "$PLUGIN_NAME"/addon.xml > "$DIR"/addon.xml
    rsync -rv --exclude=*.pyc "$PLUGIN_NAME"/resources "$PLUGIN_NAME"/addon.py "$PLUGIN_NAME"/LICENSE "$DIR"
    zip -rv -9 -m "$DIR".zip "$DIR"
    echo
}

"$@"