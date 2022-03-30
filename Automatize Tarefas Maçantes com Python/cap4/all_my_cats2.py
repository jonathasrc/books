
cat_names = []

while True:
    text = 'Enter the name of cat' + str(len(cat_names) + 1) + '(Or enter nothin to stop.):'
    print(text)

    name = input()

    if name == '':
        break

    cat_names = cat_names + [name] # concatenacao de lista

print('The cat names are: ')

for name in cat_names:
    print('' + name)
