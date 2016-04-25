TARGET=analyseAssemble
MCU=atmega48
F_CPU=8000000
SOURCES=main.c

PROGRAMMER=arduino
# Programming interface (Linux)
PORT=-P/dev/ttyACM0
BAUD=-B115200

#Ab hier nichts verändern
OBJECTS=$(SOURCES:.c=.o)
CFLAGS  =-c 
# transfer the clock speed to the code
CFLAGS += -DF_CPU=$(F_CPU)
# generating assembly code including c comments
CFLAGS += -g                 
LDFLAGS= 

all: hex eeprom

hex: $(TARGET).hex

eeprom: $(TARGET)_eeprom.hex

$(TARGET).hex: $(TARGET).elf
	avr-objcopy -O ihex -j .data -j .text $(TARGET).elf $(TARGET).hex

$(TARGET)_eeprom.hex: $(TARGET).elf
	avr-objcopy -O ihex -j .eeprom --change-section-lma .eeprom=1 $(TARGET).elf $(TARGET)_eeprom.hex

$(TARGET).elf: $(OBJECTS)
	avr-gcc $(LDFLAGS) -mmcu=$(MCU) $(OBJECTS) -o $(TARGET).elf
	avr-objdump -S  $(TARGET).elf > $(TARGET).asm

.c.o:
	avr-gcc $(CFLAGS) -mmcu=$(MCU) $< -o $@

%.s : %.c
	avr-gcc -S $(CFLAGS) -mmcu=$(MCU) $< -o $@
	
size:
	avr-size --mcu=$(MCU) -C $(TARGET).elf

program:
	avrdude -p$(MCU) $(PORT) $(BAUD) -c$(PROGRAMMER) -Uflash:w:$(TARGET).hex:a

clean:
	rm -rf *.o
	rm -rf *.elf
	rm -rf *.hex
	
run:$(TARGET).elf
	python run.py --elf $(TARGET).elf --mcu $(MCU) --f_cpu $(F_CPU)