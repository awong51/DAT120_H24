import random
true = 0
false = 0
attempts  = 8888
for i in range(attempts):
    year = random.randint(0,10000)
    if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
        true += 1
    else:
        false += 1

print(f'{true} skuddår ({true/attempts*100:.3f}%)')
print(f'{false} ikke skuddår ({false/attempts*100:.3f}%)')