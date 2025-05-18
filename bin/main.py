import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging

from waveshare_pwm_fan_hat import PwmFanHat

logging.basicConfig(level=logging.INFO)
font = ImageFont.load_default()
pfh = PwmFanHat.PwmFanHat()

options_file = open("/data/options.json", "r")
config = json.load(options_file)
fan_min_temp = config["fan_min_temp"]
fan_max_temp = config["fan_max_temp"]
delta_temp = config["delta_temp"]
update_interval = config["update_interval"]
rotate_oled = config["rotate_oled"]
options_file.close()

try:
    while True:
        pfh.update(
            fan_min_temp=fan_min_temp,
            fan_max_temp=fan_max_temp,
            delta_temp=delta_temp,
            update_interval=update_interval,
            rotate_oled=rotate_oled,
        )

except KeyboardInterrupt:
    pfh.fan_off()
    logging.info("Fan off")
