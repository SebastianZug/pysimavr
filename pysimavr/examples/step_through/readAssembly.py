import pyparsing as pp
import pandas as pd
import numpy as np

def readAssembly(filename):
  # Patterns for scanning function names
  digits = "0123456789"
  hex_signs = "abcdef"
  control_signs = ",.-+ "
  lparen = pp.Literal( "<" )
  rparen = pp.Literal( ">" )
  colon = pp.Literal( ":" )
  address = pp.Word( digits + hex_signs )
  opcode_element = pp.Word( digits + hex_signs, exact=2) 
  # Examples
  # 00000044 <__bad_interrupt>:
  # 00000046 <myFunction>:
  # 00000080 <__udivmodqi4_ep>:
  functionname = pp.Word( pp.alphas + digits + "_")
  functionentry = pp.LineStart() + address + lparen + functionname +rparen + colon +  pp.LineEnd()

  #  Patterns for scanning opcodes
  command = pp.Word( pp.alphas + digits + control_signs)
  comment = pp.Word( pp.alphas + digits + control_signs + '<' + '>' + '_')
  #  Examples
  #  40: 05 d0         rcall .+10      ; 0x4c <main>
  #  34: 11 24         eor r1, r1
  commands = address + pp.Suppress(":") + opcode_element + opcode_element + command +  pp.Optional('; ') + pp.Optional(comment) 

  functions = []
  code = []
  comments = ''
  lineNumber = 0
  for t in [line.rstrip('\n') for line in open(filename)]:
      # two steps of parsing 
      # - look for function headers
      # - look for opcodes 
      # - (optional c comments are catshed in the exception handler)  
      lineNumber = lineNumber + 1
      function_found = False
      try:
          function_header = functionentry.parseString(t)
          current_function_name = function_header[2]
          functions.append({'name':current_function_name, 
                            'adress_hex':'0x'+function_header[0].lstrip('0'), 
                            'adress_int': int('0x'+function_header[0],16),
                            'linenumber': lineNumber,
                            'executed': 0,
                            'duration': 0})
          function_found = True
      except pp.ParseException, pe:
          pass
      if not function_found:
          try:
              command = commands.parseString(t)
              code.append({'function':current_function_name,
                          'adress_hex': '0x'+command[0],
                          'adress_int': int('0x'+command[0],16),
                          'opcode' : command[1] + ' ' + command[2],
                          'command': ' '.join(command[3].split()),
                          'commments' : comments})
              comments = ''
          except pp.ParseException, pe:
              if function_found == False:
                  comments = comments + t
              pass
  functions = pd.DataFrame(functions)
  code =  pd.DataFrame(code)
  
  return [functions, code]