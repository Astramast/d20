class Caracteristic():
	def __init__(self, name, value):
		self.name = name
		self.__value = value
		self.observers = []

	def subscribe(self, observer):
		self.observers.append(observer)

	def setValue(self, value):
		self.__value = value
		for observer in self.observers:
			observer.update()

	def getValue(self):
		return self.__value

	def __repr__(self):
		return f"{self.name} : {self.__value}\n"

