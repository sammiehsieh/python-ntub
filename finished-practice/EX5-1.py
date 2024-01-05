pwd = list(input())

pwd_word = []

output = []

for i in pwd:
    if i in output:
        output.remove(i)
    output.append(i)

print(''.join(output))