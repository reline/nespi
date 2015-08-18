#!/usr/bin/bash

modprobe uinput

############# run entire loop in new thread ############
for ((;;)) do
	buttonPressed=$(python3 getGPIO.py 2>&1);
	if [ "32" = 32 ]; then # make this a new thread
		parallel python3 emitZClick.py
	else
		echo expression evaluated as false
	fi
done
########################################################

startx /usr/bin/openbox-session | nestopia ../roms/Super\ Mario\ Brothers\ \(Japan\).fds
