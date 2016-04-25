from readAssembly import readAssembly
from pysimavr.avr import Avr
from pysimavr.firmware import Firmware
import pandas as pd
import numpy as np

functions, command = readAssembly('analyseAssemble.asm')

avr = Avr(mcu='atmega48', f_cpu=8000000)
firmware = Firmware('analyseAssemble.elf')
avr.load_firmware(firmware)

filtered = functions[functions['name'] == '_exit']
exit_adress = filtered.iloc[-1]['adress_int']

function_call = np.zeros((len(functions),2))

started = avr.time_passed()
while True:
    if avr.pc == exit_adress:
      break
    index = functions[functions['adress_int'] == avr.pc].index
    if index:
      function_call[index,1] = avr.backend.cycle  - started;
      function_call[index,0] += 1
      started = avr.backend.cycle 
    avr.step()
print avr.time_passed()
avr.terminate()

functions['executed'] = function_call[:,0]
functions['duration'] = function_call[:,1]
print functions

print "Aus Maus"

