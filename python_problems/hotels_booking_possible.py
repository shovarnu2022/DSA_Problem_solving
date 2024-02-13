"""
A Hotel manager has to process an advance bookings of rooms
for the next season. His hotel has 'k' rooms. Bookings contain
an arrival date and a departure date. He wants to find out whether
there are enough rooms in the hotel to satisfy the demand.
Write a program that solves this problem in time O(N log N).

Input:

first list of arrival time of booking.
second list of departure time of booking.
Third is k which denotes count of rooms.
"""


def hotel_booking(arrival, depart, K):
    event = []
    for i in range(0, len(arrival)):
        t_arrive = ()
        t_arrive = t_arrive + (arrival[i], "RED")
        event.append(t_arrive)

    for i in range(0, len(depart)):
        t_depart = ()
        t_depart = t_depart + (depart[i], "BLUE")
        event.append(t_depart)
    event = sorted(event)

    guest = 0
    for e in event:
        if e[1] == 'RED':
            guest += 1
        else:
            guest -= 1

        if guest > K:
            return 0
    return 1


arrival = [1, 3, 5]
depart = [2, 6, 8]
print(hotel_booking(arrival, depart, 5))






