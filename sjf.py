
numberOfJobs = int(input('Enter no of processes: '))
burstTime        = [0] * numberOfJobs 
arrivalTime      = [0] * numberOfJobs 
arrivalBurstTime = [0] *  numberOfJobs 
for i in range(numberOfJobs):
    a,b = input("Enter arrival time and burst time (seperate by space) for Process  "  + str(i+1) + " : ").split()
    burstTime[i]        = int(b)
    arrivalTime[i]      = int(a)
    arrivalBurstTime[i] = [arrivalTime[i], burstTime[i], i+1, 0, 0, 0] 

waitPool = [] #to keep jobs in a queue
executedJob = [] #to keeping records of executed jobs
jobsTodo = arrivalBurstTime.copy() # copy the in formation of jobs to do

jobsTodo.sort(key=lambda x: x[0])


for i in range(numberOfJobs):
    for k in range(numberOfJobs):
        if jobsTodo[i][0] == jobsTodo[k][0]:
            if jobsTodo[i][1]<jobsTodo[k][1]:
                jobsTodo[i], jobsTodo[k] = jobsTodo[k], jobsTodo[i]

completionTime = [] #to keep a record of completed times

#calculate and append the completion time of first job
completionTime.append(jobsTodo[0][0] + jobsTodo[0][1]) 

#remove the first job from the job to do list
jobDone = jobsTodo.pop(0)

#add the first job to the executed job list
executedJob.append(jobDone)

#initialise a temporary variable to hold current completion time
currentTime = completionTime[0]

#Executing the jobs
while jobsTodo: #while there are jobs to do
#iterate over the jobs and compare their arrival time to the current
#completion time, if the arrival time is less or equal add to the wait queue
#sort the wait pool by burst time and remove the first element
#add the first job to the executed task and remove from the jobs to do list
#repeat till all jobs are done
    for job in jobsTodo: 
        if job[0] <= currentTime:
            waitPool.append(job)
    waitPool.sort(key=lambda x: x[1])
    newJobDone = waitPool.pop(0)
    executedJob.append(newJobDone)
    jobsTodo.remove(newJobDone)
    completionTime.append(completionTime[-1]+newJobDone[1])
    currentTime = completionTime[-1] 
    waitPool = []

    
totalTurnAround = 0
totalWaitTime = 0
#calculating turnaround, wait time and 
for job in executedJob:
    job[3] = completionTime.pop(0) #getiing the completion time for this process
    job[4] = job[3] - job[0] #calculating the turnaround time
    job[5] = job[4] - job[1] #calculating the waiting time of job
    totalTurnAround += job[4]
    totalWaitTime += job[5]
    


#displaying results
print("Process | Arrival |  Burst | Completion | Turn Around | Wait |")
for job in executedJob:
    print(" " ,"P"+str(job[2]) ,"   | ", job[0], "     | ",  job[1], "   |   ", job[3], "       |  ", 
    job[4], "       |   ", job[5])  

print("Average Turn Around Time: ", totalTurnAround/numberOfJobs)
print("Average Waiting Time: ", totalWaitTime/numberOfJobs)