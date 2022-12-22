numberOfJobs = int(input('Enter no of processes: '))
burstTime        = [0] * numberOfJobs 
arrivalTime      = [0] * numberOfJobs 
arrivalBurstTime = [0] *  numberOfJobs
dummy = [0] *  numberOfJobs
for i in range(numberOfJobs):
    a,b = input("Enter arrival time and burst time (seperate by space) for Process  "  + str(i+1) + " : ").split()
    burstTime[i]        = int(b)
    arrivalTime[i]      = int(a)
    dummy[i] = [i+1, burstTime[i]]
    arrivalBurstTime[i] = [arrivalTime[i], burstTime[i], i+1, 0, 0, 0] 

waitPool = [] #to keep jobs in a queue
executedJob = [] #to keeping records of executed jobs
jobsTodo = arrivalBurstTime[:] #copy the in formation of jobs to do

jobsTodo.sort(key=lambda x: x[0])

for i in range(numberOfJobs):
    for k in range(numberOfJobs):
        if jobsTodo[i][0] == jobsTodo[k][0]:
            if jobsTodo[i][1]<jobsTodo[k][1]:
                jobsTodo[i], jobsTodo[k] = jobsTodo[k], jobsTodo[i]

totalBurstTime = 0
arrival = []
for job in jobsTodo:
    totalBurstTime += job[1]
    arrival.append(job[0])

currentTime = min(arrival)
totalScheduleTime = min(arrival) + totalBurstTime
executionGraph = []

while totalScheduleTime:
    for job in jobsTodo:
        if job[0] <= currentTime:
            waitPool.append(job)
    waitPool.sort(key=lambda x: x[1])
    newJobDone = waitPool.pop(0)
    newJobDone[1] -= 1
    executionGraph.append(newJobDone[2])
    waitPool = []
    for job in jobsTodo:
        if job[2] == newJobDone[2]:
            job = newJobDone
    
    comp = currentTime
    for job in jobsTodo:
        if job[1] == 0:
            job[3] = comp+1
            executedJob.append(job)
    
    for job in jobsTodo:
        if job[1] == 0:
            jobsTodo.remove(job)
    
    if jobsTodo == []:
        break
    currentTime += 1
    totalScheduleTime -= 1

for job in executedJob:
    for i in range(numberOfJobs):
        if dummy[i][0] == job[2]:
            job[1]=dummy[i][1]

totalTurnAround = 0
totalWaitTime = 0

for job in executedJob:
    job[4] = job[3] - job[0] #calculating the turnaround time
    job[5] = job[4] - job[1] #calculating the waiting time of job
    totalTurnAround += job[4]
    totalWaitTime += job[5]


print(executionGraph)
print("Process | Arrival |  Burst | Completion | Turn Around | Wait |")
for job in executedJob:
    print(" " ,"P"+str(job[2]) ,"   | ", job[0], "     | ",  job[1], "   |   ", job[3], "       |  ", 
    job[4], "       |   ", job[5])  

print("Average Turn Around Time: ", totalTurnAround/numberOfJobs)
print("Average Waiting Time: ", totalWaitTime/numberOfJobs)