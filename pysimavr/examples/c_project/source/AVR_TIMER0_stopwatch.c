#include "AVR_TIMER0_stopwatch.h"

volatile unsigned long timer0_overflow_count = 0;
volatile unsigned long timer0_millis = 0;
static unsigned char timer0_fract = 0;

ISR(TIMER0_OVF_vect)
{
  // copy these to local variables so they can be stored in registers
  // (volatile variables must be read from memory on every access)
  unsigned long m = timer0_millis;
  unsigned char f = timer0_fract;

  m += MILLIS_INC;
  f += FRACT_INC;
  if (f >= FRACT_MAX) {
    f -= FRACT_MAX;
    m += 1;
  }

  timer0_fract = f;
  timer0_millis = m;
  timer0_overflow_count++;
}

void init_timer(){
  // fast pwm
  TCCR0A |= (1 << WGM01) | (1 << WGM00);
  // this combination is for the standard 168/328/1280/2560
  // prescaler 64
  // CS02 CS01  CS00
  // 0 	  0 	  0 	Stop
  // 0 	  0   	1 	CPU-clock speed
  // 0   	1 	  0 	CPU-clock speed / 8
  // 0   	1   	1 	CPU-clock speed / 64
  // 1 	  0   	0 	CPU-clock speed / 256
  // 1   	0   	1 	CPU-clock speed / 1024
  TCCR0B |= (1 << CS01) | (1 << CS00);   // prescaler = 64
  //TCCR0B |= (1 << CS01);                    // prescaler = 8
  // timer interrupt on
  TIMSK0 |= (1 << TOIE0);
}

unsigned long millis()
{
  unsigned long m;
  uint8_t oldSREG = SREG;
  // disable interrupts while we read timer0_millis or we might get an
  // inconsistent value (e.g. in the middle of a write to timer0_millis)
  cli();
  m = timer0_millis;
  SREG = oldSREG;
  return m;
}

unsigned long micros() {
    unsigned long m;
    uint8_t oldSREG = SREG, t;

    cli();
    m = timer0_overflow_count;
#if defined(TCNT0)
    t = TCNT0;
#elif defined(TCNT0L)
    t = TCNT0L;
#else
    #error TIMER 0 not defined
#endif

#ifdef TIFR0
    if ((TIFR0 & _BV(TOV0)) && (t & 255))
        m++;
#else
    if ((TIFR & _BV(TOV0)) && (t & 255))
        m++;
#endif
    SREG = oldSREG;
    return ((m << 8) + t) * (clockPrescaler / clockCyclesPerMicrosecond());
}
