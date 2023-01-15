class Family:
    family_name = 'Common family'
    family_founds = 1000000
    having_house = False

    def family_info(self):
        print(f'Название семьи: {self.family_name}\n'
              f'Сбережения семьи: {self.family_founds}\n'
              f'Наличие дома: {self.having_house}'
              )


my_family = Family()
my_family.family_info()
