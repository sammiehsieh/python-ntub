# 經過老師講解才算出來

total = 200

user_mind = input()

now_channel = user_mind.split(' ')[0]

goal_channel = user_mind.split(' ')[1]

click = (total - int(now_channel) + int(goal_channel)) % total

print(click)