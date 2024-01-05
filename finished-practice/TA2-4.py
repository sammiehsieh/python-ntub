# multi_lines = '''Hello
# World
# This
# is
# a
# question'''

# round_num = multi_lines.splitlines()

# i = 0
# for voc in round_num:
#     print(voc + str(i + 1))
#     i += 1



# DOMjudge pass
import sys

in_txt = sys.stdin.read()

for i, txt in enumerate(in_txt.splitlines(), start=1):
    print(f"{txt}{i}\r\n")