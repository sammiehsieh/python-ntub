# f = open('./file.txt', 'r')

# content = f.read()

# print(content)

# f.close()



# f = open('write.txt', 'w', encoding='utf-8')

# f.write('Write file!')

# f.close()



with open('file.txt', 'r', encoding='utf-8') as f:
    print(f.read())