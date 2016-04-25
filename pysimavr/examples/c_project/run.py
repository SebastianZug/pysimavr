from pysimavr.sim import ArduinoSim
import argparse

def run_avr_elf(elf_file, mcu = 'atmega2560', f_cpu = 16000000):
      print "Running simulation with ... " + elf_file
   
      simulation = ArduinoSim(external_elf=elf_file,
                        mcu = mcu,
                        f_cpu=f_cpu,
                        timespan=7,
                        fps=20,
                        )
      output = simulation.get_serial()
      print output

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--elf", help="elf file, that have to be executed", type=str)
  parser.add_argument("--mcu", help="CPU type", type=str)
  parser.add_argument("--f_cpu", help="CPU clock speed", type=int)
  args = parser.parse_args()
  print args.elf, args.mcu, args.f_cpu
  
  run_avr_elf(args.elf, args.mcu, args.f_cpu)
  print "Aus Maus"
