### INSTRUCTIONS ###
'''
Bloomberg needs a new system to schedule conference rooms! To keep things simple, the system operates in 15 minutes blocks, and only during an 8 hour workday, so that there are 32 available time slots per day for each room.

Users will submit one of two different commands: Create Booking, and Query Available.

When a user attempts to create a booking, they will submit a Room Id, a starting Timeslot, and a length (in timeslots). Each conference room can only be occupied by one user, and is booked in increments of timeslots (a minimum booking is length 1, maximum is length 32). Any user can book any room for as many slots as possible, so long as their booking does not interfere with an already occupied room. If the booking overlaps with any other bookings for that conference room (even if it's only for one slot of many), the entire booking command is rejected (i.e., the room schedule remains unchanged).

A user can also query availability to ask which rooms are available during a certain time block (a starting timeslot + a length, in timeslots). The system should report to the user which rooms are available for the entire length of their requested time. If a room is unavailable for any amount of time during the requested window, it is not returned from the Query.


> Input Specifications

Input will be the number of rooms N on the first line (1<=N<=100), followed by any number of the following request types:
    Booking:	RoomId-TimeSlot-#OfSlots
    Query:	TimeSlot-#OfSlots
You can assume that no more than 100 requests will be made. Also, RoomIds and TimeSlots are indexed starting at 1, not 0.


> Output Specifications

Output as many lines as necessary to answer each request in the order they were received.
    Booking:	You will output Y if the booking is possible and N otherwise.
    Query:	You will output a list of space-delimited room ids in order. There should be no trailing or preceding spaces. If there are no rooms available that match the Query, print None

'''


### MY SOLUTION (accepted) ###

#Problem        : Finals Spring 2015 - Conference Room Scheduler
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

# room and slot numbers indexed from 1
def areSlotsEmpty(mat,room,slot1,slots):
    if slot1+slots-1 > 32:
        return False
    return sum(mat[room-1][slot1-1:slots+slot1-1])==0 # all slots have 0 or 1, if sum is 0 all are 0

data = sys.stdin.read().splitlines()
N=int(data[0])
queries = [[int(n) for n in line.split('-')] for line in data[1:]]

slot_mat = [[0 for x in range(32)] for y in range(N)] # table of rooms and slots. Will be 1 for taken - no identity need be saved
for q in queries:
    if len(q) == 3: # Booking
        if(areSlotsEmpty(slot_mat,q[0],q[1],q[2])):
            for i in range(q[1]-1,q[2]+q[1]-1):
                slot_mat[q[0]-1][i] = 1
            print('Y')
        else:
            print('N')
    else: # assumed len(q)==2 -> Query
        free_rooms=''
        for room in range(1,N+1):
            if(areSlotsEmpty(slot_mat,room,q[0],q[1])):
                free_rooms += str(room) + ' '
        if free_rooms=='':
            print('None')
        else:
            print(free_rooms.rstrip())