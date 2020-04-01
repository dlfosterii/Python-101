#This is a "mad-lib" style exercise asking a quesiton and filling in a sentence

#Telling the user what we're doing
print('Let\'s complete this sentence:')
print('___name___\'s favorite color is ___(color)____ and your favorite movie is ___(movie)___!')

#Creating the varibles I'll need
name = input('What is your name? ')
favorite_color = input('Tell me you favorite color: ')
favorite_movie = input('What is your favorite movie? ')

#outputing the sentence

print(f'{name}\'s favorite color is {favorite_color} and your favorite movie is {favorite_movie}!')