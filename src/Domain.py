class Domain():
	def __init__(self, name, caracteristic_one, caracteristic_two):
		caracteristic_one.subscribe(self)
		caracteristic_two.subscribe(self)
		self.caracteristics = [caracteristic_one, caracteristic_two]
		self.name = name
		self.__value = self.__sumValues()

	def __sumValues(self):
		return sum([x.getValue() for x in self.caracteristics])

	def getValue(self):
		return self.__value

	def update(self, value):
		self.__value = self.__sumValues()

	def __repr__(self):
		retval = f"{self.name} : {self.__value}\n\t{str(self.caracteristics[0])}\t{str(self.caracteristics[1])}"
		return retval

