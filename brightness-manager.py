import sys, os
from tkinter import Tk ,Label
#from tkinter.ttk import Label

with open('/home/fox/Documents/Code/School-Python/brightness.txt', 'r+') as f:
    file = int(f.readline())
    f.seek(0)
    
        
    try:
        
        if  sys.argv[1] == "down" and file == 0:
            file = -15

        
        elif sys.argv[1] == "up" and file < 0:
            file = 0
        
        else:
            if sys.argv[1] == "down" and file >= 0 and file <= 100:
                file -= 5
            
            if sys.argv[1] == "up" and file >= 0 and file < 100:
                file += 5

        display = str(file) + '%'
        
        if file == 100:
            display = 'Max'
            
        elif file == 0:
            display = 'Min'
            
        elif file < 0:
            display = 'Dark'
            
        
        
        
        f.write(str(file))
        f.truncate()
        brightness = file

        window = Tk()

        window.geometry('110x25')
        
        #to have the brightness a little brighter
        brightness +=15
        brightness /= 100
        
        #change the brightness of the screen
        
        os.system('xrandr --output eDP-1 --brightness '+ str(brightness))    
        os.system('xrandr --output DP-1-0 --brightness '+ str(brightness))
        
        #borderless window
        
        #display the brightness
        Label(window, text=display, font=("Arial",37)).pack()
        #label = tk.Label(window, text = (f"{file}")).pack()
        window.after(500, window.destroy)
        
        #window.overrideredirect(True)
        window.mainloop()
    except IndexError:
        pass
    