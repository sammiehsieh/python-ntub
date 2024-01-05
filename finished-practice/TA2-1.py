con = input()

num_st = con.split(" ")[0]
num_nd = con.split(" ")[1]

i = 1

while i <= int(num_st):
    # print(i)
    k = 1
    while k <= int(num_nd):
        print(str(i) + "x" + str(k) + "=" + str(i * k))
        k += 1
    i += 1
