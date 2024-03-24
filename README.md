# Simple BLE events test setup

This is a program that lets you send events (with optional integer arguments). You can call the events what you want, but the names must match on the micro:bit end.

It is to be used in conjunction with the https://github.com/jaustin/pxt-bluetooth-commands/ extension

This script is suppposed to run in conjunction with the following MakeCode programme:

https://makecode.microbit.org/S05435-27154-54062-42140

# Usage of the basic example

Install deps:

```pip install -r requirements.txt```

Put the example on your micro:bit (amend for your platform)

```cp microbit-example.hex /Volumes/MICROBIT/```

This script will scroll the name of your micro:bit on the display. [Also, you can derive the name from the pairing pattern/graph](https://support.microbit.org/support/solutions/articles/19000067679-how-to-find-the-name-of-your-micro-bit#:~:text=Finding%20the%20name%20of%20the%20micro%3Abit%20from%20the%20pairing%20pattern)

Edit the script to change the micro:bit name
```open microbit_ble.py```

Run the sample
```python3 microbit_ble.py```

# Usage in general

This expects you to write code both on the micro:bit (in MakeCode - https://makecode.microbit.org) and in Python on the host system. You can pick your event names and arguments to represent something relevant to you. 

I don't have the concept of a 'response' because it would require tracking events and their response in a more synchronous way - you can layer your own 'response' command over this if you need, I guess.

# Skipping my PoC module

To present a simple API and to get an idea of what this might feel like, I wrapped the very complete/featurefull KaspersMicrobit library in a little wrapper. You might not want that, in which case the `microbit_ble_rawuarts.py` file is a good starting point to work against the MakeCode example, or indeed just against a simple MakeCode uart where you can do your own parsing/command interface.
