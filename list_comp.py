names = ['Peter', 'John', 'Meriem', 'Samy', 'Liam', 'Nigel']
numbers=[1,2,3,4,5,6,7,8,9]




x = [person + ' dumped me' for person in names]
n=[number**2 for number in numbers]

movies_and_ratings={'Interstellar':9,'Dark Knight':8,'Fifty Shades':3,'Fifty Shades Darker':2,'Fifty Shades Darkest':1}

l=[]
for movie in movies_and_ratings:
    if movies_and_ratings[movie]>6:
        l.append(movie)
l=[movie for movie in movies_and_ratings if movies_and_ratings[movie]>6]
print(l)
print(x)
print(n)
