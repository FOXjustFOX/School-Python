# noft, cl, cs1, cs2 = map(int, input().split()) # number of trucks, car lenght, car speed ( two values needed to calculate speed of the car )
with open("olimpiada 2022 etap 1\input.txt", "r") as f:
    x = f.readlines()
    
noft, cl, cs1, cs2 = map(int, x[0].split())
print(noft)
print(x)

cs = cs1 / cs2 # car speed
cf = cl # car front
ct = 1 # current truck

lchanges = 0 # number of lane changes

dct = { # dictionary of trucks
    
}

for i in range(1,noft):
    front, back, s1, s2 = map(int, x[i].split()) # front and back of the truck, speed of the truck ( two values needed to calculate speed of the truck )
    
    s = s1 / s2 # speed of the truck
    
    dct[i] = [front, back, s] # adding to the dictionary of trucks !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
print(dct)
    
for i in dct:
    print(f"truck: {i} front: {dct[i][0]} back: {dct[i][1]} speed: {dct[i][2]}")
    


# while the front of the car plus length is not in the same place as the back of the truck (add one turn at the end)
while cf + cl < dct[noft][0]:
    sta = cs # speed to add ( by default the car speed )

    
# checking if the trucks ale touching one another
    try:
        for i in range(1,noft):
            if dct[i][0] >= dct[i+1][0]: # if the front of the truck is in the same place or further as the back of the next truck
                dct[i][2] = dct[i+1][2] # slow down the truck to the speed of the next truck
    
    except KeyError:
        print("jello")# if the truck is the last one
        pass
    
# car speed changes
    try:
        if  dct[ct][0] - cf == 0 and cf - cl > dct[ct-1][1]: # if the car is in the same place as the truck and theres place for the car to change lane
            lchanges += 1 # add one lane change
            ct += 1 # go on to the next truck
            print(f"changes {lchanges}")
            
        elif dct[ct][2] - cf < cs: # if the front of the car is closer to the truck than the car speed
            sta = dct[ct][2] - cf # the speed to add is the distance between the car and the truck
        # else the speed to add is the car speed
        
        
    except IndexError: # if there is no truck in back of the car
        lchanges += 1 # add one lane change
        ct += 1 # go on to the next truck
        print(f"changes {lchanges}")
        

# adding the speed to the car and trucks
    cf += sta # add the speed to the car front
    for i in dct:
        dct[i][0] += dct[i][2] # add the speed of the truck to the front of the truck
        

lchanges += 1 # add one lane change at the end

print(lchanges)
    
    
    
    