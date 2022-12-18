from librus import LibrusSession


session = LibrusSession()

session.login('8431309u', 'Kwiatek1')

lessons_plan = session.schedule()

weekdays = {
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
}


for i in range(len(l)):
    g = l[i]
    print(weekdays[g.day+1], g.index, g.name, g.teacher, g.time)
    try:
        if l[i+1].day > g.day:
            print('\n')
    except IndexError:
        pass
    
    
# print(session.schedule()[9].day)
