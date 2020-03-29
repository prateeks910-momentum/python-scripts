print('This is a sample string {} - {}'.format('INSERT', 'UPDATE'))

greet = "Hello"

name = "Prateek"

greeting = '{} {}'.format(greet, name)

print(greeting)

revGreet = '{1} says {0}'.format(greet, name)

print(revGreet)

indexedGreet = '{b} says {a}'.format(a=greet, b=name)

print(indexedGreet)