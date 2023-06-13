phrase= str(input("Please type a phrase: "))

comprobacionA= False



for letter in phrase: 
    if 'a' in letter.lower() and comprobacionA == False:
        print('a')
        comprobacionA= True
