from random import randint
class Hero():
    def __init__(self, name, health, armor, power):
        self.name=name
        self.health=health
        self.armor=armor
        self.power=power
    #Выбор пути
    def print_info(self):
        print(f'Приветствуем тебя, славный рыцарь {self.name}')
        wish=input('Ты стоишь у входа в лес, полный смертельных опасностей. Готов ли ты войти внутрь и сразиться с врагами (да/нет)?').lower()
        if wish=='да':
            return True
        else:
            return False
    #Атака НА ЗЛОДЕЯ
    def strike_good(self, character):
        print(f'{self.name} бесстрашно набрасывается на {character.name}')
        character.armor-=self.power
        if character.armor<=0:
            character.health+=character.armor
            character.armor=0
            if character.health<=0 or self.health<=0:
                if character.health<=0:
                    character.health=0
                else:
                    self.health=0
                knight.state_good()
                character.state_bad()
                return False
            else:
                return True
        else:
            return True
    #Состояние РЫЦАРЯ
    def state_good(self):
        print(f'Результат боя для {knight.name}:')
        print('Здоровье:', knight.health)
        print('Броня:', knight.armor)
        
#Ссылка на "выбор пути"
class Warrior(Hero):
    def hero(self):
        print_info()

#Класс ЗЛОДЕЕВ
class Villian(Hero):
    def __init__(self, name, health, armor, power, new):
        super().__init__(name, health, armor, power)
        self.new=new
    #Вывод на экран имени соперника
    def hello(self):
        if knight.health==0:
            return False
        else:
            if self.new==True:
                if villian==drogon or villian==vizer:
                    print(f'-> НОВЫЙ ГЕРОЙ! С неба спускается свирепый дракон {self.name}')
                    self.new=False
                else:
                    print(f'НОВЫЙ ГЕРОЙ! Из глубины леса появляется искусный воин {self.name}')
                    self.new=False
            else:
                if villian==drogon or villian==vizer:
                    print(f'И вновь перед нами разъярённый дракон {self.name}')
                else:
                    print(f'Снова появляется воинственный {self.name}')
        return True
    #Вывод на экран характеристик противника
    def info_villian(self):
        print(f'Уровень здоровья: {villian.health}')
        print(f'Класс брони: {villian.armor}')
        print(f'Атака: {villian.power}')
        fight=input('Вступить в бой? (да/нет)').lower()
        if fight=='да':
            condition1=True
            condition2=True
            a=randint(0,1)
            if a==0:
                while condition1==True and condition2==True:
                    condition1=knight.strike_good(villian)
                    if condition1==False:
                        break
                    condition2=villian.strike_bad(knight)
            else:
                while condition1==True and condition2==True:
                    condition1=villian.strike_bad(knight)
                    if condition1==False:
                        break
                    condition2=knight.strike_good(villian)
    #Атака ЗЛОДЕЯ
    def strike_bad(self, character):
        print(f'{self.name} бесстрашно набрасывается на {character.name}')
        character.armor-=self.power
        if character.armor<=0:
            character.health+=character.armor
            character.armor=0
            if character.health<=0 or self.health<=0:
                if character.health<=0:
                    character.health=0
                else:
                    self.health=0
                knight.state_good()
                villian.state_bad()
                return False
            else:
                return True
        else:
            return True
    #Состояние ЗЛОДЕЯ
    def state_bad(self):
        print(f'Результат боя для {villian.name}:')
        print('Здоровье:', villian.health)
        print('Броня:', villian.armor)


play=True
knight=Hero('Ричард', 50, 25, 30)
wish=knight.print_info()
drogon=Villian('Дрогон', 5, 25, 60, True)
piter=Villian('Питер', 15, 0, 10, True)
serg=Villian('Сержио', 10, 5, 10, True)
vizer=Villian('Визерион', 5, 25, 50, True)
enemies=[drogon, piter, serg, vizer]
if wish==True:
    print('***Да начнётся битва!***')
    while play==True:
        num=randint(0,len(enemies)-1)
        villian=enemies[num]
        play=villian.hello()
        if play==False:
            print('Храбрый рыцарь Ричард погиб в бою с врагами\nТут и сказочке конец!')
            break
        villian.info_villian()
        if villian.health==0:
            enemies.remove(villian)
            if len(enemies)==0:
                print('УРА!!! ПОБЕДА!!! ПОЗДРАВЛЯЕМ!!!')
                break
else:
    print('---\nТут и сказочке конец!')
    play=False