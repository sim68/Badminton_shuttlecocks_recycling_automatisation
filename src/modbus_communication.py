# modbus_communication.py

from images_processing import capture_image
import time
import threading
from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusSequentialDataBlock, ModbusServerContext
from gpiozero import PWMOutputDevice

# Configure the servo motor
pwm_pin = 18
pwm = PWMOutputDevice(pwm_pin, frequency=50)
duty_cycle = 0.45

def print_register(context, interval):
    percentage_results = []

    while True:
        # Read Modbus holding registers
        registers = context[0].getValues(3, 0, count=10)
        print(f"Current Registers: {registers}")

        # Check command to take a photo
        start_photo = context[0].getValues(3, 0, count=1)[0]
        print(f"Start Photo Command: {start_photo}")

        if start_photo == 1:
            white_pixels_percentage = capture_image()
            context[0].setValues(3, 0, [0])

            if white_pixels_percentage != 0:
                percentage_results.append(white_pixels_percentage)
                context[0].setValues(3, 1, [1])
                time.sleep(0.5)
                context[0].setValues(3, 1, [0])

                if len(percentage_results) == 4:
                    decision_threshold = 1  # Percentage threshold to consider a shuttlecock as worn
                    if any(p > decision_threshold for p in percentage_results):
                        context[0].setValues(3, 2, [1])  # Shuttlecock is worn
                        print("Shuttlecock is worn")
                    else:
                        context[0].setValues(3, 2, [2])  # Shuttlecock is new
                        print("Shuttlecock is new")
                    percentage_results = []

        # Servo motor control
        start_pwm = context[0].getValues(3, 3, count=1)[0]
        pwm_sensor = context[0].getValues(3, 4, count=1)[0]

        try:
            if start_pwm == 1 and pwm_sensor != 1:
                pwm.value = duty_cycle
                if pwm_sensor == 1:
                    pwm.value = 0
                    print("Servo motor position 1 reached")

            # Additional conditions for start_pwm...

            # Reset
            reset = context[0].getValues(3, 5, count=1)[0]
            if reset == 1:
                context[0].setValues(3, 0, [0]*10)
                print("Registers have been reset")

        except KeyboardInterrupt:
            pwm.value = 0

        time.sleep(interval)

def run_server():
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [0]*10),
        co=ModbusSequentialDataBlock(0, [0]*10),
        hr=ModbusSequentialDataBlock(0, [0]*10),
        ir=ModbusSequentialDataBlock(0, [0]*10)
    )

    context = ModbusServerContext(slaves=store, single=True)

    thread = threading.Thread(target=print_register, args=(context, 2))
    thread.daemon = True
    thread.start()

    StartTcpServer(context, address=("192.168.0.28", 5030))

if __name__ == "__main__":
    run_server()
