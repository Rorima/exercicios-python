def generator(start, end):
  current = start
  while True:
    yield current
    current += 1
    if current >= end:
      break


for x in generator(1, 10):
  print(x)
