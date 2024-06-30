#!/bin/bash
# Minecraft server port
MINECRAFT_PORT=1910

# Function to check if the server is running
is_server_running() {
    screen -list | grep -q "minecraft"
}

# Function to start the server
start_server() {
    if ! is_server_running; then
        ~/mnt/start.sh
        echo "Minecraft server started."
    fi
}

# Monitor the network for incoming connection attempts to the Minecraft server port
while true; do
    sudo tcpdump -i any tcp dst port $MINECRAFT_PORT -c 1 2>/dev/null && start_server
    # Wait a few seconds before checking again
    sleep 10
done
