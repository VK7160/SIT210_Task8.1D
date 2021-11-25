import smbus
import time

device_address =  0x23
power_off  = 0x00
power_on   = 0x01
reset      = 0x07

one_time_high_res_mode = 0x20

bus = smbus.SMBus(1)

def read_light_value():
    value = bus.read_i2c_block_data(device_address, one_time_high_res_mode)
    return Convert(value)

def Convert(data):
    return ((data[1] + (256*data[0]))/1.2)

while True:
     print(" Light Intensity: "+ str(read_light_value())+ " Lux")
     time.sleep(1)