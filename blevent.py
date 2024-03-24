#MIT Licence
from kaspersmicrobit import KaspersMicrobit

class BleEventManager:
    def __init__(self, devname):
        self.devname = devname
        self.command_callbacks = {}
        self.microbitdev = KaspersMicrobit.find_one_microbit(microbit_name=devname)
        self.is_listening = False

    def __enter__(self):
        self.connect()
        return self
 
    def __exit__(self, *args):
        self.disconnect()

    def connect(self):
        """Establishes a connection with the micro:bit."""
        self.microbitdev.connect()

    def disconnect(self):
        self.microbitdev.disconnect()
    
    def send_command(self, command_name, argument=None):
        """Sends a command to the micro:bit over UART."""
        message = f"c:{command_name}:{argument}\n" if argument else f"c:{command_name}\n"
        self.microbitdev.uart.send_string(message)

    def bind_function(self, command_name, function):
        """Binds a function to be called when a specific command is received."""
        self.command_callbacks[command_name] = function
        print(self.command_callbacks)
        # If not already listening, set up listener
        if not self.is_listening:
            self.microbitdev.uart.receive_string(self.event_receiver)
            self.is_listening = True

    def event_receiver(self, rxstring):
        """Handles incoming strings, calling bound functions if command matches."""
        rxstring = rxstring.strip()
        # Check if the string matches the expected format
        if rxstring.startswith('c:'):
            parts = rxstring[2:].split(':', 1)
            command = parts[0]
            value = parts[1] if len(parts) > 1 else None  # Value is optional
            
            if command in self.command_callbacks:
                if value is not None:
                    self.command_callbacks[command](value)
                else:
                    self.command_callbacks[command]()
