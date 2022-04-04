secret_number = 777
print("+================================+","| Welcome to my game, muggle!    |","| Enter an integer number        |","| and guess what number I've     |","| picked for you.                |","| So, what is the secret number? |","+================================+",sep='\n')
guess=int(input('enter a guess'))
while(guess!=secret_number):
  print("Ha ha! You're stuck in my loop!")
  print("+================================+","| Welcome to my game, muggle!    |","| Enter an integer number        |","| and guess what number I've     |","| picked for you.                |","| So, what is the secret number? |","+================================+",sep='\n')
  guess=int(input('enter a guess'))
print("Well done, muggle! You are free now.")