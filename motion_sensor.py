#!/usr/bin/env python3
# Marco Gabriel
# CPSC 440-01
# 2022-11-28
# marcog10@csu.fullerton.edu
# @PMarcoG10
#
# Project
#
# motion sensor written in Python3
#

"""Detects motion and outputs a sound via a piezo buzzer."""

import time
import gpiod


def main():
    """Main function"""

    # Information: about the wires
    # sensor
    # gpioget 1 94
    # line  94
    # pir_sensor = pin 18
    #
    # piezo buzzer
    # gpioget 1 98
    # line   98
    # ground pin 9
    # piezo = pin 7

    # list of currently available GPIO chips is
    # returned by the Chips function
    chip = gpiod.Chip("gpiochip1")

    # piezo buzzer
    piezo = chip.get_line(98)
    print(piezo)
    # false at the start
    piezo.request(consumer="piezo", type=gpiod.LINE_REQ_DIR_OUT)

    # sensor
    pir_sensor = chip.get_line(94)
    print(pir_sensor)
    pir_sensor.request(consumer="pir_sensor", type=gpiod.LINE_REQ_DIR_IN)

    # buzzer beeps
    # while True:
    #     piezo.set_value(1)
    #     time.sleep(1)
    #     piezo.set_value(0)
    #     time.sleep(5)

    # sensor detects
    # while True:
    #     print(pir_sensor.get_value())
    #     time.sleep(1)
    #     print(pir_sensor.get_value())
    #     time.sleep(1)

    state = 0
    try:
        # indicate that it is set to 0
        print(f'GPIO pin {pir_sensor} is {state}')
        while True:
            time.sleep(0.1)
            state = pir_sensor.get_value()
            if state == 1:
                piezo.set_value(1)
                print("Movement was detected")
                # indicate that it is set to 1
                print(f'GPIO pin {pir_sensor} is {state}')
                # 1 = on
                piezo.set_value(1)
                # indicate that it is on
                print(f'Piezo is: {piezo.get_value()}')
                time.sleep(1)
                # 0 = off
                piezo.set_value(0)
                # indicate that it is off
                print(f'Piezo is: {piezo.get_value()}')
                time.sleep(5)

    except KeyboardInterrupt:
        pass
    finally:
        # chip should be closed to release resources
        chip.close()
        print("\n")


if __name__ == "__main__":
    main()
