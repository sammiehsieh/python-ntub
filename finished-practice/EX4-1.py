sentence = input()

s_list = sentence.split(' ')

res = []

i = 0

while i < len(s_list):
    res.append(''.join(list(s_list[i])[::-1]))
    i += 1

print(' '.join(res))