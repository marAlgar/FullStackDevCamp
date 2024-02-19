def full_name(first, last):
	return f'{first} {last}'


def greeting(name):
	def full_name(first, last):
		return f'{first} {last}'

	print(f'Hi {name}!')

greeting(full_name('Kristine', 'Hudgens'))
