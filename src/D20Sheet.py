from Caracteristic import Caracteristic
from Domain import Domain

class D20Sheet:
	def __init__(self, number_list):
		if number_list == None:
			self.number_list = [1, 0, 0, 0, 0, 0, 0, 1]
		else:
			self.number_list = number_list
		self.level = Caracteristic("Niveau", self.number_list[0])
		self.strength = Caracteristic("Force", self.number_list[1])
		self.dexterity = Caracteristic("Dexterité", self.number_list[2])
		self.constitution = Domain("Constitution", self.strength, self.dexterity)
		self.intelligence = Caracteristic("Intelligence", self.number_list[3])
		self.wisdom = Caracteristic("Sagesse", self.number_list[4])
		self.spirit = Domain("Esprit", self.intelligence, self.wisdom)
		self.charisma = Caracteristic("Charisme", self.number_list[5])
		self.perspicacity = Caracteristic("Perspicacité", self.number_list[6])
		self.social = Domain("Social", self.charisma, self.perspicacity)
		self.fate = Caracteristic("Destin", self.number_list[7])
		points = (29 + self.level.getValue()) - (self.physical.getValue() + self.spirit.getValue() + self.social.getValue() + self.vision.getValue() + self.fate.getValue() - 1)
		self.points = Caracteristic("Points Restants", points)

