
opkg update
opkg install mosquitto mosquitto-client libmosquitto
npm install mqtt@1.7.0 --save
npm install ntp-client –save
pip install pyserial paho-mqtt
opkg install coreutils-nohup
opkg install nano
nano /etc/rc.local 
#!/bin/sh -e
nohup python /root/things.py LASS_DEVICE_ID > /dev/null 2>&1 &
