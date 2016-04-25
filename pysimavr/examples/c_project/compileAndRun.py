from entrypoint2 import entrypoint
from pyavrutils.avrgcc import AvrGcc, AvrGccCompileError
from pysimavr.sim import ArduinoSim
import time

def prepareHeaderFiles (names):
  headers = {}
  for name in names:
    with open(name) as f:
      content = f.readlines()
    headers[name]=''.join(content)
  if headers == {}:
    headers = None
  return headers

mcu='atmega328'
f_cpu=1000000

sources = ['main.c', 'AVR_UART0_writeSerial.c', 'AVR_TIMER0_stopwatch.c']
headerfiles = ['AVR_UART0_writeSerial.h', 'AVR_TIMER0_stopwatch.h']

cc = AvrGcc(mcu = mcu)
cc.f_cpu = f_cpu
cc.optimization = 's'
cc.options_extra = ['-uvfprintf' ,'-lprintf_flt', '-lm', '-DF_CPU=%d'%f_cpu]

print '-------------------------------------------------------------------'
print  'compiler version:', cc.version()
print '-------------------------------------------------------------------'
print 'Project targets'
for source in sources:
    print '  '+source
print '-------------------------------------------------------------------'

error = False

try:
    #print "Command list"
    #print cc.command_list(sources = sources)

    cc.build(sources = sources)    
    
except:
    error = True
    print cc.error_text
    print 'compile error'


if not error:
    print 'Temporary output file \n' + '   ' + cc.output
    size = cc.size()
    print '-------------------------------------------------------------------'
    print 'Program size \n  program =' , str(size.program_bytes).rjust(8) , '\n  data    =', str(size.data_bytes).rjust(7)
    print '-------------------------------------------------------------------'
    simulation = ArduinoSim(external_elf=cc.output,
                            mcu = mcu,
                            f_cpu=f_cpu,
                            timespan=5,
                            fps=20,
                            )
    output = simulation.get_serial()
    print output

print "Aus Maus"