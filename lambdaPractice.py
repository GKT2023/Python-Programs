## add three nums:
x = 1
y = 2
z = 3
add = lambda x,z,y: x+z+y
print(add(x,z,y))


## square of a num
a = 4
sq = lambda a : a ** 2
print(sq(a))

## concat
s1 = "Garima"
s2 = " & Thalesh"

conc = lambda s1,s2 : s1 + s2
print(conc(s1,s2))

# even and odd
evenOdd = lambda x : "even" if x % 2 == 0 else "odd"
print(evenOdd(4))
print(evenOdd(5))

## max num

largest = lambda x,y : x if x > y else y
print(largest(6,9))

## add for custom input

add = lambda : int(input("enter first number: ")) + int(input("enter second number: "))
print(add())

## list comprehension

sq = lambda x: [i* 100  for i in x]
print(sq([1,2,3]))