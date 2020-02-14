class car:
    def __init__(self, name='Ferari', color='', speed=33):
        self.speed = speed
        self.color = color
        self.name = name

    def changeColor(self, color):
        self.color = color
        return f'color changed to {color}'
    
    def changeSpeed(self, speed):
        self.speed = speed
        return f'speed changed to {speed}'
    
    def changeName(self, name):
        self.name = name
        return f'name changed to {name}'
    
    def increaseSpeed(self, speed=1):
        self.speed = self.speed + speed
        return self.speed
    

# ferari = car()

# print(ferari.name)
# print(ferari.speed)
# print(ferari.color)

# ferari.changeColor('blue')
# print(' ')
# print(ferari.name)
# print(ferari.speed)
# print(ferari.color)

# ferari.changeName('BG')
# print(' ')
# print(ferari.name)
# print(ferari.speed)
# print(ferari.color)

# ferari.increaseSpeed()
# print(' ')
# print(ferari.name)
# print(ferari.speed)
# print(ferari.color)

# newCar = car(name='peugeot', speed=100, color='Red')

# print(' ')
# print(newCar.name)
# print(newCar.speed)
# print(newCar.color)