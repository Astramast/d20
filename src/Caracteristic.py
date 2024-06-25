from Publisher import Publisher

class Caracteristic(Publisher):
	def __init__(self, name, value):
		self.name = name
		self.__value = value

	def setValue(self, value):
		if value < 0 or value > 20:
			raise ValueError
		self.__value = value
		self.notifySubscribers()

	def getValue(self):
		return self.__value

	def __repr__(self):
		return f"{self.name} : {self.__value}\n"

