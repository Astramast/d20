from Caracteristic import Caracteristic
from Domain import Domain
from Sheet import Sheet

class D20Sheet(Sheet):
	def __init__(self, number_list):
		if number_list == None:
			self.number_list = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
		else:
			self.number_list = number_list
		self.level = Caracteristic("Niveau", self.number_list[0])
		self.strength = Caracteristic("Force", self.number_list[1])
		self.dexterity = Caracteristic("Dexterité", self.number_list[2])
		self.physical = Domain("Physique", self.strength, self.dexterity)
		self.intelligence = Caracteristic("Intelligence", self.number_list[3])
		self.wisdom = Caracteristic("Sagesse", self.number_list[4])
		self.spirit = Domain("Esprit", self.intelligence, self.wisdom)
		self.charisma = Caracteristic("Charisme", self.number_list[5])
		self.perspicacity = Caracteristic("Perspicacité", self.number_list[6])
		self.social = Domain("Social", self.charisma, self.perspicacity)
		self.discretion = Caracteristic("Discretion", self.number_list[7])
		self.perception = Caracteristic("Perception", self.number_list[8])
		self.vision = Domain("Vision", self.discretion, self.perception)
		self.fate = Caracteristic("Destin", self.number_list[9])
		points = (29 + self.level.getValue()) - (self.physical.getValue() + self.spirit.getValue() + self.social.getValue() + self.vision.getValue() + self.fate.getValue() - 1)
		self.points = Caracteristic("Points Restants", points)
		super().__init__([self.level, self.physical, self.spirit, self.social, self.vision, self.fate, self.points])

