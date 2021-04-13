
#1  -  str
x = str(int(float(5)))
#2   -  bool
x = 'aa' == 'AA'
#3   -  dict
x = {i: i**2 for i in range(5)}
#4  -  set
x = set(list((5, 6, 7)))
#5   -  список
a = {1: 1, 2: 4, 3: 9}
x = a.get(4)
#6   -   список
x = [].append('j')
#7  -  цикл
for i in range(10):
		if i < 5:
				x = 'hello'
		else:
				x = 5
#8   -    встроенная функция инпут
x = input('Enter and integer: ')
#9  -  int
a = 5
b = [1, 3, 5, ]
x = 'x'
a, b, x = x, a, b
#10   -   функция
def func(x, y=5):
		return x + y
x = func('Jaguar ', 'hunter')



