print("1: Basic - 0 - 150")
for x in range(0,151):
    print(x)

print("\n2: Multiples of 5")
for x in range(5,1001,5):
    print(x)

print("\n3: Counting, the Dojo Way")
for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)
 
print("\n4: Whoa. That Sucker's Huge")
sum = 0
for x in range(0, 500001):
    if x % 2 != 0:
        sum += x
print(sum)

print("\n5: Countdown by Fours")
for x in range(2018, -1, -4):
    print(x)


print("\n6: Flexible Counter")
lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum, highNum + 1):
    if x % mult == 0:
        print(x)
