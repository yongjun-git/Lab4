import time
from hal import hal_led as led
from hal import hal_input_switch as switch

LEFT = 1   # ← the number your switch showed in the LEFT position

def main():
    led.init()
    switch.init()

    right_start = None   # stopwatch not started

    while True:
        if switch.read_slide_switch() == LEFT:
            right_start = None          # reset the stopwatch
            # 5 Hz
            led.set_output(24, 1)
            time.sleep(0.1)
            led.set_output(24, 0)
            time.sleep(0.1)
        else:
            if right_start is None:     # just moved right?
                right_start = time.time()   # start the stopwatch

            if time.time() - right_start < 5:
                # under 5 s: 10 Hz
                led.set_output(24, 1)
                time.sleep(0.05)
                led.set_output(24, 0)
                time.sleep(0.05)
            else:
                # 5 s or more: off
                led.set_output(24, 0)

if __name__ == "__main__":
    main()