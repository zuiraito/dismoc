screen -S minecraft -X stuff '\n'
screen -S minecraft -X stuff 'say Server wird in 10s heruntergefahren\n'
sleep 10
screen -S minecraft -X stuff 'stop\n'
