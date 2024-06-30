#!/bin/bash

is_server_running() {
    screen -list | grep -q "discord"
}

start_server() {
    if ! is_server_running; then
        echo "Starting server..."
        screen -dmS discordbot bash -c 'cd /home/ubuntu/mnt && python3 bot.py'
    else
        echo "Server is already running."
    fi
}

start_server

