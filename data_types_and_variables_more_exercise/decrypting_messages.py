decrypting_key = int(input())
number_of_lines = int(input())
decrypting_massage = ''

for _ in range(number_of_lines):
    line = input()
    decrypting_massage += chr(ord(line) + decrypting_key)

print(decrypting_massage)
