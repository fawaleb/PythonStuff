list1 = [1, 2, 3, 4, 5, 6]
list2 = ['one', 'two', 'three', 'four', 'five', 'six']

zipped = list(zip(list1, list2))
print(zipped)
print(zipped[0])

items=['Apple','Banana','Orange']
counts=[3,6,4]
prices=[0.99,0.78,.25]

sentences=[]

for (item,count,price) in zip(items,counts,prices):
    sentence=f'I bought {count} {item}s at {price} cents each'
    sentences.append((sentence))

print(sentences)
