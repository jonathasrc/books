def spam():
    global eggs
    eggs = 'spam' # essa é a variavel global

def bacon():
    eggs = 'bacon' # essa é a variavel local

def ham():
    print(eggs) # essa é a variavel global

eggs = 42 # essa e variavel global
spam()
print(eggs)
