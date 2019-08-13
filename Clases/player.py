class Player:
    vocation = "No vocation"
    spell = "puff"
    movement_speed = "50"

    def __init__(self,**kwargs):
        self.name = input("Elije tu nombre: ")
        self.hit_points = kwargs.get("hit_poitns", 50)
        self.mana = kwargs.get("mana", 50)
    
    def __str__(self):
        return "Bienvenido, {} El {} tiene {} hit point y {} mana, puede lanzar {} y corre a {}".format(self.name,self.vocation,self.hit_points,self.mana,self.spell,self.movement_speed)

    def cast_spell(self):
        return self.spell

class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Utevo Lux"
    movement_speed = "20"

    def cast_spell(self):
        return "{} y Exura".format(self.spell)

class Knight(Player):
    vocation = "Knight"
    spell = "Exoir"
    movement_speed = "60"
    
    def cast_spell(self):
        return "{} y Exura".format(self.spell)

class Druid(Player):
    vocation = "Druid"
    spell = "Song Of God"
    movement_speed = "80"

class Paladin(Player):
    vocation = "Paladin"
    spell = "Ligth Storm"
    movement_speed = "60"