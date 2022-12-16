import random
while True:
      RANDOMPASSWORDLIST = ["gate", "peep", "lacking", "decide", "perfect", "expert", "empty", "receptive", "lavish", "protect", "bucket", "annoy", "evanescent", "mysterious",
      "popper", "toilet", "juice", "gadget", "lemon", "python", "solid", "snake", "final", "fantasy", "grapple", "hippo", "hide", "wibbly", "wobbly", "timey", "wimey", "stuff"]
      try:
            numberPass = input("How many passwords would you like? ")
            print("Password Generator")
            print("================== \n")
            if 0 < int(numberPass) < 25:
                  for x in range (int(numberPass)):
                        numberPassOne = (random.choice(RANDOMPASSWORDLIST))
                        numberPassTwo = (random.choice(RANDOMPASSWORDLIST))
                        numberPassThree = (random.choice(RANDOMPASSWORDLIST))
                        numberPassFour = numberPassOne + numberPassTwo + numberPassThree

                        print(numberPassFour)
                  break
            else:
                  print("An error has occured")
      except ValueError:
            print("An error has occured")