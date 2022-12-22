numberOfJobs = int(input("Enter number of process: "))
processID = []
burstTime = []
arrivalTime = []

#comment
for i in range(numberOfJobs):
    processID.append(i+1)
    a,b = input("Enter arrival time and burst time (seperate by space) for Process  "  + str(i+1) + " : ").split()
    arrivalTime.append(int(a))
    burstTime.append(int(b))

#sort the arrival time from lowest to highest
sortedArrivalTime = sorted(arrivalTime)

#order the process ID and Bursttime based on the arrival time
orderedProcessId = [x for _,x in sorted(zip(arrivalTime, processID))]
orderedBurstTime = [x for _,x in sorted(zip(arrivalTime, burstTime))]

#calculate the starting time and completion time
startingTime = [0]*numberOfJobs
completionTime = [0]*numberOfJobs
waitTime = [0]*numberOfJobs
turnAroundTime = [0]*numberOfJobs
for i in range(numberOfJobs):
    if i + 1 == 1:
        startingTime[i] = sortedArrivalTime[i]
        completionTime[i] = startingTime[i] + orderedBurstTime[i]
    else:
        if sortedArrivalTime[i] < completionTime[i-1]:
            startingTime[i] = completionTime[i-1]
            completionTime[i] = startingTime[i] + orderedBurstTime[i]
        else:
            startingTime[i] = sortedArrivalTime[i]
            completionTime[i] = startingTime[i] + orderedBurstTime[i]
    waitTime[i] = startingTime[i] - sortedArrivalTime[i]
    turnAroundTime[i] = completionTime[i] - sortedArrivalTime[i]
    

print("Process | Arrival | Starting | Burst | Completion | Turn Around | Wait |")
for i in range(numberOfJobs):
    print(" " ,"P"+str(orderedProcessId[i]) ,"   | ", sortedArrivalTime[i], "     | ", startingTime[i],
    "      | ", orderedBurstTime[i], "   |   ", completionTime[i], "       |  ", 
    turnAroundTime[i], "       |   ", waitTime[i])