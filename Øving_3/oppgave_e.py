from math import log
def logaritme(x,base=10):
    print(base)
    answer = x*log(x,base)
    return answer

print(logaritme(5) + logaritme(3))