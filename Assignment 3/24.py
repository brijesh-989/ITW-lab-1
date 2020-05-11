import random
lottery =[]
for i in range(100):
    lottery.append(random.randrange(1000000000,9999999999))
winners=random.sample(lottery,2)
print(f"winners are : {winners}")    