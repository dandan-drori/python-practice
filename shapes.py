def square(length):
  line = ''
  for i in range(length):
    line += '* '
  for j in range(length):
    print(line)

def triangle(length):
  line = ''
  for i in range(length):
    line += '* '
    print(line)

def upside_triangle(length):
  for i in range(length):
    line = ''
    stars = i + 1
    spaces = length - stars
    line += (length - i) * ' '
    line += '*' * stars
    line += (length - i) * ' '
    print(line)

def rhombos(length):
  for i in range(length + 1):
    line = ''
    for j in range(length):
      if (j == (length + 1) // 2 - i) or j == length // 2 - (length - i):
        line += '*'
      elif j == (length + 1) // 2:
        line += '='
      elif j == (length + 1) // 2 + i or j == length // 2 + (length - i):
        line += '+'
      else:
        line += ' '
    print(line)    

def main():
  print('')
  square(5)
  print('')
  triangle(5)
  print('')
  upside_triangle(5)
  print('')
  rhombos(8)


main()



