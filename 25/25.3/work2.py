class Ship:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return f'Модель корабля: {self.__model}'

    def sail(self):
        print('Корабль куда-то поплыл')

class Military(Ship):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def attack(self):
        print(f'Корабль атакует с помощью {self.weapon}')

class Cargo(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.cargo_load = 0

    def load(self):
        print('Загружаем корабль')
        self.cargo_load += 1
        print(f'Текущая загруженность: {self.cargo_load}')

    def un_load(self):
        if self.cargo_load > 0:
            print('Разгружаем корабль')
            self.cargo_load -= 1
        else:
            print('Корабль пустой, нечего разгружать')
        print(f'Текущая загруженность: {self.cargo_load}')

    def move(self, unload_point):
        self.unload_point = unload_point
        print(f'Корабль плывет к месту разгрузки в {unload_point}')




avrora = Military('Аврора', 'MachineGun')
print(avrora)
avrora.attack()
kruser = Cargo('Крузенштерн')
print(kruser)
kruser.load()
kruser.un_load()
kruser.move('Пятигорск')
kruser.un_load()


