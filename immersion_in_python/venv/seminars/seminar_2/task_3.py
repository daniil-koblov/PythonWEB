

BIN = 2
OCT = 8

number = 46
print(bin(number))
string = '0b'
while number != 0:
    string += str(number % BIN)
    number //= BIN

print(string)
