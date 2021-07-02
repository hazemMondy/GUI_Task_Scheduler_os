import gantt


def FCFS_Specific(NumOfProcesses, BurstTimeList):
    
    # # SJF bsmga
    ArrivalTime = []
    ArrivalStatus = []
    waitingTime = 0
    totalTime = 0
    GanttChart = []
    # for i in range(0, NumOfProcesses):
    #     ArrivalTime.append(BurstTimeList[i][2])
    #     ArrivalStatus.append(False)
    #     waitingTime -= (BurstTimeList[i][1]+BurstTimeList[i][2])
    #     totalTime += BurstTimeList[i][1]
    # smallestIndex = 0
    # smallestValue = totalTime
    # for i in range(0, totalTime):
    #     smallestValue = totalTime
    #     for j in range(0, NumOfProcesses):
    #         if i == ArrivalTime[j]:
    #             ArrivalStatus[j] = True
        
    #     for j in range(0, NumOfProcesses):
    #         if ArrivalStatus[j] and BurstTimeList[j][1] < smallestValue and BurstTimeList[j][1] != 0:
    #             smallestValue = BurstTimeList[j][1]
    #             smallestIndex = j
    #     GanttChart.append(smallestIndex+1)
    #     BurstTimeList[smallestIndex][1] -= 1
    #     if BurstTimeList[smallestIndex][1] == 0:
    #         waitingTime += (i+1)
            
    # task1 -
    BurstTimeList.sort(key=lambda x: (x[2], x[0])) # Sort by arrival time then by task id 
    for i in range(0, NumOfProcesses):
        for j in range(0, BurstTimeList[i][1]):
            GanttChart.append(BurstTimeList[i][0])
        waitingTime += BurstTimeList[i][1]*(NumOfProcesses-i-1)
    waitingTime /= NumOfProcesses
    return GanttChart, waitingTime

def FCFS(NumOfProcesses, BurstTimeList):
    
    # # SJF bsmga
    ArrivalTime = []
    ArrivalStatus = []
    waitingTime = 0
    totalTime = 0
    GanttChart = []
    # for i in range(0, NumOfProcesses):
    #     ArrivalTime.append(BurstTimeList[i][2])
    #     ArrivalStatus.append(False)
    #     waitingTime -= (BurstTimeList[i][1]+BurstTimeList[i][2])
    #     totalTime += BurstTimeList[i][1]
    # smallestIndex = 0
    # smallestValue = totalTime
    # for i in range(0, totalTime):
    #     smallestValue = totalTime
    #     for j in range(0, NumOfProcesses):
    #         if i == ArrivalTime[j]:
    #             ArrivalStatus[j] = True
        
    #     for j in range(0, NumOfProcesses):
    #         if ArrivalStatus[j] and BurstTimeList[j][1] < smallestValue and BurstTimeList[j][1] != 0:
    #             smallestValue = BurstTimeList[j][1]
    #             smallestIndex = j
    #     GanttChart.append(smallestIndex+1)
    #     BurstTimeList[smallestIndex][1] -= 1
    #     if BurstTimeList[smallestIndex][1] == 0:
    #         waitingTime += (i+1)
            
    # task1 -
    
    for i in range(0, NumOfProcesses):
        for j in range(0, BurstTimeList[i][1]):
            GanttChart.append(BurstTimeList[i][0])
        waitingTime += BurstTimeList[i][1]*(NumOfProcesses-i-1)
    waitingTime /= NumOfProcesses
    return GanttChart, waitingTime


def SJFNonPreemptive(NumOfProcesses, BurstTimeList):
    # swapList = []
    # for i in range(0, NumOfProcesses):
    #     c = i
    #     for j in range(i+1, NumOfProcesses):
    #         if BurstTimeList[j][1] < BurstTimeList[c][1]:
    #             c = j
    #     if c != i:
    #         swapList = BurstTimeList[c]
    #         BurstTimeList[c] = BurstTimeList[i]
    #         BurstTimeList[i] = swapList
    print("before: ",BurstTimeList)
    BurstTimeList.sort(key=lambda x: (x[2],x[1])) #sort by arrival time then shortest job first
    print("after: ",BurstTimeList)
    return FCFS(NumOfProcesses, BurstTimeList)


def SJFPreemptive(NumOfProcesses, BurstTimeList):
    ArrivalTime = []
    ArrivalStatus = []
    waitingTime = 0
    totalTime = 0
    GanttChart = []
    for i in range(0, NumOfProcesses):
        ArrivalTime.append(BurstTimeList[i][2])
        ArrivalStatus.append(False)
        waitingTime -= (BurstTimeList[i][1]+BurstTimeList[i][2])
        totalTime += BurstTimeList[i][1]
    smallestIndex = 0
    smallestValue = totalTime
    for i in range(0, totalTime):
        smallestValue = totalTime
        for j in range(0, NumOfProcesses):
            if i == ArrivalTime[j]:
                ArrivalStatus[j] = True
        
        for j in range(0, NumOfProcesses):
            if ArrivalStatus[j] and BurstTimeList[j][1] < smallestValue and BurstTimeList[j][1] != 0:
                smallestValue = BurstTimeList[j][1]
                smallestIndex = j
        GanttChart.append(smallestIndex+1)
        BurstTimeList[smallestIndex][1] -= 1
        if BurstTimeList[smallestIndex][1] == 0:
            waitingTime += (i+1)
            
            
    waitingTime /= NumOfProcesses
    return GanttChart, waitingTime


def PriorityNonPreemptive(NumOfProcesses, BurstTimeList):
    # swapList = []
    # for i in range(0, NumOfProcesses):
    #     c = i
    #     for j in range(i+1, NumOfProcesses):
    #         if BurstTimeList[j][2] < BurstTimeList[c][2]:
    #             c = j
    #     if c != i:
    #         swapList = BurstTimeList[c]
    #         BurstTimeList[c] = BurstTimeList[i]
    #         BurstTimeList[i] = swapList
    
    BurstTimeList.sort(key=lambda x: (x[2], x[3])) # Sort by arrival time then priority
    return FCFS(NumOfProcesses, BurstTimeList)


def PriorityPreemptive(NumOfProcesses, BurstTimeList):
    ArrivalTime = []
    ArrivalStatus = []
    waitingTime = 0
    totalTime = 0
    GanttChart = []
    print("Burst1: ", BurstTimeList)
    for i in range(0, NumOfProcesses):
        ArrivalTime.append(BurstTimeList[i][2])
        ArrivalStatus.append(False)
        waitingTime -= (BurstTimeList[i][1]+BurstTimeList[i][2])
        totalTime += BurstTimeList[i][1]
    print("Burst2: ", BurstTimeList)
    smallestIndex = 0
    smallestValue = 30
    for i in range(0, totalTime):
        smallestValue = totalTime
        for j in range(0, NumOfProcesses):
            if i == ArrivalTime[j]:
                ArrivalStatus[j] = True
        for j in range(0, NumOfProcesses):
            if ArrivalStatus[j] and BurstTimeList[j][3] < smallestValue and BurstTimeList[j][1] != 0:
                smallestValue = BurstTimeList[j][3]
                smallestIndex = j
        GanttChart.append(smallestIndex+1)
        BurstTimeList[smallestIndex][1] -= 1
        if BurstTimeList[smallestIndex][1] == 0:
            waitingTime += (i+1)
    waitingTime /= NumOfProcesses
    print("Burst3: ", BurstTimeList)
    print("Gantt ", GanttChart)

    return GanttChart, waitingTime


def RoundRobin(NumOfProcesses, BurstTimeList, TimeQuantum):
    waitingTime = 0
    GanttChart = []
    myLen = 0
    for i in range(0, NumOfProcesses):
        waitingTime -= BurstTimeList[i][1]
    i = 0
    NumOfZeroes = 0
    BurstTimeList.sort(key=lambda x: x[2])
    while True:
        if(BurstTimeList[i][1] == 0):
            i = (i+1) % NumOfProcesses
            continue
        if BurstTimeList[i][1] > TimeQuantum:
            BurstTimeList[i][1] -= TimeQuantum
            myLen += TimeQuantum
            for j in range(0, TimeQuantum):
                GanttChart.append(BurstTimeList[i][0])
        else:
            myLen += BurstTimeList[i][1]
            for j in range(0, BurstTimeList[i][1]):
                GanttChart.append(BurstTimeList[i][0])
            BurstTimeList[i][1] = 0
            NumOfZeroes += 1
            waitingTime += myLen
        if NumOfZeroes == NumOfProcesses:
            break
        i = (i+1) % NumOfProcesses
    waitingTime /= NumOfProcesses
    # print("Gantt ", GanttChart)
    return GanttChart, waitingTime

# [ [1,6], [2,5]]


def EnterBurstTime(BurstTimeList, BurstData):
    for i in range(len(BurstData)):
        BurstTimeList[i].append(int(BurstData[i]))
    print("enterbursttime ", BurstTimeList)


def EnterArrivalTime(BurstTimeList, ArrivalData):
    for i in range(len(ArrivalData)):
        BurstTimeList[i].append(int(ArrivalData[i]))


def EnterPriority(BurstTimeList, PriorityData):
    for i in range(len(PriorityData)):
        BurstTimeList[i].append(int(PriorityData[i]))


def GanttOutput(GanttChart):
    firstLine = "|"
    aboveLine = "_"
    underLine = "‾"
    secondLine = "0"
    for i in range(0, len(GanttChart)):
        firstLine = firstLine + "P" + str(GanttChart[i]) + "|"
        if i < 10:
            secondLine = secondLine + "  " + str((i+1))
        else:
            secondLine = secondLine + " " + str((i+1))
    for i in range(1, len(firstLine)):
        underLine += "‾"
        aboveLine += "_"
    return aboveLine + "\n" + firstLine + "\n" + underLine + "\n" + secondLine


def execute(scheduler, NumOfProcesses, BurstData, ArrivalData, PriorityData, QuantumData):

    BurstTimeList = []
    for i in range(0, NumOfProcesses):
        newList = []
        newList.append((i+1))
        BurstTimeList.append(newList)
        # print("BurstTimeList ",BurstTimeList[i][0])
        # print("BurstTimeList ",BurstTimeList[i][1])
    # print("BurstTimeList ",BurstTimeList)

    waitingTime = 0
    GanttChart = []
    if scheduler == 'FCFS':
        EnterBurstTime(BurstTimeList, BurstData)
        EnterArrivalTime(BurstTimeList, ArrivalData)
        GanttChart, waitingTime = FCFS_Specific(NumOfProcesses, BurstTimeList)
    elif scheduler == 'SJF':
        EnterBurstTime(BurstTimeList, BurstData)
        EnterArrivalTime(BurstTimeList, ArrivalData)
        GanttChart, waitingTime = SJFNonPreemptive(
            NumOfProcesses, BurstTimeList)
    elif scheduler == 'SRTF':
        EnterBurstTime(BurstTimeList, BurstData)
        EnterArrivalTime(BurstTimeList, ArrivalData)
        GanttChart, waitingTime = SJFPreemptive(NumOfProcesses, BurstTimeList)
    elif scheduler == "P(PR)":
        EnterBurstTime(BurstTimeList, BurstData)
        EnterArrivalTime(BurstTimeList, ArrivalData)
        EnterPriority(BurstTimeList, PriorityData)
        GanttChart, waitingTime = PriorityPreemptive(
            NumOfProcesses, BurstTimeList)
    elif scheduler == 'P(NONPR)':
        EnterBurstTime(BurstTimeList, BurstData)
        EnterArrivalTime(BurstTimeList, ArrivalData)
        EnterPriority(BurstTimeList, PriorityData)
        GanttChart, waitingTime = PriorityNonPreemptive(
            NumOfProcesses, BurstTimeList)
    elif scheduler == 'RR':
        # print("burst in rr: ", BurstTimeList)
        EnterBurstTime(BurstTimeList, BurstData)
        EnterArrivalTime(BurstTimeList, ArrivalData)
        print("burst in rr: ", BurstTimeList)
        GanttChart, waitingTime = RoundRobin(
            NumOfProcesses, BurstTimeList, QuantumData)

    gantt.drawGantt(NumOfProcesses, GanttChart, waitingTime)
    print("GanttChart :")
    print(GanttOutput(GanttChart))
    print("waiting time = ", waitingTime)
    print("BurstTIMELIST ", BurstTimeList)
