sample=lambda x:x+x

c=sample(10)

print(c)

def sample(a):
    a+=a
    return a

c=sample(5)
print(c)

def sample_1():
    a=10
    print(a)
    return