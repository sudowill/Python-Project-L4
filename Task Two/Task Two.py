from statistics import mean

print("Park Run Record")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

print("\nPlease enter all data as 'No. of Runner'::'Time Taken'' and if you would like to stop input say 'END'!\n")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

listOfTimes = []

while True:

    runner_time = input("> ")

    if runner_time == "END":

        break

    else:

        listOfTimes.append(runner_time.split("::"))

if len(listOfTimes) != 0:

    times = []

    for i in range(len(listOfTimes)):
        times.append(int(listOfTimes[i][1]))

    minimumTime = int(min(times))

    maximumTime = divmod(int(max(times)), 60)

    maximumTime = str(maximumTime[0]) + "minutes," + str(maximumTime[1]) + "seconds"

    averageTime = divmod(int(mean(times)), 60)

    averageTime = str(averageTime[0]) + " minutes, " + str(averageTime[1]) + " seconds"

    for i in range(len(listOfTimes)):

        if minimumTime == int(listOfTimes[i][1]):
            fastestRunner = "#" + str(listOfTimes[i][0])

            minimumTime = divmod(minimumTime, 60)

            minimumTime = str(minimumTime[0]) + "minutes," + str(minimumTime[1]) + "seconds"

            print("Total Runners:", len(listOfTimes))

            print("Average Time:", averageTime)

            print("fastestRunner Time:", minimumTime)

            print("Slowest Time:", maximumTime)

            print("\nBest Time Here: Runner", fastestRunner)

else:

    print("An error has occured")
