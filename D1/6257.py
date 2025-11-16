fruit = ['   apple    ', 'banana', '  melon']
new_fruit = {fruit[i].strip(): len(fruit[i].strip()) for i in range(0, len(fruit))}
print(new_fruit)
