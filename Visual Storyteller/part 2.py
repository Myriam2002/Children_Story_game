from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
from playsound import playsound
import pygame
from tkinter import messagebox

window = Tk()
window.title('sweet dreams')
window.iconbitmap('icons8-crescent-moon-48.ico')
window.geometry("")
window.state('zoomed')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

mariam0=Frame(window,bg='#ffffff')
mariam1 = Frame(window,bg='#ffffff')
mariam2 = Frame(window,bg='#ffffff')
mariam3 = Frame(window,bg='#ffffff')
rana1 = Frame(window,bg='#ffffff')
rana2 = Frame(window,bg='#ffffff')
rana3 = Frame(window,bg='#ffffff')
samaa1 = Frame(window,bg='#A5D9F1')
samaa2 = Frame(window,bg='#ffffff')
samaa3 = Frame(window,bg='#16130C')

# # playing sounds through the program
# def play_music(sound, loop):
#     pygame.mixer.music.load(sound)
#     pygame.mixer.music.play(loops=loop)


# switching frames
def raise_frame(frame):
    frame.tkraise()



#=========loop============
for frame in (mariam0,mariam1,mariam2,mariam3,rana1,rana2,rana3,samaa1,samaa2,samaa3):
    frame.grid(row=0, column=0, sticky='nsew')


#==========Functions========
def show_frame(frame):
    """
    this makes the buttons get to a specific page
    """
    frame.tkraise()
def error():
    """
    this is the error message for clicking the a story that still didn't get uploaded
    """
    messagebox.showinfo('Sorry!', 'This story is still under construction')
#===========image buttons=====
forward=PhotoImage(file="forward.png")
backward=PhotoImage(file='backward.png')
play=PhotoImage(file='play.png')

x_back = 5
y_back = 385

x_next = 1180
y_next =  385

x_image = 125
y_image = 20

x_text = 160
y_text = 490
#==========mariam0=============
text=Label(mariam0,text="What story do you want to read?",font='Times 45 bold',bg='#ffffff').place(x=410,y=40)


story1=PhotoImage(file="ourstory.png")
story1_buttonH=Button(mariam0,image=story1,command=lambda: show_frame(mariam1),borderwidth=0)
story1_buttonH.place(x=90,y=160)
mariam1_back = Button(mariam0, text='back',command=lambda: show_frame(samaa2),image=backward)
mariam1_back.place(x=20,y=60)

story2=PhotoImage(file="soon.png")
story2_buttonH=Button(mariam0,image=story2,command=error,borderwidth=0)
story2_buttonH.place(x=356,y=160)

story3=PhotoImage(file="soon.png")
story3_buttonH=Button(mariam0,image=story2,command=error,borderwidth=0)
story3_buttonH.place(x=622,y=160)

story4=PhotoImage(file="soon.png")
story4_buttonH=Button(mariam0,image=story2,command=error,borderwidth=0)
story4_buttonH.place(x=888,y=160)

story4=PhotoImage(file="soon.png")
story4_buttonH=Button(mariam0,image=story2,command=error,borderwidth=0)
story4_buttonH.place(x=1154,y=426)


story5=PhotoImage(file="soon.png")
story5_buttonH=Button(mariam0,image=story2,command=error,borderwidth=0,)
story5_buttonH.place(x=90,y=426)


story6=PhotoImage(file="soon.png")
story6_buttonH=Button(mariam0,image=story2,command=error,borderwidth=0)
story6_buttonH.place(x=356,y=426)

story7=PhotoImage(file="soon.png")
story7_buttonH=Button(mariam0,image=story2,command=error,borderwidth=0)
story7_buttonH.place(x=622,y=426)

story8=PhotoImage(file="soon.png")
story8_buttonH=Button(mariam0,image=story2,command=error,borderwidth=0)
story8_buttonH.place(x=888,y=426)

story9=PhotoImage(file="soon.png")
story9_buttonH=Button(mariam0,image=story2,command=error,borderwidth=0)
story9_buttonH.place(x=1154,y=426)

story10=PhotoImage(file="soon.png")
story10_buttonH=Button(mariam0,image=story2,command=error,borderwidth=0)
story10_buttonH.place(x=1154,y=160)
#==========mariam1================
my_image1 = Image.open("art_ page_one.png")
my_image1 = my_image1.resize((1024,576), Image.ANTIALIAS)
my_image1 = ImageTk.PhotoImage(my_image1)
my_label1 = Label(mariam1, image=my_image1)
my_label1.place(x=x_image,y=y_image)
#text
mariam1_story = Label(mariam1,
                     text="Breathe in and breathe out...\n Let us thank God together for all his blessings.",font='Comic 30 bold')
mariam1_story.place(x=x_text,y=y_text)
mariam1_next = Button(mariam1, text='next',command=lambda: show_frame(mariam2),image=forward)
mariam1_next.place(x=x_next,y=y_next)
mariam1_back = Button(mariam1, text='back',command=lambda: show_frame(mariam0),image=backward)
mariam1_back.place(x=x_back,y=y_back)
PLAYING = Button(mariam1, text="Sound",command=lambda: playsound("page1.mp3"),image=play)
PLAYING.place(x=1,y=1)

#==========mariam2================
my_image2 = Image.open("Page2Art.png")
my_image2 = my_image2.resize((1024,576), Image.ANTIALIAS)
my_image2 = ImageTk.PhotoImage(my_image2)
my_label2 = Label(mariam2, image=my_image2)
my_label2.place(x=x_image,y=y_image)

mariam2_title = Label(mariam2,
                     text="Thank you God for my hands, legs, nose, mouth and eyes.\n  Thank you God for a brain "
                          "that keeps me learning. \n  (Give yourself a very big hug)\n  And promise yourself "
                          "that you will take care of you body.", font='Comic 25 bold ')
mariam2_title.place(x=x_text,y=y_text)
mariam2_btn = Button(mariam2, text='next', command=lambda: show_frame(mariam3),image=forward)
mariam2_btn.place(x=x_next,y=y_next)
frame1_back = Button(mariam2, text='back', command=lambda: show_frame(mariam1),image=backward)
frame1_back.place(x=x_back,y=y_back)
PLAYING = Button(mariam2, text="Sound",command=lambda: playsound("page2.mp3"),image=play)
PLAYING.grid()
#==========mariam3================
my_image3 = Image.open("healthpage.png")
my_image3 = my_image3.resize((1024,576), Image.ANTIALIAS)
my_image3 = ImageTk.PhotoImage(my_image3)
my_label3 = Label(mariam3, image=my_image3)
my_label3.place(x=x_image,y=y_image)
mariam3_title = Label(mariam3, text="By exercising , drinking water, \n And eating mighty superhero "
                                  "vegetables and fruits. ", font='Comic 30 bold',bg="#ffffff")
mariam3_title.place(x=x_text,y=y_text)
mariam3_btn = Button(mariam3, text='next', command=lambda: show_frame(rana1),image=forward)
mariam3_btn.place(x=x_next,y=y_next)
frame1_back = Button(mariam3, text='back', command=lambda: show_frame(mariam2),image=backward)
frame1_back.place(x=x_back,y=y_back)
PLAYING = Button(mariam3, text="play",command=lambda: playsound("page3.mp3"),image=play)
PLAYING.grid()
#==========rana1================
family=Image.open('famILYART.png')
family=family.resize((1024,576), Image.ANTIALIAS)
family=ImageTk.PhotoImage(family)
img_label0=Label(rana1,image=family)
img_label0.place(x=x_image,y=y_image)
#switching
rana1_btn = Button(rana1, text='next', command=lambda: show_frame(rana2),image=forward)
rana1_btn.place(x=x_next,y=y_next)
rana1_back = Button(rana1, text='back', command=lambda: show_frame(mariam3),image=backward)
rana1_back.place(x=x_back,y=y_back)
PLAYING = Button(rana1, text="play",command=lambda: playsound("page4.mp3"),image=play)
PLAYING.grid()

 #text
label_text=Label(rana1,text="Thank you God for my family, who give me so much love.",font='Comic 25 bold ')
label_text.place(x=x_text,y=y_text)
label_text2=Label(rana1,text="(go hug your family!)",font=('helvetica',15))
label_text2.place(x=x_text,y=y_text+50)
#==========rana2================
grateful=Image.open('grateful.png')
grateful=grateful.resize((1024,576), Image.ANTIALIAS)
grateful=ImageTk.PhotoImage(grateful)
img_label0=Label(rana2,image=grateful)
img_label0.place(x=x_image,y=y_image)

#switching
rana2_btn = Button(rana2, text='next', command=lambda: show_frame(rana3),image=forward)
rana2_btn.place(x=x_next,y=y_next)
rana2_back = Button(rana2, text='back', command=lambda: show_frame(rana1),image=backward)
rana2_back.place(x=x_back,y=y_back)
PLAYING = Button(rana2, text="play",command=lambda: playsound("page5.mp3"),image=play)
PLAYING.grid()

#text
text2_label=Label(rana2,text="Thank you God for all what I have. \nMy home, toys, food and clothes.", font='Comic 30 bold ', bg="#ffffff")
text2_label.place(x=x_text,y=y_text)
#==========rana3================
life=Image.open('lastpageART.png')
life=life.resize((1024,576), Image.ANTIALIAS)
life=ImageTk.PhotoImage(life)
img_label0=Label(rana3,image=life)
img_label0.place(x=x_image,y=y_image)
#switching pages
rana3_btn = Button(rana3, text='next', command=lambda: show_frame(samaa1),image=forward)
rana3_btn.place(x=x_next,y=y_next)
rana3_back = Button(rana3, text='back', command=lambda: show_frame(rana2),image=backward)
rana3_back.place(x=x_back,y=y_back)
PLAYING = Button(rana3, text="play",command=lambda: playsound("page6.mp3"),image=play)
PLAYING.grid()

#text
text3_label=Label(rana3,text="Thank you God for always being with me, wherever I am.\nThank you God for giving me the gift of life.",font='Comic 30 bold',bg='#ffffff')
text3_label.place(x=x_text,y=y_text)
#==========samaa1================
samaa1_forward=Button(samaa1,text='Next',command=lambda:show_frame(samaa2),image=forward)
samaa1_forward.place(x=x_next,y=y_next)
samaa1_back = Button(samaa1, text='back', command=lambda: show_frame(rana3),image=backward)
samaa1_back.place(x=x_back,y=y_back)
clapping=PhotoImage(file='clap1.png')
PLAYING = Button(samaa1, text="play",command=lambda: playsound("Clapping Sound Effects.mp3"),image=clapping)
PLAYING.grid()

samaa1_image=Image.open('trophy1.png')
samaa1_image=samaa1_image.resize((750,750), Image.ANTIALIAS)
samaa1_image=ImageTk.PhotoImage(samaa1_image)
img_label0=Label(samaa1,image=samaa1_image,borderwidth=0, highlightthickness=0,padx=0,pady=0)
img_label0.place(x=400,y=0)

# insert text
my_text= Label(samaa1, text="EXCELLENT WORK!", font='Playfair 35 bold ', fg="white", relief="flat", bg="#DD4F55", width=25, height=2)   #replace (name)with name_entry.get()
my_text.place(x=435, y=650)

#==========samaa2================


#background image
bg2=PhotoImage(file='colour.png')

#label 2
my_label2=Label(samaa2, image=bg2 )
my_label2.place(x=20, y=20, relwidth=1, relheight=1)
#inset text
my_text= Label(samaa2, text="What do you think of the story?", font='Playfair 40 bold ', fg="#696969", relief="flat", bg="white")
my_text.place(x=370, y=100)
samaa2_forward=Button(samaa2,text='Next',command=lambda:show_frame(samaa3),image=forward)
samaa2_forward.place(x=x_next,y=y_next)
samaa2_back = Button(samaa2, text='back', command=lambda: show_frame(samaa1),image=backward)
samaa2_back.place(x=x_back,y=y_back)

sad=PhotoImage(file="bad.png")
sad_buttonH=Button(samaa2,image=sad,command=lambda: playsound("boring.mp3"),borderwidth=0)
sad_buttonH.place(x=350,y=250)


love=PhotoImage(file="love2.png")
love_buttonS=Button(samaa2,image=love,command=lambda: playsound("I love it.mp3"),borderwidth=0)
love_buttonS.place(x=860,y=250)


happy=PhotoImage(file="smile.png")
happy_button2=Button(samaa2,image=happy,command=lambda: playsound("nice.mp3"),borderwidth=0)
happy_button2.place(x=600,y=250)

#==========samaa3================

#setting the backgroud image

end=Image.open('baby moon and clouds.png')
end=end.resize((660,510), Image.ANTIALIAS)
end=ImageTk.PhotoImage(end)
img_label0=Label(samaa3,image=end,borderwidth=0, highlightthickness=0,padx=0,pady=0)
img_label0.place(x=300,y=100)

 #adding text

samaa3_forward=Button(samaa3,text='Next',command=lambda:show_frame(mariam1),image=forward)
samaa3_forward.place(x=x_next,y=y_next)
samaa3_back = Button(samaa3, text='back', command=lambda: show_frame(samaa2),image=backward)
samaa3_back.place(x=x_back,y=y_back)

#=======end code===========
window.mainloop()