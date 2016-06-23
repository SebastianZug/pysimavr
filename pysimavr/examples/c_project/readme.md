##How to run the example##

Depending on your needs you can compile and run the project in two different
ways:
  1. Use the the exemplary Makefile. It combines all steps for compiling and
	   linking a c project. Hence,

		 make run

     builds your program and starts a python script that executes the elf file
		 in pysimavr.

  2. Use the python script compileAndRun.py for controlling the build process
	   and executing the maschine code.

		 python compileAndRun
