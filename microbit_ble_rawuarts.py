import time

from kaspersmicrobit import KaspersMicrobit

def print_received_string(string: str):
    print(f"Received from microbit: '{string}'")

with KaspersMicrobit.find_one_microbit() as microbit:
    # listen for strings sent by the micro:bit
    microbit.uart.receive_string(print_received_string)

    # send a string to the micro:bit
    microbit.uart.send_string("c:arg:3\n")
    time.sleep(10)
    print("now narg")
    microbit.uart.send_string("c:narg\n")

    time.sleep(20)
'''