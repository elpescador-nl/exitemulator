from time import sleep
import signal
import os
import re
import RPi.GPIO as GPIO

gpio_pin_number=25

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def exitEmulator(channel):
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

    re_path = re.compile('\/opt\/retropie\/(emulators|ports)\/')

    for pid in pids:
        try:
            commandpath = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
            if re_path.match(commandpath):
                os.kill(int(pid), signal.SIGTERM)
                print('SIGTERM sent to process %s' % pid)
        except IOError:
            continue
GPIO.add_event_detect(gpio_pin_number, GPIO.RISING, callback=exitEmulator, bouncetime=500)

while True:
    sleep(10)
