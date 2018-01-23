#简单的函数
def greet_user():
	print("hello!")

greet_user()

#向函数传递信息
def greet_user(username):
	print("hello " + username.title() + "!")

greet_user('jesse')
greet_user('sarah')

#实参和形参
#传递实参
def describe_pet(animal_type, pet_name):
	print("\ni have a " + animal_type + ". ")
	print("my" + animal_type + "'name is " + pet_name.title() + ".")

describe_pet('hamster','harry')

#关键字实参
describe_pet(animal_type = 'hamster', pet_name = 'harry')

#默认值
def describe_pet(pet_name,animal_type='dog'):
	print("\ni have a " + animal_type + ". ")
	print("my " + animal_type + "'s name is " + pet_name.title() + ". ")

describe_pet('willie')

#等效的函数调用
def describe_pet(pet_name,animal_type = 'type'):
	print(pet_name,animal_type)

describe_pet(animal_type = 'dog',pet_name = "willie")

#返回值
#返回简单值
def get_formatted_name(first_name,last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

#返回字典
def build_person(first_name,last_name): 
	person = {'first': first_name,'last':last_name}
	return person
musician = build_person('jimi','hendrix')
print(musician)

def build_person(first_name,last_name,age=''):
	person = {'first':first_name,'last': last_name}
	if age:
		person['age'] = age
	return person
musician = build_person('jimi','hendrix',age = 27)
print(musician)			

#结合使用函数和while
def get_formatted_name(first_name,last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print("\nplease tell me your name:")
	f_name = input("first name: ")
	if f_name == 'q':
		break	
	l_name = input("last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name,l_name)
	print("\nhello, " + formatted_name + "!")	

