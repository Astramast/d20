class Domain():
	def __init__(self, name, caracteristic_list):
		self.caracteristics = caracteristic_list
		self.name = name

	def getValue(self):
		return sum([c.getValue() for c in self.caracteristics])//len(self.caracteristics)

	def __repr__(self):
		retval = f"{self.name} : {self.__value}\n\t{str(self.caracteristics[0])}\t{str(self.caracteristics[1])}"
		return retval

