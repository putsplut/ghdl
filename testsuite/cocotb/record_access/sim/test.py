#!/usr/bin/python2.7

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge
from simulator import get_sim_time

@cocotb.test(timeout=100)
def proto(dut):

  dut.stl_in <= 0xa6
  yield Timer(1)
  
  print dut.stl_in.name
  print "  ", dut.stl_in
  # Odd behavior: value doesn't update until an additional yield!
  yield Timer(1)
  print '[After another yield]'
  print "  ", dut.stl_in
  print "  ", hex(int(dut.stl_in.value))
  for idx in reversed(range(1,9)):
    v = dut.stl_in[idx]
    print ' ',idx,'->',v
  print

  yield Timer(1)
  print dut.stl_out.name
  print "  ", dut.stl_out
  print "  ", hex(int(dut.stl_out.value))
  for idx in range(8):
    v = dut.stl_out[idx]
    n = dut.stl_out[idx].name
    print ' ',idx,'->',v, n
  print


  print '[Before Set]'
  print dut.foo_in
  print dut.foo_in.a
  print dut.foo_in.a[3]
  dut.foo_in.a <= 0x15
  dut.foo_in.b <= 0x6
  yield Timer(1)
  print '[One Yield]'
  print dut.foo_in.a
  print dut.foo_in.a[3]
  yield Timer(1)
  print '[Second Yield]'
  print dut.foo_in.a
  print dut.foo_in.a[3]
  print
 
  if False: # Aldec crashes on all of these
    print '[Looking at a constant]'
    v = dut.const_foo.b
    print v
    print '[Looking at more complex constant]'
    v = dut.const_foov[0].b
    print v

  if True:
    print '[Looking at foo_t internal]'
    v = dut.sig_foo.b
    print v
    print '[Looking at foo_vec_t internal]'
    v = dut.sig_foov[0].b
    print v
    for e in range(3):
      n = dut.sig_foov[e].name
      print n
      v = dut.sig_foov[e].b
      print '######', v
      for idx in range(3):
        v = dut.sig_foov[e].b[idx]
        n = dut.sig_foov[e].b[idx].name
        print ' ',idx,'->',v, n
    print
