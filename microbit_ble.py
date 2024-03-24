import time
from blevent import BleEventManager

def dnarg_command():
    print(f"dnarg")

def darg_command(arg: int):
    print(f"darg with arg: {arg}")

with BleEventManager("vapev") as microbit:
    microbit.bind_function("dnarg", dnarg_command)
    microbit.bind_function("darg", darg_command)
    microbit.send_command("narg")
    time.sleep(3)
    microbit.send_command("arg",3)
    time.sleep(20)
