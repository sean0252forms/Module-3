def findHeight():
  blocks = int(input("Enter the number of blocks: "))
  height = 0
  while blocks>=height:
      height+=1
      blocks-=height
      print('Height Number: ',height)
  print(height)