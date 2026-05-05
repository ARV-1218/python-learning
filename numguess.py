import random
def getNum(chosenN):
    isCorrect = False
    for i in range(1,11):
            if(isCorrect == False):
                guessNum = int(input(f"Try number:{i}) Enter a number:"))
                isCorrect = checkNum(guessNum,chosenN)
                if(i == 10):
                     print("You have ran out of tries")            
                     print(f"The correct answer was {chosenN}")
 
            
def checkNum(num,chosenN):
    
    if(num == chosenN):
        print("Its correct.")
        return True
    elif(num > chosenN):
        print("It should be lower")  
        return False  
    elif(num < chosenN):
        print("It should be higher")    
        return False
  

def main():
      chosenN = random.randint(1,100)
      print("You have 10 tries to guess the chosen number betwn 1-100.")
      getNum(chosenN)
      
main()