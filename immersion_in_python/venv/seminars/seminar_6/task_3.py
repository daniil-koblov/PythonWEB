from sys import argv
from task_2 import guess_number

num_list = list(map(int, argv[1:4]))

low_limit, high_limit, tries = 1, 100, 10

if len(num_list) == 1:
    high_limit = num_list[0]
elif len(num_list) == 2:
    low_limit, high_limit = num_list
else:
    low_limit, high_limit, tries = num_list

print(guess_number(low_limit, high_limit, tries))