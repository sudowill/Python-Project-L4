import random
while True:
      # Random Word Generation
      RANDOMPASSWORDLIST = ["gate", "peep", "lacking", "decide", "perfect", "expert", "empty", "receptive", "lavish", "protect", "bucket", "annoy", "evanescent", "mysterious",
      "popper", "toilet", "juice", "gadget", "lemon", "python", "solid", "snake", "final", "fantasy", "grapple", "hippo", "hide", "wibbly", "wobbly", "timey", "wimey", "stuff"]
      try:
            # Ask the user for the amount of passwords they want
            numberPass = input("How many passwords would you like? ")
            print("Password Generator")
            print("================== \n")
            
            # Generate the passwords for however many the user specificated
            if 0 < int(numberPass) < 25:
                  for x in range (int(numberPass)):
                        NumberPassOne = (random.choice(RANDOMPASSWORDLIST))
                        NumberPassTwo = (random.choice(RANDOMPASSWORDLIST))
                        NumberPassThree = (random.choice(RANDOMPASSWORDLIST))
                        NumberPassFour = NumberPassOne + NumberPassTwo + NumberPassThree

                        print(NumberPassFour)
                  break
            else:
                  print("An error has occured")
      except ValueError:
            print("An error has occured")