#!/usr/bin/bash

#startx /usr/bin/openbox-session
#nestopia ../roms/Super\ Mario\ Brothers\ \(Japan\).fds
modprobe uinput
for ((;;)) do
	buttonPressed=$(python3 getGPIO.py 2>&1);
	if [ "32" = 32 ]; then # make this a new thread
		python3 emitZClick.py
	else
		echo expression evaluated as false
	fi
done
