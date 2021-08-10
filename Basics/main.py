cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car=='bmw' and cars[1]==car:
        print(car.upper())
    elif car=='bmw':
        print(car.title())
    else:
        print(car.title())
        break
    

#we use and , or 


#to check if a value in a list
print('audi' in cars)
print('audi' not in cars)



alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


del alien_0['points']


point_value=alien_0.get('xpos','no point value assigned.')


user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#a list of Dictionaries


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

















