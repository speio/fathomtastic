#The game of the Rat
print "     The \n Game of the \n     Rat"
raw_input("Press enter to continue")
print "Choose your character:"
raw_input()

#Drawing character choices
print "Elfred Ratskill"


print "	 	   	          _..----.._      _"
print "	      			.\'  .--.    \"-.(0)_"
print "                  '-.__.-''''=:|   ,  _)_ \__  . c\\'-.."
print "	     			 '''------'---''---'-\""



raw_input("...")
print "Sir. Ratsalot"

print "	             (\,/)"
print "                     oo   '''//,        _"
print "                   ,/_;~,        \,    / '"
print "                    \"'  \    (    \    !"
print "                         ',|  \    |__.'"
print "                         '~  '~----''"


raw_input("...")

print "Ratzo"

print "                .---."
print "           (\./)     \.......- "
print "           >' '<  (__.'\"\"\"\" "
print "          \" ` \" \""

#taking character input
#and checking to see if character was typed correctly
character =""
while len(character) == 0:
	character = raw_input("Which character do you choose? \n > " )	

	if character in ["Sir. Ratsalot" , "Ratzo" , "Elfred Ratskill"]:
		print "Good choice %s is a great rat" % character
		break	
	elif character not in ["Sir. Ratsalot" , "Ratzo" , "Elfred Ratskill"]:
		character = ""
		print "You probably mistyped something, let's try entering the rat's name again"

print "Let's begin our adventure!"
raw_input("...")
print "You awake in a small ratbed with a candle precariously burning beside the bed."
print "The rest of the room is dark besides the sphere of light around you from the candle."
print "You probably fell asleep reading"
raw_input("...")
print "Thank god you didn't burn the rathouse down."

if character == "Ratzo":
	print "...and suddenly a voice"
	print "Hi Ratzo...Would you like the package you left me back?"
	package = raw_input("(y/n) \n > ")
		if package == "y":
			print "A package slides out of the darkness towards your bed"
		
		elif package == "n":
			print "\"Very well then, I'll keep it\", \n says the voice"
			print "You get out of bed and begin wandering into the darkness"
			print "You feel around the room helplessly and touch what feels like a door knob"
			
			raw_input("Should you: 1), Turn it \n 2) Look for a keyhole to peak through \n 3) wander some more")			 	
	





if character == "Sir. Ratsalot":
	print "Hey Sir Ratsalot...nice to see you again."
	
if character == "Elfred Ratskill":
	print "Hello Elfred"