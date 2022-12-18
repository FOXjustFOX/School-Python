from librus import LibrusSession
import sys, os


if sys.argv[1] == 'login':

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


    for i in range(len(lessons_plan)):
        g = lessons_plan[i]

        print(f'{weekdays[g.day + 1]}, {g.index}, {g.name}, {g.teacher}, {g.time}\n')

else:
    c = open('~/timetable.txt', 'r')
    o_c = open('~/old_timetable.txt', 'r')

    for i in range(len(c)):
        if c[i] != o_c[i]:
            msg = ""
            os.system(f'curl \
                    -H "Title: Zmiana w planie lekcji" \
                      -H "Priority: urgent" \
                      -H "Tags: warning" \
                      -d "{msg}" \
                      ntfy.sh/planlekcjiupdates')
