from statistics import mean

print("Park Run Recorder")
print("================================================")
print("Please write your inputs in the correct format 'Number of Runner'::'Time Taken' if finished all inputs say 'END'")
print("================================================")
listOfTimes = []
while True:
    runnerTime = input(" > ")
    runnerTime = runnerTime.upper

    if runnerTime == "END":

        break
    else:
        listOfTimes.append(runnerTime.split("::"))
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

            fastest = "#" + str(listOfTimes[i][0])

    minimumTime = divmod(minimumTime, 60)

    minimumTime = str(minimumTime[0]) + "minutes," + str(minimumTime[1]) + "seconds"

    print("List of Runners Times: ", len(listOfTimes))
    print("Average Time of Runners: ", averageTime)
    print("Fastest Timed Runner: ", minimumTime)
    print("Slowest Timed Runner: ", maximumTime)
    print("Fastest Runner: ", fastest)

else:
    print("Error, no times found")
