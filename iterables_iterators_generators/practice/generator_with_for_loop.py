def divisible(the_list):
  for x in the_list:
    if not x % 3:
      yield x


my_list = list(range(1, 30))

for x in divisible(my_list):
  print(x)
