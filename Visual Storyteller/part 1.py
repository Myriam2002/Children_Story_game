from tkinter import *
from PIL import ImageTk, Image
import pygame
import time
import threading
from tkinter import messagebox


def play(sound, loop):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=loop)


def raise_frame(frame):
    frame.tkraise()


window = Tk()
window.geometry("700x500+400+150")
window.title("storyteller")
window.iconbitmap("crescent.ico")

pygame.mixer.init()
play("lullaby.mp3", 6)

f1 = Frame(window)
f2 = Frame(window)
f3 = Frame(window)


for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')

# creating canvases
c1 = Canvas(f1, width=700, height=500, bd=-2, bg="light blue")
c1.pack()
c2 = Canvas(f2, width=700, height=500, bd=-2, bg="light blue")
c2.pack()
c3 = Canvas(f3, width=700, height=500, bd=-2, bg="light blue")
c3.pack()

# defining images then adding them to the canvas
stars_img = Image.open("stars1.png")
stars_img = stars_img.resize((700, 350), Image.ANTIALIAS)
stars_img = ImageTk.PhotoImage(stars_img)
c1.create_image(350, 340, image=stars_img)
c1.create_image(350, -18, image=stars_img)

moon_img = Image.open("moon.png")
moon_img = moon_img.resize((200, 200), Image.ANTIALIAS)
moon_img = ImageTk.PhotoImage(moon_img)
c1.create_image(120, 390, image=moon_img)

baby_img = Image.open("baby.png")
baby_img = baby_img.resize((175, 140), Image.ANTIALIAS)
baby_img = ImageTk.PhotoImage(baby_img)
c1.create_image(600, 95, image=baby_img)

go_img = Image.open("cloud.png")
go_img = go_img.resize((150, 110), Image.ANTIALIAS)
go_img = ImageTk.PhotoImage(go_img)
go_btn = Button(f1, image=go_img, borderwidth=0, bg="light blue")


farm_img = Image.open("farm.png")
farm_img = farm_img.resize((700, 480), Image.ANTIALIAS)
farm_img = ImageTk.PhotoImage(farm_img)
c3.create_image(350, 260, image=farm_img)


start_img = Image.open("start.png")
start_img = start_img.resize((150, 60), Image.ANTIALIAS)
start_img = ImageTk.PhotoImage(start_img)


# adding text
c3.create_text(450, 100, text="As you wish, little lamb", font="times 25 bold italic", fill="#8a5938")
c3.create_text(450, 150, text="Let's count sheeps together", font="times 20 bold italic", fill="#8a5938")

c1.create_text(200, 50, text="Hello, Little One!", font="times 38 bold italic", fill="brown")
c1.create_text(145, 140, text="What is your Name?", font="times 24 bold italic", fill="brown")

# input for child's name
name_entry = Entry(f1, font="times 18", width=10, fg="#f98b88")
c1.create_window(360, 140, window=name_entry)


def yes_btn_click(event):
    pass


def no_btn_click(event):
    raise_frame(f3)


def go_btn_click(event):
    c1.delete("all")

    # defining images then adding them to the canvas
    global dangling_img
    dangling_img = Image.open("dangling stars.png")
    dangling_img = dangling_img.resize((400, 200), Image.ANTIALIAS)
    dangling_img = ImageTk.PhotoImage(dangling_img)
    c1.create_image(200, 260, image=dangling_img)
    c1.create_image(580, 260, image=dangling_img)

    global clouds_img
    clouds_img = Image.open("clouds.png")
    clouds_img = clouds_img.resize((700, 200), Image.ANTIALIAS)
    clouds_img = ImageTk.PhotoImage(clouds_img)
    c1.create_image(350, 180, image=clouds_img)
    c1.create_image(350, 90, image=clouds_img)

    c1.create_text(350, 90,
                   text="Does little " + name_entry.get() + " want to hear a bedtime story?",
                   font="times 25 bold italic",
                   fill="#CD853F")

    # defining an image and making the button in the shape of it
    global yes_img
    yes_img = Image.open("yes.png")
    yes_img = yes_img.resize((240, 120), Image.ANTIALIAS)
    yes_img = ImageTk.PhotoImage(yes_img)
    yes_btn = Button(f1, image=yes_img, borderwidth=0, bg="light blue")
    yes_btn.bind("<Button-1>", yes_btn_click)
    c1.create_window(200, 420, window=yes_btn)

    global no_img
    no_img = Image.open("no.png")
    no_img = no_img.resize((90, 135), Image.ANTIALIAS)
    no_img = ImageTk.PhotoImage(no_img)
    no_btn = Button(f1, image=no_img, borderwidth=0, bg="light blue")
    no_btn.bind("<Button-1>", no_btn_click)
    c1.create_window(500, 420, window=no_btn)


go_btn.bind("<Button-1>", go_btn_click)
c1.create_window(360, 275, window=go_btn)


arrow_img = Image.open("arrow.png")
arrow_img = arrow_img.resize((65, 40), Image.ANTIALIAS)
arrow_img = ImageTk.PhotoImage(arrow_img)


def arrow_btn_click(event):
    play("lullaby.mp3", 6)
    raise_frame(f1)


arrow_btn = Button(f3, image=arrow_img, borderwidth=0, bg="light blue")
c3.create_window(30, 25, window=arrow_btn)
arrow_btn.bind("<Button-1>", arrow_btn_click)


# counting sheep page
def start_btn_click(event):
    window2 = Toplevel()
    window2.geometry("700x500+400+150")
    f4 = Frame(window2)
    f4.grid(row=0, column=0, sticky='news')
    c4 = Canvas(f4, width=700, height=500, bd=-2, bg="light blue")
    c4.grid()
    count = Label(f4, text=0, font="times 45 bold italic", bg="light blue")
    count.place(x=345, y=70)
    count["text"] = -1
    play("numbers.mp3", 0)

    global garden_img
    garden_img = Image.open("garden.png")
    garden_img = garden_img.resize((700, 480), Image.ANTIALIAS)
    garden_img = ImageTk.PhotoImage(garden_img)
    c4.create_image(350, 260, image=garden_img)

    global sheep_img
    sheep_img = Image.open("sheep.png")
    sheep_img = sheep_img.resize((170, 170), Image.ANTIALIAS)
    sheep_img = ImageTk.PhotoImage(sheep_img)
    sheep_image = c4.create_image(700, 400, image=sheep_img)

    global exit_img
    exit_img = Image.open("exit.png")
    exit_img = exit_img.resize((150, 150), Image.ANTIALIAS)
    exit_img = ImageTk.PhotoImage(exit_img)

    def change_count():
        count.config(text=count["text"] + 1)
        count.after(2000, change_count)
        if count["text"] > 100:
            count.destroy()
            c4.create_text(345, 70,
                           text="sleep tight little " + name_entry.get(),
                           font="times 45 bold italic",
                           fill="brown")

    def move_sheep():
        while True:
            coordinates = c4.coords(sheep_image)
            c4.move(sheep_image, -5, 0)
            window.update()
            time.sleep(0.01)
            if 200 < coordinates[0] < 400:
                c4.move(sheep_image, -5, 8)
            elif 400 < coordinates[0] < 600:
                c4.move(sheep_image, -5, -8)
            elif coordinates[0] <= -100:
                c4.move(sheep_image, 900, 0)
            if count["text"] > 100:
                break

    def exit_sheep(event):
        pygame.mixer.music.stop()
        window2.destroy()

    exit_btn = Button(f4,
                       image=exit_img,
                       borderwidth=0,
                       bg="light blue")
    exit_btn.bind("<Button-1>", exit_sheep)
    c4.create_window(75, 50, window=exit_btn)

    def on_close_sheep():
        pygame.mixer.music.stop()
        window2.destroy()

    window2.protocol("WM_DELETE_WINDOW", on_close_sheep)

    # removes lag
    t1 = threading.Thread(target=change_count)
    t1.setDaemon(True)
    t1.start()

    t2 = threading.Thread(target=move_sheep)
    t2.setDaemon(True)
    t2.start()


start_btn = Button(f3,
                   image=start_img,
                   borderwidth=0,
                   bg="#8ba81c",)
start_btn.bind("<Button-1>", start_btn_click)
c3.create_window(325, 435, window=start_btn)


def on_close():
    close = messagebox.askokcancel("Quit", "Do you want to leave?")
    if close:
        pygame.mixer.music.stop()
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_close)

window.mainloop()