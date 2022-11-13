# noft, cl, cs1, cs2 = map(int, input().split()) # number of trucks, car lenght, car speed ( two values needed to
# calculate speed of the car )
with open("input.txt", "r") as f:
    x = f.readlines()
    
noft, cl, cs1, cs2 = map(int, x[0].split())
print(noft)
print(x)

cs = cs1 / cs2 # car speed
cf = cl # car front
ct = 1 # current truck

clane = 0  # current lane,      0 = right, 1 = left

lchanges = 0  # number of lane changes

dct = { # dictionary of trucks
    
}

for i in range(1,noft+1):
    front, back, s1, s2 = map(int, x[i].split())  # front and back of the truck, speed of the truck ( two values
    # needed to calculate speed of the truck )
    
    s = s1 / s2 # speed of the truck
    
    dct[i] = [front, back, s]  # adding to the dictionary of trucks # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
print(dct)


# while the front of the car plus length is not in the same place as the back of the truck (add one turn at the end)
while True:
    sta = cs  # speed to add ( by default the car speed )
    
# checking if the trucks ale touching one another
# car speed changes
    if clane == 0:  # is on right lane
        if dct[ct][1] - cs < cf:  # if the space between trucks back and car front is less than car speed
            sta = dct[ct][1] - cf  # then sta = the distance between trucks back and car front

        if dct[ct][1] == cf:  # if the car front is touching trucks back then change lanes
            lchanges += 1  # add one lane change
            ct += 1  # go on to the next truck
            clane = 1  # change the lane to left
            print(f"changes {lchanges}")

    elif clane == 1:  # is on left lane
        try:
            if dct[ct][0] <= cf - cl and dct[ct+1][1] > cf:  # if front of the ct truck is less or equal to car back
                # and there's place in the front of the car
                lchanges += 1  # add one lane change
                ct += 1  # go on to the next truck
                print(f"changes {lchanges}")

                clane = 0  # change the lane to left

        except IndexError:  # if there's no truck in front of the car, it means that all the trucks have been
            # overtaken
            lchanges += 1  # add one lane change
            print(f"changes {lchanges}")
            break  # end the while loop

    # if dct[ct][1] > cf:  # if the truck is in front of the car, then change the lanes

    for i in range(1,noft):
        try:
            if dct[i][0] >= dct[i+1][0]:  # if the front of the truck is in the same place or further as the back of the
                # next truck
                dct[i][2] = dct[i+1][2]  # slow down the truck to the speed of the next truck
        except KeyError:
            pass

# adding the speed to the car and trucks
    cf += sta # add the speed to the car front
    for i in dct:
        dct[i][0] += dct[i][2] # add the speed of the truck to the front of the truck
        dct[i][1] += dct[i][2]  # and the back

    # for i in dct:
    #     print(f"truck: {i} front: {dct[i][0]} back: {dct[i][1]} speed: {dct[i][2]} \n")

    print(sta,"\n")

# lchanges += 1 # add one lane change at the end

print(lchanges)
    
    
    
    