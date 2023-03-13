# PasswordGenerator
The purpose of this program is to allow a user to generate a unique password of various lengths depending on the user's choice. 
The program then gives the user the option to save their generated password into a text file, or simply view it in the console.
## Motivation
I made this program as a way to start putting into practice the basics of Python that I had been learning during coursework.
This allowed me to get further experience utilizing conditional statements, try and except statements, debugging issues, while and for loops
just to name a few.
## Language
As stated previously, this code was written in Python to practice the syntax of Python
## Build Status
This was my first completed project that I was able to expand upon after looking for inspiration for a beginner project.
Although the program is simple, there are certain things I would like to expand upon in the future, most notably being able to add
additional passwords and save those to text files, but as well as assigning which "account" or "website" said generated passwords
would pair up with. Although the program works as intended, there is room for improvement and expansion. 
## Pseudocode Template
Below was the pseudocode template I used broadly to write the program:

	This program generates a unique password for the user, and allows them the option

	to save it to a text file, or to generate a new password should they not like

	their originally generated password.

	This program will initially start with NO text file created.

	Function yesOrNo():
  	 PRINT “please enter ‘yes’ or ‘no’.”

	Random Character variable that stores character options for password generator.

	PRINT Welcoming Statement

	Main Program Loop variable whether to stay in loop or exit and terminate program.
	Main Program While Loop
		First Question WHILE Loop
			Receive input of desired password length
			Receive input of confirmation of password length
			IF password length is correct
				Continue through program
			ELSE IF password length is not correct
				Repeat the First Question While Loop
			ELSE
				function yesOrNo()

		Generated password variable initially set to blank
		FOR every digit index IN range of desired password length
			Add the randomly chosen character to the variable holding the generated password
		PRINT the generated password variable
		
		Text file creation WHILE Loop
			Receive input if the user would like to save their generated password to a text file.
			IF response is ‘yes’
				Create text file
				Save generated password to text file
				Save text file
				PRINT Password saved to ‘password.txt’.
			ELSE IF response is no
				BREAK out of WHILE loop

			ELSE
				Function yesOrNo()

		PRINT New password statement yes or no.

		Receive input of if the user wants a new password or not.
		IF response is ‘yes’
			CONTINUE and begin the process anew
		ELSE IF response is ‘no’
			PRINT closing statement
			Changes Main Program Loop variable to exit the loop and program
		ELSE:
			Function yesOrNo()
		
## Test Scenarios
Below are some example scenarios that could come about during the program:

Scenario 1: User chooses a password length of “16” and decides to create a text file to store the password where they can reference the password later in a text editor.
1.	The program begins by greeting the user to their unique password generator program.
2.	The program then asks the user for their desired length of the password, with the user choosing a length of 16 characters.
3.	The program reads the user’s choice back to them and confirms it is correct.
4.	The program randomly generates a 16-character password.
5.	The user is then asked if they would like to save the password to a text file. The user chooses to do so.
6.	A text file is created where their randomly generated password is viewable.
7.	The program asks the user if they are satisfied with the password or would like to choose a new one. The user decides to stick with the previously generated password.
8.	The program reminds the user of safe password usage, and successfully terminates

Scenario 2: User chooses a password length of “12” but doesn’t want a text file.
1.	The program begins by greeting the user to their unique password generator program.
2.	The program then asks the user for their desired length of the password, with the user choosing a length of 12 characters.
3.	The program reads the user’s choice back to them and confirms it is correct.
4.	The program randomly generates a 12-character password.
5.	The user is then asked if they would like to save the password to a text file. The user chooses not to do so.
6.	The program does NOT create the text file.
7.	The program asks the user if they are satisfied with the password or would like to choose a new one. The user decides to stick with the previously generated password.
8.	The program reminds the user of safe password usage, and successfully terminates.

Scenario 3: User chooses a password length of “20”, wants a text file, but doesn’t like their password and opts for a new one.
1.	The program begins by greeting the user to their unique password generator program.
2.	The program then asks the user for their desired length of the password, with the user choosing a length of 20 characters.
3.	The program reads the user’s choice back to them and confirms it is correct.
4.	The program randomly generates a 20-character password.
5.	The user is then asked if they would like to save the password to a text file. The user chooses to do so.
6.	A text file is created where their randomly generated password is viewable.
7.	The program asks the user if they are satisfied with the password or would like to choose a new one.
8.	The user decides for whatever reason that they are not satisfied with their given password and opts to make a new one.
9.	The program loops back to beginning and repeats steps 1-6, this time with a new password, and the new text file replacing the old one.
10.	The user decides to use the second password generated.
11.	The program reminds the user of safe password usage, and successfully terminates.

## Debugging Issues
The main issue that I ran into constantly was when asking for input. If the user entered anything but my desired inputs of ‘yes’ or ‘no’ I would run into a ValueError as shown below:

Code used:
![image](https://user-images.githubusercontent.com/104124602/214954619-a818b9b3-b736-4051-8f40-f934e492f35a.png)

Error received:

![image](https://user-images.githubusercontent.com/104124602/214954753-67adc24e-9a01-4f49-818f-eeae8064987b.png)

To combat this, I utilized a try and except statement to catch the error. I didn’t want to simply have it print out something to the user, but I also wanted to print out which error it was and why it failed. For that I coded the try and except statement as follows:
![image](https://user-images.githubusercontent.com/104124602/214954811-ee63c4e9-31a3-4da8-9cfa-734bb26a6c75.png)

That way if the user did repeat that error, the console would print out what caused the error, and a prompt to the user asking them to enter ‘yes’ or ‘no’:

![image](https://user-images.githubusercontent.com/104124602/214954931-320b4719-2362-4eab-85d9-739e1cdb878c.png)

Another error that I came around was one that was user error, but an understandable mistake. When asking for the use to type in ‘yes’ or ‘no’, if the user typed in “Yes” or “NO” or some combination of upper and lower case characters, I would receive an error. Below was the original code:
![image](https://user-images.githubusercontent.com/104124602/214954983-bdb0a9eb-eb9f-490a-816e-e163e5303775.png)

And below was the console’s output:

![image](https://user-images.githubusercontent.com/104124602/214955031-86edf99b-c437-4d7d-9fc7-11b585d365ea.png)

So what I did to combat this was to add a .lower() method to the user’s input, in which case when my conditional statements were set to either == ‘yes’ or == ‘no’ the user’s input would automatically be made into all lowercase, thus matching what I programmed into the conditional statements.

Below is the new code:
![image](https://user-images.githubusercontent.com/104124602/214955120-7890af05-d389-4372-a225-3f6bb23ebca4.png)

Along with the desired console output:
![image](https://user-images.githubusercontent.com/104124602/214955161-c3f6d9ad-9ef6-4160-9a5e-bde99ff285f7.png)
