///////////////////////////////////////////////////////////////////////////////
// Sebastian Zug, Otto-von-Guericke University Magdeburg, Germany
//
// Evaluation of in-code profiling for AVR applications
// 
// Measurement    Comments
// 1              Determining the delay caused by the stop watch functions
// 2              Determining the granulariy of the results (4us)
// 3              Duration of a printf for float values
//
// The inline assembler was generated appliing 
// http://bretmulvey.com/avrdelay.html
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
    // no delay due to an application 
    stop = micros();
    printf("First run  = %3.0ld [us]\n",(stop-start));
    start = micros();
    // no delay due to an application 
    stop = micros();
    printf("Second run = %3.0ld [us]\n",(stop-start));
    start = micros();
    // no delay due to an application 
    stop = micros();
    printf("Third run  = %3.0ld [us]\n",(stop-start));
    printf("The true value is around 1us[!] but due to the granularity we\n");
    printf("measure %2.1fus or (very rarely) %2.1fus \n", (float)TIMER_GRANULARITY, 2*(float)TIMER_GRANULARITY);
 
    printf("\nMEASUREMENT 2 - Check the accurate delay methods of avrlibc \n");
    printf("--------------------------------------------------------------------\n");
    printf("10 excecution of a 200us inline assembler take:\n");
    int a;
    for( a = 1; a < 10; a++){
        start = micros();
        _delay_us(200);
        stop = micros();
        printf("%3dus ",(stop - start));
    }
    printf("\n");
  
    printf("\nMEASUREMENT 3 - How long does a printf take?\n");
    printf("--------------------------------------------------------------------\n");
    start = micros();
    float myfloat =3.14159265359;
    fprintf(stdout,"Print arbitary float value = %1.8f\n", myfloat);
    stop = micros();
    printf("Duration of a printf fload = %ld [us] \n",(stop - start));
    printf("Suprised?\n");

    return 0;
}
