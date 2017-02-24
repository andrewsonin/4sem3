from random import randint

my_list = [[randint(0, 10) for i in range(1000)] for j in range(1000)]
output = open('output.txt', 'w', encoding='utf8')
for element in my_list:
    output.write(' '.join(map(str, element)) + '\n')
