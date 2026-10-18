class GameCharacter:
    _health=100
    _mana=50
    _level=1
    
    def __init__(self,name):
        self._name=name
        self._health=GameCharacter._health
        self._mana=GameCharacter._mana
        self._level=GameCharacter._level
    def level_up(self):
        self.health=100
        self.mana=50
        self._level+=1
        
        
        print(f"{self.name} leveled up to {self.level}!")
    def __str__(self):
        return (f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}")
    @property
    def name(self):
        return self._name
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self,new_health):
        if not isinstance(self._health,(int,float)):
            raise TypeError("Health should be int or float")
        if new_health <=0 :
            self._health=0
        elif 0<=new_health<=100:
            self._health=new_health


    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self,new_mana):
        if new_mana<=0:
            self._mana=0
        if new_mana>=50:
            self._mana=50
        if 0<=new_mana<=50:
            self._mana=new_mana
    @property
    def level(self):
        return self._level
    # @level.setter
    # def level(self):
    #     pass

hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up
