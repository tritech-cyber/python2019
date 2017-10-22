class Animal(object):
	def __init__(self,name):
		self.name = name

	def desc(self):
		print(self.name)
    
    
txt = Animal("dog")
txt.desc()
