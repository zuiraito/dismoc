is_server_running() {
    screen -list | grep -q "minecraft"
}

start_server() {
    if ! is_server_running; then
        ~/mnt/start.sh
        echo "Minecraft server started."
    fi
}

start_server
sleep 10800 
screen -S minecraft -X stuff 'say server shutdown in 60 s.\n'
sleep 55
screen -S minecraft -X stuff 'say server shutdown in 5 s.\n'
sleep 1
screen -S minecraft -X stuff 'say server shutdown in 4 s.\n'
sleep 1
screen -S minecraft -X stuff 'say server shutdown in 3 s.\n'
sleep 1
screen -S minecraft -X stuff 'say server shutdown in 2 s.\n'
sleep 1
screen -S minecraft -X stuff 'say server shutdown in 1 s.\n'
sleep 1
~/mnt/stop.sh

