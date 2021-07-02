import matplotlib.pyplot as plt
import random as random


def drawGantt(processNumber, gantt, waitingTime):
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()

    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Seconds')
    gnt.set_ylabel('Process')

    # Setting ticks on y-axis
    gnt.set_yticks([3])

    # Setting graph attribute
    gnt.grid(True)

    # set the random colors (R,G,B)
    colors = []
    for color in range(processNumber):
        colors.append((random.random(), random.random(), random.random()))

    # Loop to put labels
    for process in range(processNumber):
        gnt.broken_barh([(0, 0)], (5, 10), color=colors[process],
                        label='p'+str(process+1))

    # Loop to draw { gantt= [1,1,1,2,3,1,1] }
    for process in range(len(gantt)):
        gnt.broken_barh([(process, 1)], (5, 10),
                        color=colors[gantt[process]-1])

    gnt.legend()
    plt.title("Average Waiting Time: "+ str(waitingTime))
    
    # plt.subplots_adjust(top=0.2)
    
    plt.show()
    
