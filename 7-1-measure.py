import RPi.GPIO as GPIO
import time
import matplotlib as plt
import numpy as np

def dec_to_bin(number):
    return [int(element) for element in  bin(number)[2:].zfill(8)]

def adc():
    for value in range (0, 256):
        bin_num = dec_to_bin(value)
        GPIO.output (dac, bin_num)
        time.sleep(0.001)
        comparator_value = GPIO.input(comp)
        if comparator_value == 1 :
            break
    print ('return value = ', value, "\n")
    return int(value)

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup (dac, GPIO.OUT)


comp = 14
troyka = 13

GPIO.setup (troyka, GPIO.OUT)
GPIO.setup (comp, GPIO.IN)
GPIO.output (troyka, 1)

number_of_values = 255
max_voltage = 3.3

value = 0

data_value = []
data_set = []
start_time = time.time()

try:

    while (True):

        value = adc()
        data_value.append(value)

        if value <= 20:
            GPIO.output (troyka, 1)
        elif value >= 213:
            GPIO.output (troyka, 0)


except ArithmeticError:
    print ("program cancle\n")

finally :
    stop_time = time.time()
    data_value_str = [str(i) for i in data_value]
    
    for i in range (0, len(data_value)):
        data_set.append (str(data_value[i] * max_voltage / number_of_values) + " " + str (i * (stop_time - start_time) / len(data_value)))

    with open ("data.txt", "w") as output:
        output.write("\n".join(data_value_str))

    with open ("settings.txt", "w") as output_set:
        output_set.write("\n".join(data_set))
    
    print ("\n")
    GPIO.output(dac, 0)
    GPIO.cleanup()