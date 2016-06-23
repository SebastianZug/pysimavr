#include <stdio.h>
#include <math.h>
#include <avr/io.h>
#include <avr/interrupt.h>

// if you change the prescaler value you have to adapt the configuration
// of the timer in AVR_TIMER_stopwatch.c
#define clockPrescaler 64
#define clockCyclesPerMicrosecond() ( F_CPU / 1000000L )
#define clockCyclesToMicroseconds(a) ((a) / clockCyclesPerMicrosecond() )
// the prescaler is set so that timer0 ticks every 64 clock cycles, and the
// the overflow handler is called every 256 ticks.
#define MICROSECONDS_PER_TIMER0_OVERFLOW (clockCyclesToMicroseconds(clockPrescaler * 256))
// the whole number of milliseconds per timer0 overflow
#define MILLIS_INC (MICROSECONDS_PER_TIMER0_OVERFLOW / 1000)
// the fractional number of milliseconds per timer0 overflow. we shift right
// by three to fit these numbers into a byte. (for the clock speeds we care
// about - 8 and 16 MHz - this doesn't lose precision.)
#define FRACT_INC ((MICROSECONDS_PER_TIMER0_OVERFLOW % 1000) >> 3)
#define FRACT_MAX (1000 >> 3)
#define TIMER_GRANULARITY (clockPrescaler / clockCyclesPerMicrosecond() )

void init_timer();
unsigned long millis();
unsigned long micros();
