# Type conversion
# int(), float() and complex()
# Implicit conversion - done by python(automatic)
# Explicit conversion - done by the programmer using the functions
# print(10/3)
# print(int(10/3))
# print(complex(10/2))
# print(10/2)
# print(5.5/2.5)

# import random

# print(random.randrange(1,20))

# n = 23e123
# print(n)
# print(type(n))
# print(9 / 3)
# print(9 // 3)
# # print(2 / 0)
# print(2 ** 5)
# print(2*2*2*2*2)


# # print(2**2)
# print((2*2)**2) # operator precedence
# print(4**2)
# # print(4*4)
# print((74+6)/3//2*5)
# print(9%2)
# print(9%5)

# print(round(5.5))
# print(pow(2, 5))
# print(pow(2, 6, 10))
# print(2**6)
# print(64%10)





# Object referencing

a = 10
c = a
print(id(a))
b = 20
print(id(b))
print(a == b)


cars = ['4matic', 'Rolls Royce', 'Maybach', 'rolls royce', 'Bentley' ]
cars[0]='Bentley'
print(cars)
print('formatic' not in cars)

greet = 'Hellooo'
print(len(greet))
poem = '''
Lorem ipsum dolor sit amet,
 consectetur adipisicing elit. 
 Est ipsum dignissimos vel 
 exercitationem fugiat facilis
   totam minus debitis, quos 
   tenetur quis alias eius 
   quaerat harum esse iure sed. 
   Numquam, ab.
'''
print(poem)

print('I\'m a \\lady')

y = 'hjgbhjugfvnugfdf bgdjkgiofdioiodsioiofifiofio\
,mvgkjjkgvkjjgfvinjfgvnjfgnnj'
print('hello\nworld')
print("Hello\tWorld")
