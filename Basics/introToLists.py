bicycles=['trek','cannodale','redline','speciaized']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[0].title())
print(f"to returer the last item in the lest we use -1 {bicycles[-1]}")

#values with - return the value but frome left -1 is the last item
#-2 is the value before the last item

#modifying elements in a list

bicycles[0]='coco'
print(bicycles)


#adding knew  data we use append

bicycles.append('ducati')

print(bicycles)

#insert elements we use insert(0,'what we will insert')

motorcycles=['honda','yamaha','suzuki']

motorcycles.insert(0,'ducati')
print(motorcycles)

#removing elements
print("*******************************removing from lists**************************************\n\n")


#remove element using del statement

moto=['honda','yamaha','suzuki']
print(moto)
del moto[0]
print(moto)

moto.pop()   #pop return value is the indew wich is poped
print(moto)
moto.pop(0)
print(moto)
#we can also pop from any position pop(1)

#you can use remove () to remove using value

print("*******************************Organizing a list**************************************\n\n")

cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#sort change the list state you can use sorted() its return the array 
#sorted without affecting the original array
#sorted function also use reverse order


cars.reverse()
len(cars)


#for loop in python


magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, we are lookin for you next trick")
    

#range()  function can be used to pirnt random numbers in a range
for value in range(1,5):
    print(value)

numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2)) #third variable is the increased value default type=1
print(even_numbers)  

#you can get min,max,sum using this simple functions
min(even_numbers)
max(even_numbers)
sum(even_numbers)

squares=[value**2 for value in range(1,11)]
print(squares)



list=[value for value in range(1,12)]

print(list)


players=list[0:3]

print(players)


players2=list[:2]
players3=list[3:0]

players4 = ['charles', 'martina', 'michael', 'florence', 'eli']



for player in players4[:3]:
    print(player.title())


copy=players4[:]  #copying the existing  list

#if we do copy=players4   the two names will point to the same array in the memory



#tuple use parentheses instead o fsquare brackets 
#you can't change the tuble elements value

dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])


