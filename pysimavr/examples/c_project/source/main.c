///////////////////////////////////////////////////////////////////////////////
// Sebastian Zug, Otto-von-Guericke University Magdeburg, Germany
//
// Evaluation of in-code profiling for AVR applications
//
// Measurement    Comments
// 1              Determining the delay caused by the stop watch functions
// 2              Evaluate the duration of a specific number of cycles
// 3              Duration of a printf for float values
//
// The inline assembler was generated appliing
// http://bretmulvey.com/avrdelay.html
// The Arduino micro() and milli() were used for the implementation.
// Its analysis on
// https://ucexperiment.wordpress.com/2012/03/17/examination-of-the-arduino-micros-function/
// was very helpful.
///////////////////////////////////////////////////////////////////////////////

#include <avr/io.h>
#include <avr/interrupt.h>

#include "AVR_UART0_writeSerial.h"
#include "AVR_TIMER0_stopwatch.h"
#include <util/delay.h>

FILE usart0_str = FDEV_SETUP_STREAM(USART0SendByte, USART0ReceiveByte, _FDEV_SETUP_RW);

int main()
{
    stdin=stdout=&usart0_str;
    USART0Init();
    printf("\nLet's evaluate the duration of a program code!\n");

    init_timer();
    sei();

    // prepare measurements
    unsigned long start;
    unsigned long stop;

    printf("\nMEASUREMENT 1 - How much time takes the pure measurement function?\n");
    printf("--------------------------------------------------------------------\n");
    printf("We run start and stop without any application code in between\n");
    start = micros();
    stop = micros();
    printf("First run  = %3.0ld [us] (%i CPU cycles)\n",
                                     (stop-start),
                                     (stop-start)*clockCyclesPerMicrosecond() );
    start = micros();
    stop = micros();
    printf("Second run = %3.0ld [us] (%i CPU cycles)\n",
                                     (stop-start),
                                     (stop-start)*clockCyclesPerMicrosecond() );
    start = micros();
    stop = micros();
    printf("Third run  = %3.0ld [us] (%i CPU cycles)\n",
                                     (stop-start),
                                     (stop-start)*clockCyclesPerMicrosecond() );
    printf("The resolution of of the timer is  %i / %7.0f = %4.0f us\n",
                  clockPrescaler, (float)F_CPU,
                  clockPrescaler *  1000000L / (float)F_CPU);
    printf("The micros() function executes up to 24 opcodes. Hence, we have to  \n");
    printf("consider approximatly %2.0f us for this.\n", 24/(float)(clockCyclesPerMicrosecond()));


    printf("\nMEASUREMENT 2 - Check the runtime of a method \n");
    printf("--------------------------------------------------------------------\n");
    printf("The following assemble example runs 800 cycles that means %5.0f [us]\n",
            (float)clockCyclesToMicroseconds(800));
    printf("in the current configuration. \n");

    int a;
    for( a = 1; a < 12; a++){
        start = micros();
        asm volatile (
            "    ldi  r18, 2"	"\n"
            "    ldi  r19, 9"	"\n"
            "1:  dec  r19"	"\n"
            "    brne 1b"	"\n"
            "    dec  r18"	"\n"
            "    brne 1b"	"\n"
        );
        stop = micros();
        printf("%3dus ",(stop - start));
    }
    printf("\n");

    printf("\nMEASUREMENT 3 - How long does a printf take?\n");
    printf("--------------------------------------------------------------------\n");
    float myfloat =3.14159265359;
    start = micros();
    fprintf(stdout,"Print arbitary float value = %1.8f\n", myfloat);
    stop = micros();
    printf("Duration of a printf fload = %ld [us] \n",(stop - start));
    printf("Suprised?\n");

    return 0;
}
