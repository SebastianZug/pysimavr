
analyseAssemble.elf:     Dateiformat elf32-avr


Disassembly of section .text:

00000000 <__vectors>:
   0:	19 c0       	rjmp	.+50     	; 0x34 <__ctors_end>
   2:	20 c0       	rjmp	.+64     	; 0x44 <__bad_interrupt>
   4:	1f c0       	rjmp	.+62     	; 0x44 <__bad_interrupt>
   6:	1e c0       	rjmp	.+60     	; 0x44 <__bad_interrupt>
   8:	1d c0       	rjmp	.+58     	; 0x44 <__bad_interrupt>
   a:	1c c0       	rjmp	.+56     	; 0x44 <__bad_interrupt>
   c:	1b c0       	rjmp	.+54     	; 0x44 <__bad_interrupt>
   e:	1a c0       	rjmp	.+52     	; 0x44 <__bad_interrupt>
  10:	19 c0       	rjmp	.+50     	; 0x44 <__bad_interrupt>
  12:	18 c0       	rjmp	.+48     	; 0x44 <__bad_interrupt>
  14:	17 c0       	rjmp	.+46     	; 0x44 <__bad_interrupt>
  16:	16 c0       	rjmp	.+44     	; 0x44 <__bad_interrupt>
  18:	15 c0       	rjmp	.+42     	; 0x44 <__bad_interrupt>
  1a:	14 c0       	rjmp	.+40     	; 0x44 <__bad_interrupt>
  1c:	13 c0       	rjmp	.+38     	; 0x44 <__bad_interrupt>
  1e:	12 c0       	rjmp	.+36     	; 0x44 <__bad_interrupt>
  20:	11 c0       	rjmp	.+34     	; 0x44 <__bad_interrupt>
  22:	10 c0       	rjmp	.+32     	; 0x44 <__bad_interrupt>
  24:	0f c0       	rjmp	.+30     	; 0x44 <__bad_interrupt>
  26:	0e c0       	rjmp	.+28     	; 0x44 <__bad_interrupt>
  28:	0d c0       	rjmp	.+26     	; 0x44 <__bad_interrupt>
  2a:	0c c0       	rjmp	.+24     	; 0x44 <__bad_interrupt>
  2c:	0b c0       	rjmp	.+22     	; 0x44 <__bad_interrupt>
  2e:	0a c0       	rjmp	.+20     	; 0x44 <__bad_interrupt>
  30:	09 c0       	rjmp	.+18     	; 0x44 <__bad_interrupt>
  32:	08 c0       	rjmp	.+16     	; 0x44 <__bad_interrupt>

00000034 <__ctors_end>:
  34:	11 24       	eor	r1, r1
  36:	1f be       	out	0x3f, r1	; 63
  38:	cf ef       	ldi	r28, 0xFF	; 255
  3a:	d2 e0       	ldi	r29, 0x02	; 2
  3c:	de bf       	out	0x3e, r29	; 62
  3e:	cd bf       	out	0x3d, r28	; 61
  40:	40 d0       	rcall	.+128    	; 0xc2 <main>
  42:	64 c0       	rjmp	.+200    	; 0x10c <_exit>

00000044 <__bad_interrupt>:
  44:	dd cf       	rjmp	.-70     	; 0x0 <__vectors>

00000046 <myFunction>:
#include<avr/io.h>

int myFunction(unsigned char a){
  46:	cf 93       	push	r28
  48:	df 93       	push	r29
  4a:	1f 92       	push	r1
  4c:	cd b7       	in	r28, 0x3d	; 61
  4e:	de b7       	in	r29, 0x3e	; 62
  50:	89 83       	std	Y+1, r24	; 0x01
  return a % 5;
  52:	29 81       	ldd	r18, Y+1	; 0x01
  54:	8d ec       	ldi	r24, 0xCD	; 205
  56:	28 9f       	mul	r18, r24
  58:	81 2d       	mov	r24, r1
  5a:	11 24       	eor	r1, r1
  5c:	98 2f       	mov	r25, r24
  5e:	96 95       	lsr	r25
  60:	96 95       	lsr	r25
  62:	89 2f       	mov	r24, r25
  64:	88 0f       	add	r24, r24
  66:	88 0f       	add	r24, r24
  68:	89 0f       	add	r24, r25
  6a:	92 2f       	mov	r25, r18
  6c:	98 1b       	sub	r25, r24
  6e:	89 2f       	mov	r24, r25
  70:	90 e0       	ldi	r25, 0x00	; 0
}
  72:	0f 90       	pop	r0
  74:	df 91       	pop	r29
  76:	cf 91       	pop	r28
  78:	08 95       	ret

0000007a <toggle>:

void toggle( volatile uint8_t* Port, uint8_t Pin )
{
  7a:	cf 93       	push	r28
  7c:	df 93       	push	r29
  7e:	00 d0       	rcall	.+0      	; 0x80 <toggle+0x6>
  80:	1f 92       	push	r1
  82:	cd b7       	in	r28, 0x3d	; 61
  84:	de b7       	in	r29, 0x3e	; 62
  86:	9a 83       	std	Y+2, r25	; 0x02
  88:	89 83       	std	Y+1, r24	; 0x01
  8a:	6b 83       	std	Y+3, r22	; 0x03
  *Port ^= ( 1 << Pin );
  8c:	89 81       	ldd	r24, Y+1	; 0x01
  8e:	9a 81       	ldd	r25, Y+2	; 0x02
  90:	fc 01       	movw	r30, r24
  92:	80 81       	ld	r24, Z
  94:	48 2f       	mov	r20, r24
  96:	8b 81       	ldd	r24, Y+3	; 0x03
  98:	28 2f       	mov	r18, r24
  9a:	30 e0       	ldi	r19, 0x00	; 0
  9c:	81 e0       	ldi	r24, 0x01	; 1
  9e:	90 e0       	ldi	r25, 0x00	; 0
  a0:	02 c0       	rjmp	.+4      	; 0xa6 <toggle+0x2c>
  a2:	88 0f       	add	r24, r24
  a4:	99 1f       	adc	r25, r25
  a6:	2a 95       	dec	r18
  a8:	e2 f7       	brpl	.-8      	; 0xa2 <toggle+0x28>
  aa:	84 27       	eor	r24, r20
  ac:	28 2f       	mov	r18, r24
  ae:	89 81       	ldd	r24, Y+1	; 0x01
  b0:	9a 81       	ldd	r25, Y+2	; 0x02
  b2:	fc 01       	movw	r30, r24
  b4:	20 83       	st	Z, r18
}
  b6:	0f 90       	pop	r0
  b8:	0f 90       	pop	r0
  ba:	0f 90       	pop	r0
  bc:	df 91       	pop	r29
  be:	cf 91       	pop	r28
  c0:	08 95       	ret

000000c2 <main>:

int main()
{
  c2:	cf 93       	push	r28
  c4:	df 93       	push	r29
  c6:	1f 92       	push	r1
  c8:	cd b7       	in	r28, 0x3d	; 61
  ca:	de b7       	in	r29, 0x3e	; 62
  DDRC = 0xFF;    //configure portC as output
  cc:	87 e2       	ldi	r24, 0x27	; 39
  ce:	90 e0       	ldi	r25, 0x00	; 0
  d0:	2f ef       	ldi	r18, 0xFF	; 255
  d2:	fc 01       	movw	r30, r24
  d4:	20 83       	st	Z, r18
 
  unsigned char i;
  for (i=0; i<5; i++)
  d6:	19 82       	std	Y+1, r1	; 0x01
  d8:	10 c0       	rjmp	.+32     	; 0xfa <main+0x38>
  {
    if (myFunction(i)>3){
  da:	89 81       	ldd	r24, Y+1	; 0x01
  dc:	b4 df       	rcall	.-152    	; 0x46 <myFunction>
  de:	84 30       	cpi	r24, 0x04	; 4
  e0:	91 05       	cpc	r25, r1
  e2:	44 f0       	brlt	.+16     	; 0xf4 <main+0x32>
      toggle(PORTC, PD7 );
  e4:	88 e2       	ldi	r24, 0x28	; 40
  e6:	90 e0       	ldi	r25, 0x00	; 0
  e8:	fc 01       	movw	r30, r24
  ea:	80 81       	ld	r24, Z
  ec:	88 2f       	mov	r24, r24
  ee:	90 e0       	ldi	r25, 0x00	; 0
  f0:	67 e0       	ldi	r22, 0x07	; 7
  f2:	c3 df       	rcall	.-122    	; 0x7a <toggle>
int main()
{
  DDRC = 0xFF;    //configure portC as output
 
  unsigned char i;
  for (i=0; i<5; i++)
  f4:	89 81       	ldd	r24, Y+1	; 0x01
  f6:	8f 5f       	subi	r24, 0xFF	; 255
  f8:	89 83       	std	Y+1, r24	; 0x01
  fa:	89 81       	ldd	r24, Y+1	; 0x01
  fc:	85 30       	cpi	r24, 0x05	; 5
  fe:	68 f3       	brcs	.-38     	; 0xda <main+0x18>
  {
    if (myFunction(i)>3){
      toggle(PORTC, PD7 );
    }
  }
  return 0;
 100:	80 e0       	ldi	r24, 0x00	; 0
 102:	90 e0       	ldi	r25, 0x00	; 0
 104:	0f 90       	pop	r0
 106:	df 91       	pop	r29
 108:	cf 91       	pop	r28
 10a:	08 95       	ret

0000010c <_exit>:
 10c:	f8 94       	cli

0000010e <__stop_program>:
 10e:	ff cf       	rjmp	.-2      	; 0x10e <__stop_program>
