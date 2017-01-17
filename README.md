# exitemulator
Python script to exit RetroPie emulator using GPIO button press

## Source
Script based on example made by reddit user *b4ux1t3*: https://www.reddit.com/r/raspberry_pi/comments/2yw4fn/finally_set_up_retropie_complete_with_a_gpio/

## Usage
Connect a pull up button to the designated pin, in the example BCM pin 25.

## Start at boot
To start this script at boot edit `/etc/rc.local`. 
At the end above `exit 0` add the following line:
```
python /home/pi/RetroPie/scripts/exitemulator.py
```
