with open("input.txt", "r") as f:
    x = f.readlines()

max_trucks, car_lenght, cs1, cs2 = map(int, x[0].split())
print(max_trucks)

car_speed = cs1 / cs2  # car speed
car_front = car_lenght  # car front
current_truck = 1  # current truck

current_lane = "right"  # current lane,

lane_changes = 0  # number of lane changes

dct = {  # dictionary of trucks

}

for i in range(1, max_trucks + 1):  # normally (max_trucks)
    truck_front, truck_back, s1, s2 = map(int, x[i].split())  # front and back of the truck, speed of the truck ( two values
    # needed to calculate speed of the truck )

    truck_speed = s1 / s2  # speed of the truck



    dct[i] = [truck_front, truck_back, truck_speed]



while True:
    speed_to_add = car_speed  # speed to add ( by default the car speed )

    print(dct[current_truck][1] - car_front, car_speed)

    if dct[current_truck][1] - car_front < car_speed:  # if the space between trucks back and car front is less than car speed
        speed_to_add = dct[current_truck][1] - car_front  # then sta = the distance between trucks back and car front
        print("sta = ", speed_to_add)

    # adding the speed to the car and trucks
    car_front += speed_to_add  # add the speed to the car front
    for i in dct:
        dct[i][0] += dct[i][2]  # add the speed of the truck to the front of the truck
        dct[i][1] += dct[i][2]  # and the back

    # checking if the trucks ale touching one another
    for truck in len(dct):
        if dct[truck][0] >= dct[truck + 1][1]:
            dct[truck][2] = dct[truck+1][2]



