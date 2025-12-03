# TASK 1: CPU Scheduling (Priority + Round Robin)

# ---------- PRIORITY SCHEDULING ----------
def priority_scheduling():
    processes = []
    n = int(input("Enter number of processes: "))

    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        pr = int(input(f"Enter Priority (lower number = higher priority) for P{i+1}: "))
        processes.append((i+1, bt, pr))

    processes.sort(key=lambda x: x[2])  # Sort by priority

    wt = 0
    total_wt = 0
    total_tt = 0

    print("\nPriority Scheduling:")
    print("PID\tBT\tPriority\tWT\tTAT")

    for pid, bt, pr in processes:
        tat = wt + bt
        print(f"{pid}\t{bt}\t{pr}\t\t{wt}\t{tat}")
        total_wt += wt
        total_tt += tat
        wt += bt

    print(f"Average Waiting Time: {total_wt / n}")
    print(f"Average Turnaround Time: {total_tt / n}")


# ---------- ROUND ROBIN SCHEDULING ----------
def round_robin():
    n = int(input("\nEnter number of processes: "))
    burst_times = []
    for i in range(n):
        burst_times.append(int(input(f"Enter Burst Time for P{i+1}: ")))

    quantum = int(input("Enter Time Quantum: "))

    remaining_bt = burst_times[:]
    t = 0
    wt = [0] * n
    tat = [0] * n

    print("\nRound Robin Scheduling Order:")
    while True:
        done = True
        for i in range(n):
            if remaining_bt[i] > 0:
                done = False
                print(f"P{i+1}", end=" ")

                if remaining_bt[i] > quantum:
                    t += quantum
                    remaining_bt[i] -= quantum
                else:
                    t += remaining_bt[i]
                    wt[i] = t - burst_times[i]
                    remaining_bt[i] = 0

        if done:
            break

    for i in range(n):
        tat[i] = burst_times[i] + wt[i]

    print("\nPID\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{i+1}\t{burst_times[i]}\t{wt[i]}\t{tat[i]}")

    print(f"Average Waiting Time: {sum(wt)/n}")
    print(f"Average Turnaround Time: {sum(tat)/n}")


# MAIN CALLS
print("----- CPU Scheduling -----")
priority_scheduling()
round_robin()
