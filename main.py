import tkinter
from tkinter import ttk
from tkinter import Canvas
from tkinter import *
from PIL import ImageTk, Image

import sv_ttk

root = tkinter.Tk()
root.geometry("1900x900")

C = Canvas(root, bg="white", height=700, width=1900)

image = Image.open("concavetwo.png")
concave_image = ImageTk.PhotoImage(image)
C.create_image(950,350,image=concave_image)

C.create_line(0,361, 1900,361, tags="line", fill="black", width=7) # pirincple plane


################################################


fl_label = ttk.Label(root, text="Focal Length")
fl_input = Text(root, height = 2, width =8)


fl_label.place(relx=0.02, rely=0.87, anchor="sw")
fl_input.place(relx=0.025, rely=0.91, anchor="sw")


##########################################################

# top of line is at y = 358




od_label = Label(root, text="Object Distance")
od_input = Text(root, height=2, width=8)

od_label.place(relx=0.2, rely=0.87, anchor="s")
od_input.place(relx=0.2, rely=0.91, anchor="s")

####################################


oh_label = Label(root, text="Object Height")
oh_input = Text(root, height=2, width=8)

oh_label.place(relx=0.34, rely=0.87, anchor="s")
oh_input.place(relx=0.34, rely=0.91, anchor="s")






#####################################

def calculate():
    object_distance = int(od_input.get("1.0",END))
    focal_length = int(fl_input.get("1.0",END))
    object_height = int(oh_input.get("1.0",END))
    center = focal_length * 2
    
    image_distance = (1 / ((1/focal_length) - (1/object_distance)))
    magnification = (-1 * image_distance) / (object_distance)
    image_height = magnification * object_height

#C.create_line(100,358, 100, 200, tags="line", fill="blue", width=2 )
    
    print("image distance" + str(image_distance))
    print("magnification : " + str(magnification))
    print("image height : " + str(image_height))


    C.create_line((450-(object_distance*10)), 358, (450-(object_distance*10)), (358-(object_height*10)), tags="line", fill="black", width=5 ) # object

    C.create_line((450+(image_distance*10)), 358, (450+(image_distance*10)), (358+(image_height*10)), tags="line", fill="black", width=5 ) # image

    



    C.create_line((450-(object_distance*10)) , (358-(object_height*10)) , 953,(358-(object_height*10)) , tags="line", fill="red", width=1.5) # first line

    C.create_line( 953,(358-(object_height*10)) , (450+(image_distance*10)), (358+(image_height*10)) , tags="line", fill="red", width=1.5) # second line
    
    C.create_line(953, (358-(object_height*10)), (950-(focal_length*10)), 358, tags="line", fill="red", width=1.5) # line back to focal point

    


calc_button = Button(root, height=2, width=8, text="Calculate", command=lambda:calculate())
calc_button.place(relx=0.5, rely=0.92, anchor="s")







####################################

C.pack()

######################################




####################################

sv_ttk.set_theme("dark")
root.mainloop()
