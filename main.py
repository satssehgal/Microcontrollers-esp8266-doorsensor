
import machine
import time

rw = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    val1= rw.value()
    time.sleep(0.01)
    val2= rw.value()
    if val1 and not val2:
        print('Door Closed')
    elif not val1 and val2:
        print('Door Open')
