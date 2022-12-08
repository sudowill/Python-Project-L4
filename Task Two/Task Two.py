from statistics import mean

print("Park Run Recorder")
print("================================================")
print("Please write your inputs in the correct format 'Number of Runner'::'Time Taken' if finished all inputs say 'END'")
print("================================================")
ListOfTimes = []
while True:
    # Asks for inputs until the user puts in END
    runner_time = input(" > ")
    runner_time = runner_time.upper

    if runner_time == "END":

        break
    else:
        # Splits the two datas into ::
        ListOfTimes.append(runner_time.split("::"))
if len(ListOfTimes) != 0:
    # Stores the data inputted into a list
    times = []

    for i in range(len(ListOfTimes)):

        times.append(int(ListOfTimes[i][1]))
    # Calculations for all the different times
    minimumTime = int(min(times))
    maximumTime = divmod(int(max(times)), 60)
    maximumTime = str(maximumTime[0]) + "minutes," + str(maximumTime[1]) + "seconds"
    averageTime = divmod(int(mean(times)), 60)
    averageTime = str(averageTime[0]) + " minutes, " + str(averageTime[1]) + " seconds"

    for i in range(len(ListOfTimes)):

        if minimumTime == int(ListOfTimes[i][1]):

            fastest = "#" + str(ListOfTimes[i][0])

    minimumTime = divmod(minimumTime, 60)

    minimumTime = str(minimumTime[0]) + "minutes," + str(minimumTime[1]) + "seconds"

    # Gives the output of the math
    print("List of Runners Times: ", len(ListOfTimes))
    print("Average Time of Runners: ", averageTime)
    print("Fastest Timed Runner: ", minimumTime)
    print("Slowest Timed Runner: ", maximumTime)
    print("Fastest Runner: ", fastest)

else:
    print("Error, no times found")
