class Publisher:
	def __init__(self):
		self.__subscribers = []

	def addSubscriber(self, subscriber):
		self.__subscribers.append(subscriber)

	def notifySubscribers(self):
		for subscriber in self.__subscribers:
			subscriber.update()
