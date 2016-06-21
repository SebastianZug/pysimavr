# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_uart_udp', [dirname(__file__)])
        except ImportError:
            import _uart_udp
            return _uart_udp
        if fp is not None:
            try:
                _mod = imp.load_module('_uart_udp', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _uart_udp = swig_import_helper()
    del swig_import_helper
else:
    import _uart_udp
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_uart_udp.IRQ_UART_UDP_BYTE_IN_swigconstant(_uart_udp)
IRQ_UART_UDP_BYTE_IN = _uart_udp.IRQ_UART_UDP_BYTE_IN

_uart_udp.IRQ_UART_UDP_BYTE_OUT_swigconstant(_uart_udp)
IRQ_UART_UDP_BYTE_OUT = _uart_udp.IRQ_UART_UDP_BYTE_OUT

_uart_udp.IRQ_UART_UDP_COUNT_swigconstant(_uart_udp)
IRQ_UART_UDP_COUNT = _uart_udp.IRQ_UART_UDP_COUNT

_uart_udp.uart_udp_fifo_overflow_f_swigconstant(_uart_udp)
uart_udp_fifo_overflow_f = _uart_udp.uart_udp_fifo_overflow_f

_uart_udp.uart_udp_fifo_fifo_size_swigconstant(_uart_udp)
uart_udp_fifo_fifo_size = _uart_udp.uart_udp_fifo_fifo_size
class uart_udp_fifo_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, uart_udp_fifo_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, uart_udp_fifo_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["buffer"] = _uart_udp.uart_udp_fifo_t_buffer_set
    __swig_getmethods__["buffer"] = _uart_udp.uart_udp_fifo_t_buffer_get
    if _newclass:
        buffer = _swig_property(_uart_udp.uart_udp_fifo_t_buffer_get, _uart_udp.uart_udp_fifo_t_buffer_set)
    __swig_setmethods__["read"] = _uart_udp.uart_udp_fifo_t_read_set
    __swig_getmethods__["read"] = _uart_udp.uart_udp_fifo_t_read_get
    if _newclass:
        read = _swig_property(_uart_udp.uart_udp_fifo_t_read_get, _uart_udp.uart_udp_fifo_t_read_set)
    __swig_setmethods__["write"] = _uart_udp.uart_udp_fifo_t_write_set
    __swig_getmethods__["write"] = _uart_udp.uart_udp_fifo_t_write_get
    if _newclass:
        write = _swig_property(_uart_udp.uart_udp_fifo_t_write_get, _uart_udp.uart_udp_fifo_t_write_set)
    __swig_setmethods__["flags"] = _uart_udp.uart_udp_fifo_t_flags_set
    __swig_getmethods__["flags"] = _uart_udp.uart_udp_fifo_t_flags_get
    if _newclass:
        flags = _swig_property(_uart_udp.uart_udp_fifo_t_flags_get, _uart_udp.uart_udp_fifo_t_flags_set)

    def __init__(self):
        this = _uart_udp.new_uart_udp_fifo_t()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _uart_udp.delete_uart_udp_fifo_t
    __del__ = lambda self: None
uart_udp_fifo_t_swigregister = _uart_udp.uart_udp_fifo_t_swigregister
uart_udp_fifo_t_swigregister(uart_udp_fifo_t)

class uart_udp_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, uart_udp_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, uart_udp_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["irq"] = _uart_udp.uart_udp_t_irq_set
    __swig_getmethods__["irq"] = _uart_udp.uart_udp_t_irq_get
    if _newclass:
        irq = _swig_property(_uart_udp.uart_udp_t_irq_get, _uart_udp.uart_udp_t_irq_set)
    __swig_setmethods__["avr"] = _uart_udp.uart_udp_t_avr_set
    __swig_getmethods__["avr"] = _uart_udp.uart_udp_t_avr_get
    if _newclass:
        avr = _swig_property(_uart_udp.uart_udp_t_avr_get, _uart_udp.uart_udp_t_avr_set)
    __swig_setmethods__["thread"] = _uart_udp.uart_udp_t_thread_set
    __swig_getmethods__["thread"] = _uart_udp.uart_udp_t_thread_get
    if _newclass:
        thread = _swig_property(_uart_udp.uart_udp_t_thread_get, _uart_udp.uart_udp_t_thread_set)
    __swig_setmethods__["s"] = _uart_udp.uart_udp_t_s_set
    __swig_getmethods__["s"] = _uart_udp.uart_udp_t_s_get
    if _newclass:
        s = _swig_property(_uart_udp.uart_udp_t_s_get, _uart_udp.uart_udp_t_s_set)
    __swig_setmethods__["peer"] = _uart_udp.uart_udp_t_peer_set
    __swig_getmethods__["peer"] = _uart_udp.uart_udp_t_peer_get
    if _newclass:
        peer = _swig_property(_uart_udp.uart_udp_t_peer_get, _uart_udp.uart_udp_t_peer_set)
    __swig_setmethods__["xon"] = _uart_udp.uart_udp_t_xon_set
    __swig_getmethods__["xon"] = _uart_udp.uart_udp_t_xon_get
    if _newclass:
        xon = _swig_property(_uart_udp.uart_udp_t_xon_get, _uart_udp.uart_udp_t_xon_set)
    __swig_setmethods__["_in"] = _uart_udp.uart_udp_t__in_set
    __swig_getmethods__["_in"] = _uart_udp.uart_udp_t__in_get
    if _newclass:
        _in = _swig_property(_uart_udp.uart_udp_t__in_get, _uart_udp.uart_udp_t__in_set)
    __swig_setmethods__["out"] = _uart_udp.uart_udp_t_out_set
    __swig_getmethods__["out"] = _uart_udp.uart_udp_t_out_get
    if _newclass:
        out = _swig_property(_uart_udp.uart_udp_t_out_get, _uart_udp.uart_udp_t_out_set)
    __swig_setmethods__["_terminate"] = _uart_udp.uart_udp_t__terminate_set
    __swig_getmethods__["_terminate"] = _uart_udp.uart_udp_t__terminate_get
    if _newclass:
        _terminate = _swig_property(_uart_udp.uart_udp_t__terminate_get, _uart_udp.uart_udp_t__terminate_set)

    def __init__(self):
        this = _uart_udp.new_uart_udp_t()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _uart_udp.delete_uart_udp_t
    __del__ = lambda self: None
uart_udp_t_swigregister = _uart_udp.uart_udp_t_swigregister
uart_udp_t_swigregister(uart_udp_t)


def uart_udp_init(avr, b):
    return _uart_udp.uart_udp_init(avr, b)
uart_udp_init = _uart_udp.uart_udp_init

def uart_udp_connect(p, uart):
    return _uart_udp.uart_udp_connect(p, uart)
uart_udp_connect = _uart_udp.uart_udp_connect

def uart_udp_terminate(p):
    return _uart_udp.uart_udp_terminate(p)
uart_udp_terminate = _uart_udp.uart_udp_terminate
# This file is compatible with both classic and new-style classes.


