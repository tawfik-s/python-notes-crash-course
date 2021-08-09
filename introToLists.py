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






















