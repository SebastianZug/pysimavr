from readAssembly import readAssembly
from pysimavr.avr import Avr
from pysimavr.firmware import Firmware
import pandas as pd
import numpy as np

[functions, command] = readAssembly('analyseAssemble.asm')

avr = Avr(mcu='atmega48', f_cpu=8000000)
firmware = Firmware('analyseAssemble.elf')
avr.load_firmware(firmware)

filtered = functions[functions['name'] == '_exit']
exit_adress = filtered.iloc[-1]['adress_int']

function_call = np.zeros((len(functions),2))

print "Press Enter to continue ... "
while True:
    if avr.pc == exit_adress:
      break
    current = command[command['adress_int'] == avr.pc]
    print current['command']
    key = raw_input()
    if key != '':
       break
    avr.step()
print avr.time_passed()
avr.terminate()

print "Aus Maus"

