from entrypoint2 import entrypoint
from pyavrutils.avrgcc import AvrGcc, AvrGccCompileError
from pysimavr.sim import ArduinoSim
import time
import glob

# define controller and clockspeed
mcu='atmega328'
f_cpu=8000000

# sourcefolder
sources = glob.glob('./source/*.c')
headerlocation = './header'

# compile the project
cc = AvrGcc(mcu = mcu)
cc.f_cpu = f_cpu
cc.options_extra = ['-I%s'%headerlocation,
                    '-uvfprintf',
                    '-lprintf_flt', '-lm', '-DF_CPU=%d'%f_cpu]

print '-------------------------------------------------------------------'
print  'compiler version:', cc.version()
print '-------------------------------------------------------------------'
print 'Project targets'
for source in sources:
    print '  '+source
print '-------------------------------------------------------------------'
print cc.command_list(sources)
error = False
try:
    cc.build(sources = sources)

except:
    error = True
    print cc.error_text

# run the project for 5 seconds
if not error:
    print 'Temporary output file \n' + '   ' + cc.output
    size = cc.size()
    print '-------------------------------------------------------------------'
    print 'Program size \n  program =' , str(size.program_bytes).rjust(8), \
          '\n  data    =', str(size.data_bytes).rjust(7)
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
