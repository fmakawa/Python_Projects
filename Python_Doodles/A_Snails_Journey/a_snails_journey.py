

def snail_trip(height,daymv,nightmv):
    # height>daymv>nightmv
    if height > daymv and daymv > nightmv:
        days = int(((height - daymv)/(daymv - nightmv))+1)
        print (days)
        return days

snail_trip(15,1,0.5)
