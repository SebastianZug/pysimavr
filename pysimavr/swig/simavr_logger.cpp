#include <sstream>
using namespace std;
#include "simavr_logger.h"
#include <stdio.h>
#include <stdarg.h>
#include "sim_avr.h"
#include "avr_uart.h"

stringstream oss;

char* mem_logger_read_line()
{
    static char buff[256];
    buff[0] = 0;

    if (oss.rdbuf()->in_avail())
        oss.getline(buff, 256);

    return buff;
}

void mem_logger_print(avr_t* avr, const int level, const char * format, va_list args)
{
//    va_list args;
//    va_start(args, format);
    char buff[100];
    vsnprintf(buff, 100, format, args);
    oss.clear();
    oss << buff;
//    va_end(args);
}

void use_mem_logger()
{
    avr_global_logger_set(mem_logger_print);
}

