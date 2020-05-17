
lectures = [(30, 75), (0, 50), (60, 150)]


def minimum(times):
    len_times = len(times)
    #start times
    start = []
    for i in range(len_times):
        start.append(times[i][0])
    #end times
    end = []
    for e in range(len_times):
        end.append(times[e][1])

    #room i
    for h in range(len_times):
        add_room = False
        for g in range(len_times):
            if times[g][0] >= times[h][0] and times[g][0] <= times[h][0] :
                add_room = True
                


    #new room if time in any room

    #repeat until no more time    
    
    return (start, end)


print(minimum(lectures))


