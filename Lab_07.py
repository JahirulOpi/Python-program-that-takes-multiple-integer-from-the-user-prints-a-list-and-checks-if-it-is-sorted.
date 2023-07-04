import random

def is_sorted(a):
    for i in range(0,len(a)):
        if a[i] < a[i-1]:
            return False
    return True
    
a = []
k = random.randint(1,10)
print("Enter",k,"values:")
for i in range(k):
    x = int(input("Enter value "+str(i+1)+":"))
    a.append(x)
print("Original list: ",a)
is_sorted(a)
if a[i] < a[i-1]:
    print("the list is not sorted")
else:
    print("the list is sorted")
