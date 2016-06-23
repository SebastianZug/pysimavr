##How to run the example

Depending on your needs you can compile and run the project in two different
ways:
  1. Use the the exemplary Makefile. It combines all steps for compiling and
	   linking a c project. Hence,

		 make run

     builds your program and starts a python script that executes the elf file
		 in pysimavr.

  2. Use the python script compileAndRun.py for controlling the build process
	   and executing the maschine code.

		 python compileAndRun.py

##Output

The small c project combines 2 specific tasks, a generic UART output
and a two Timer0 based functions.  micro() is used to illustrate
the use of pysimavr while "profiling" some code snippets. The output
illustrates the limits of this method. Depending on the configuration of the
timer the resolution of micro() is limited. The default parameters us a
prescaler of 64, consequently we have a step width of 8us.

      ▶ python compileAndRun.py
      -------------------------------------------------------------------
      compiler version: 4.9.2
      -------------------------------------------------------------------
      Project targets
        ./source/AVR_UART0_writeSerial.c
        ./source/main.c
        ./source/AVR_TIMER0_stopwatch.c
      -------------------------------------------------------------------
      Program size
        program =     4994
        data    =     859
      -------------------------------------------------------------------

      Let's evaluate the duration of a program code!

      MEASUREMENT 1 - How much time takes the pure measurement function?
      --------------------------------------------------------------------
      We run start and stop without any application code in between
      First run  =   8 [us] (64 CPU cycles)
      Second run =   8 [us] (64 CPU cycles)
      Third run  =   8 [us] (64 CPU cycles)
      The resolution of of the timer is  64 / 8000000 =    8 us
      The micros() function executes up to 24 opcodes. Hence, we have to  
      consider approximately 3 us for this.

      MEASUREMENT 2 - Check the runtime of a method
      --------------------------------------------------------------------
      The following assemble example runs 800 cycles that means   100 [us]
      in the current configuration.
      104us 104us 112us 112us 104us 112us 104us 112us 104us 104us 112us

      MEASUREMENT 3 - How long does a printf take?
      --------------------------------------------------------------------
      Print arbitrary float value = 3.14159270
      Duration of a printf float = 46952 [us]
      Surprised?

      Aus Maus
