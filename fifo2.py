# Prompt user to enter the number of processes and their arrival and burst times
number_of_jobs = int(input("Enter number of process: "))
process_id = []
burst_time = []
arrival_time = []

for i in range(number_of_jobs):
    process_id.append(i+1)
    a, b = input(f"Enter arrival time and burst time (separated by space) for Process {i+1}: ").split()
    arrival_time.append(int(a))
    burst_time.append(int(b))

# Sort the arrival times in ascending order
arrival_time.sort()

# Order the process IDs and burst times based on the arrival times
ordered_process_id = [x for _, x in sorted(zip(arrival_time, process_id))]
ordered_burst_time = [x for _, x in sorted(zip(arrival_time, burst_time))]

# Calculate the starting time, completion time, wait time, and turn-around time for each process
starting_time = [0] * number_of_jobs
completion_time = [0] * number_of_jobs
wait_time = [0] * number_of_jobs
turn_around_time = [0] * number_of_jobs
for i in range(number_of_jobs):
    if i + 1 == 1:
        starting_time[i] = arrival_time[i]
        completion_time[i] = starting_time[i] + ordered_burst_time[i]
    else:
        if arrival_time[i] < completion_time[i-1]:
            starting_time[i] = completion_time[i-1]
            completion_time[i] = starting_time[i] + ordered_burst_time[i]
        else:
            starting_time[i] = arrival_time[i]
            completion_time[i] = starting_time[i] + ordered_burst_time[i]
    wait_time[i] = starting_time[i] - arrival_time[i]
    turn_around_time[i] = completion_time[i] - arrival_time[i]
    
# Print the results in a table
print("Process | Arrival | Starting | Burst | Completion | Turn Around | Wait |")
for i in range(number_of_jobs):
    print(f"P{ordered_process_id[i]} | {arrival_time[i]} | {starting_time[i]} | {ordered_burst_time[i]} | {completion_time[i]} | {turn_around_time[i]} | {wait_time[i]}")
