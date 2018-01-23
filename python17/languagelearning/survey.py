#测试类
class AnonymousSurvey():

	def __init__(self,question):
		self.question = question
		self.resposes = []

	def show_question(self):
		print(question)

	def store_response(self,new_response):
		self.resposes.append(new_response)

	def show_question(self):
		print("survey result: ")
		for respose in resposes:
			print('-' + respose)
						