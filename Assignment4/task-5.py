# scheduling.py

def fcfs(processes):
    wt = 0
    tat_list = []
    wt_list = []

    for bt in processes:
        wt_list.append(wt)
        tat_list.append(wt + bt)
        wt += bt

    print("\nFCFS Scheduling:")
    print("BT\tWT\tTAT")
    for i in range(len(processes)):
        print(f"{processes[i]}\t{wt_list[i]}\t{tat_list[i]}")

def sjf(processes):
    sorted_p = sorted(processes)
    fcfs(sorted_p)

def round_robin(processes, quantum):
    rem = processes[:]
    t = 0
    wt = [0]*len(processes)
    tat = [0]*len(processes)

    while True:
        done = True
        for i in range(len(processes)):
            if rem[i] > 0:
                done = False
                if rem[i] > quantum:
                    t += quantum
                    rem[i] -= quantum
                else:
                    t += rem[i]
                    wt[i] = t - processes[i]
                    rem[i] = 0
        if done:
            break

    for i in range(len(processes)):
        tat[i] = wt[i] + processes[i]

    print("\nRound Robin:")
    print("BT\tWT\tTAT")
    for i in range(len(processes)):
        print(f"{processes[i]}\t{wt[i]}\t{tat[i]}")

def priority(processes):
    sorted_p = sorted(processes, key=lambda x: x[1])  
    print("\nPriority Scheduling:")
    wt = 0
    for pid, bt, pr in sorted_p:
        tat = wt + bt
        print(f"P{pid}\tBT={bt}\tPR={pr}\tWT={wt}\tTAT={tat}")
        wt += bt

# --------- Test ---------
bt_list = [10, 5, 8]

fcfs(bt_list)
sjf(bt_list)
round_robin(bt_list, 2)

priority([(1,10,3), (2,5,1), (3,8,2)])
