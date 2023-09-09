from mpu6050 import mpu6050
import time
import math

sensor = mpu6050(0x68) # I2C ad

while True:

    accel_data = sensor.get_accel_data()

    # Calc pitch and roll angles
    pitch = math.atan2(accel_data['y'], math.sqrt(accel_data['x'] ** 2 + accel_data['z'] ** 2)) * 180 / math.pi
    roll = math.atan2(accel_data['x'], math.sqrt(accel_data['y'] ** 2 + accel_data['z'] ** 2)) * 180 / math.pi

    print("Pitch: {:.2f}   Roll: {:.2f}".format(pitch, roll))

    time.sleep(0.1)
