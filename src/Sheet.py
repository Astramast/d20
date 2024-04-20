class Sheet():
	def __init__(self, caracteristic_list):
		self.caracteristics = caracteristic_list

	def getItems(self):
		return self.caracteristics

	def addCaracteristic(self, caracteristic):
		self.caracteristics.append(caracteristic)

	def __repr__(self):
		retval = "Sheet : \n"
		for caracteristic in self.caracteristics:
			retval += "\t" + str(caracteristic).replace("\t", "\t\t")
		return retval
