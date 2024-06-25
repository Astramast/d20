class Caracteristic():
	def __init__(self, name, value):
		self.name = name
		self.__value = value

	def __repr__(self):
		return f"{self.name} : {self.__value}\n"

