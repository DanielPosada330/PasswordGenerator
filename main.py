#This program generates a unique password for the user, and allows them the option
#to save it to a text file, or to generate a new password should they not like
#their originally generated password.
#This program will initially start with NO text file created.

#Importing the random module to use the choice method.
import random


#Simple function that reminds the user to enter yes or no should they enter anything besides
#those two responses.
def yesOrNo():
  print("\nPlease enter \'yes\' or \'no\'. ")


#This variable contains the random characters that the program will choose from
#for the password generator.
randomCharacter = (
  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*(),.?0123456789")

print("Hello! Welcome to your unique password generator program.")

#This will be the Main progam loop that the password generator is encompassed in.
#Depending on the user, the program will either reloop for another password,
#Or it will terminate with the password of the user's choice.
mainProgramLoop = False

while mainProgramLoop == False:
  answerChoice = False
  #This loop asks the user their desired password length, and to verify if it's correct.
  while answerChoice == False:
    #A try and except statement is used in case the user inputs a different value type.
    try:
      passwordLength = int(
        input("\nPlease input the desired length of your password: "))
      answerResponse = input((
        f"\nDo you want to print out a password with {passwordLength} characters?\nPlease enter  \'yes\' or \'no\': "
      )).lower()
      if answerResponse == "yes":
        answerChoice = True
      elif answerResponse == "no":
        continue
      else:
        yesOrNo()
    except ValueError as error:
      print("")
      print(error)
      yesOrNo()

  #The generatedPassword variable is where the randomly generated password will be stored.
  generatedPassword = ""
  #For every element or digit in the desired password length, a character will be chosen
  #and added to the generatedPassword variable until the desired length is reached.
  for pWord in range(passwordLength):
    generatedPassword += random.choice(randomCharacter)
  print("")
  print(generatedPassword)

  #This while loop asks the user if they would like to save
  #their password to a text file or not.
  answerChoiceTwo = False
  while answerChoiceTwo == False:
    #Another try and except statement is used in case the user inputs a different value type.
    try:
      questionResponse = input(
        "\nWould you like to save this password into a text file?\nPlease answer \'yes\' or  \'no\: '"
      ).lower()
      if questionResponse == "yes":
        passwordFile = open("password.txt", "w")
        passwordFile.write(generatedPassword)
        passwordFile.close()
        print("\nYour password has been saved to \'password.txt\'.")
        answerChoiceTwo = True
      elif questionResponse == "no":
        break
      else:
        yesOrNo()
    except ValueError as errorTwo:
      print("")
      print(errorTwo)
      yesOrNo()

  #Asking the user if they want a new password thus restarting the program.
  #Or if the user is satisfied with their generated password.
  print("\nWould you like to request a different password?")
  print("If so, you will repeat the process from the beginning.")
  print("If you are satisifed, then you may exit the program")

  #Another try and except statement is used in case the user inputs a different value type.
  #Final conditional statement asking if the user wants a new password or not.
  try:
    finalQuestion = input(
      "\nWith that in mind, would you like to request a different password?")
    if finalQuestion == "yes":
      continue
    elif finalQuestion == "no":
      print("\nThank you for using your unique password generator program!")
      print(
        "Remember not to share your password with others,\nor use the same password in multiple places!"
      )
      print("\nThank you, and have a good day!")
      #Sets the mainProgramLoop to True, thus exiting the main program while loop.
      mainProgramLoop = True
    else:
      yesOrNo()
  except ValueError as errorThree:
    print("")
    print(errorThree)
    yesOrNo()
