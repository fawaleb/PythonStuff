digits=[0,1,2,3,4,5,6,7,8,9]

# print(digits[-1])
#
# for number in digits:
#     print(number)

# print()
# print(digits[-len(digits)])
# print()
# # Slicing Example
# print(digits[:3])
#
# # Striding Example
# print(digits[0:10:3])
# print(digits[::-1])
#
# for i in range(len(digits)):
#     print(digits[0:i])

window_size=5
for i in range(len(digits)-4):
    print(digits[i:i+window_size])

problems='broke, pale, short, nerdy'
print(problems)
l = problems.split(', ')
print(l)

joined=' and '.join(l)
print(joined)


csv=','.join(l)
print(csv)