import sys, os

with open('/home/fox/projects/brightness.txt', 'r+') as f:
    i = float(f.readline())
    f.seek(0)
    try:
        if sys.argv[1] == "down" and i >= 0.1 and i <= 1.0:
            i -= 0.1
        
        if sys.argv[1] == "up" and i >= 0.0 and i < 1.0: 
            i += 0.1
    except IndexError:
        pass
    f.write(str(i))
    f.truncate()
    
    os.system('xrandr --output eDP-1 --brightness '+ str(i))
    
    