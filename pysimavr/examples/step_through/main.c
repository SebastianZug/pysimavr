#include<avr/io.h>

int myFunction(unsigned char a){
  return a % 5;
}

void toggle( volatile uint8_t* Port, uint8_t Pin )
{
  *Port ^= ( 1 << Pin );
}

int main()
{
  DDRC = 0xFF;    //configure portC as output
 
  unsigned char i;
  for (i=0; i<5; i++)
  {
    if (myFunction(i)>3){
      toggle(PORTC, PD7 );
    }
  }
  return 0;
}