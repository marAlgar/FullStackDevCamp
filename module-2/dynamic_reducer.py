import operator
from functools import reduce

"""
dynamic_reducer([1, 2, 3], '+')
dynamic_reducer([1, 2, 3], '-')
dynamic_reducer([1, 2, 3], '*')
dynamic_reducer([1, 2, 3], '/')
"""

def dynamic_reducer(collection, op):
	operators = {
		'+': operator.add,
		'-': operator.sub,
		'*': operator.mul,
		'/': operator.truediv
	}							 # dictionary of operators

	return reduce((lambda total, element: operators[op](total, element)), collection)

"""
estamos llamando directamente a la función desde lambda, porque operators[operation] contiene
'operator.add' (por ejemplo), entonces, nosotros al hacer 'operators[operation](total, element)'
es lo mismo que hacer 'operator.add(total, element)'
"""

print(dynamic_reducer([1, 2, 3], '+'))  # 6
print(dynamic_reducer([1, 2, 3], '-'))  # -4
print(dynamic_reducer([1, 2, 3], '*'))	# 6
print(dynamic_reducer([1, 2, 3], '/'))	# 0.16666666666666666
