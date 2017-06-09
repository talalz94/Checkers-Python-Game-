

from tkinter import *                                                                         #Tkinter is used as the GUI.
from tkinter import messagebox
import sys
import os


def board():

    Label(image=logo3, width=570, height=568).place(x=219, y=52)                               #This function draws the board using nested loops
                                                                                               #Block by Block.
    x = 0
    y = 0
    c = 0
    while x < 480:
        while y < 480:

            if (c % 2 == 0):
                if (y<180):
                    Label(image=logo4, width=60, height=60).place(x=250 + x, y=85 + y)

                elif (y>300):
                    Label(image=logo5, width=60, height=60).place(x=250 + x, y=85 + y)

                else:

                    Label(image=logo, width=60, height=60).place(x=250 + x, y=85 + y)

            else:

                Label(image=logo2, width=60, height=60).place(x=250 + x, y=85 + y)

            y = y + 64
            c = c + 1
        x = x + 64
        c = c + 1
        y = 0

# def center(toplevel):
#
#     toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


def players():                                                                              #This function gets the name of 2 players by
                                                                                            #opening a dialog box where they can write them.
    def Pnames():
        pname1 = name.get()[0:10]
        pname2 = name2.get()[0:10]
        labelfont = ('times', 28, 'bold')
        Label(root, text=pname1, fg='RED',background="BLACK",font=labelfont).place(x=50,y=0)
        Label(root,text="Vs", fg="WHITE",bg="BLACK", font=labelfont).place(x=482,y=0)
        Label(root, text=pname2, fg='GRAY',background="BLACK",font=labelfont).place(x=850,y=0)
        messagebox.showinfo(title="Checkers",message="Black goes first")
        names.destroy()
        return


    name=StringVar()
    name2=StringVar()
    names = Toplevel(root)
    names.resizable(width=False, height=False)
    names.geometry('265x115')
    names.attributes("-topmost",True)
    L1 = Label(names, text="Enter Name Player 1: ", fg='RED')
    L1.place(x=5,y=10)
    L2 = Label(names, text="Enter Name Player 2: ",fg='GRAY')
    L2.place(x=5,y=35)
    E1 = Entry(names, textvariable=name)
    E1.place(x=125,y=10)
    E2 = Entry(names, textvariable=name2)
    E2.place(x=125, y=35)

    button = Button(names, text="   Enter   ", command = Pnames )                                 #Pnames is called to show the names on the screen.
    button.place(x=100,y=75)




# game start
root = Tk()


root.resizable(width=False, height=False)                                                      #The window size of the game.
root.geometry('1000x650')
root.configure(background='black')
root.title("Checkers")



#Top menu bar
menubar = Menu(root)                                                                     #This will create a menubar.
filemenu = Menu(menubar, tearoff=0)


filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
#Top menu bar end

logo = PhotoImage(file="white2.gif")                                                     #Loading all the image files that are required in the game.
logo2 = PhotoImage(file="brown2.gif")
logo3 = PhotoImage(file="board test.gif")
logo4 = PhotoImage(file="whiteg.gif")
logo5 = PhotoImage(file="browng.gif")
logos = PhotoImage(file="whitegs.gif")
logobs = PhotoImage(file="browngs.gif")
logork = PhotoImage(file="whitek.gif")
logobk = PhotoImage(file="Brownk.gif")

players()
board()                                                                              #These functions loads the game board and the name entry screen.


#intializing all the global variables
Rx0 = [250, 378, 506, 634,  314, 442, 570, 698,  250, 378, 506, 634]
Rx = [314, 442, 570, 698,  378, 506, 634, 762,  314, 442, 570, 698]  #red blocks cordinates.
Ry0 = [85, 85, 85, 85,  149, 149, 149, 149,  213, 213, 213, 213]
Ry = [149, 149, 149, 149,  213, 213, 213, 213,  277, 277, 277, 277]

Rkx0 = []
Rkx = []  #red king blocks cordinates.
Rky0 = []
Rky = []

Bx0 = [314, 442, 570, 698,  250, 378, 506, 634,  314, 442, 570, 698]
Bx = [378, 506, 634, 762,  314, 442, 570, 698,  378, 506, 634, 762]  #Black blocks cordinates.
By0 = [405, 405, 405, 405,  469, 469, 469, 469,  533, 533, 533, 533]
By = [469, 469, 469, 469,  533, 533, 533, 533,  597, 597, 597, 597]

Bkx0 = []
Bkx = []  #Black king blocks cordinates.
Bky0 = []
Bky = []

Lrx0=[314, 442, 570, 698] #Red King condition cordinates.
Lry0=533

Lbx0=[250, 378, 506, 634] #Red King condition cordinates.
Lby0=85


Fbx0 = [314, 442, 570, 698,  250, 378, 506, 634]
Fbx = [378, 506, 634, 762,  314, 442, 570, 698]  #free blocks cordinates.
Fby0 = [277, 277, 277, 277,  341, 341, 341, 341]
Fby = [341, 341, 341, 341,  405, 405, 405, 405]



select = False
kk=0
black = True
killed = False
king = False
killer = False
kingkiller = False
kill =0
kingmade = False
kingbmade = False



def listadd(i):                                                       #This function updates the lists for all the blocks depending on the move
                                                                      #the player made. This checks if the turn was of red player, and then
    if black == False:                                                #whether a king was played or not.

        if (king == True):
            Rkx.append(Fbx[i]);
            Rkx0.append(Fbx0[i]);
            Rky.append(Fby[i]);
            Rky0.append(Fby0[i]);

            Fbx.append(lastx);
            Fbx0.append(lastx0);
            Fby.append(lasty);
            Fby0.append(lasty0);

            del Rkx0[kk]  # red
            del Rkx[kk]
            del Rky0[kk]  # red
            del Rky[kk]

            del Fbx0[i]  # free
            del Fbx[i]
            del Fby0[i]  # free
            del Fby[i]

            return

        else:


            Rx.append(Fbx[i]);
            Rx0.append(Fbx0[i]);
            Ry.append(Fby[i]);
            Ry0.append(Fby0[i]);

            Fbx.append(lastx);
            Fbx0.append(lastx0);
            Fby.append(lasty);
            Fby0.append(lasty0);

            del Fbx0[i]  # free
            del Fbx[i]
            del Fby0[i]  # free
            del Fby[i]

            del Rx0[k]  # red
            del Rx[k]
            del Ry0[k]  # red
            del Ry[k]

            return

    elif (black == True):                                         #Similarly lists are updated for the black player.

        if (king == True):
            Bkx.append(Fbx[i]);
            Bkx0.append(Fbx0[i]);
            Bky.append(Fby[i]);
            Bky0.append(Fby0[i]);

            Fbx.append(lastx);
            Fbx0.append(lastx0);
            Fby.append(lasty);
            Fby0.append(lasty0);

            del Bkx0[kk]  # red
            del Bkx[kk]
            del Bky0[kk]  # red
            del Bky[kk]

            del Fbx0[i]  # free
            del Fbx[i]
            del Fby0[i]  # free
            del Fby[i]

            return

        else:


            Bx.append(Fbx[i]);
            Bx0.append(Fbx0[i]);
            By.append(Fby[i]);
            By0.append(Fby0[i]);

            Fbx.append(lastx);
            Fbx0.append(lastx0);
            Fby.append(lasty);
            Fby0.append(lasty0);

            del Fbx0[i]  # free
            del Fbx[i]
            del Fby0[i]  # free
            del Fby[i]

            del Bx0[k]  # red
            del Bx[k]
            del By0[k]  # red
            del By[k]

            return


def move(killed, killer, select, black, i, k, ffx,x,y,king,kingkiller):  #This functions moves the game pieces according to the move.


    if black == False:                                                  #Here it checks for the red player. Then it checks whether a kill was made.
                                                                        #Accordingly the loop traverses through possible kill moves and if a suitable
        if (killed == True):                                            #move is found, it moves the images of game pieces to move them on board.
            if (king == False):

                for bb in range (len(Bx0)):
                    if ((x < (lastx + 124) and x >= (lastx0 + 124) and y >= (lasty0 + 124) and y < (lasty + 124) and
                        ((lastx0+64 == Bx0[bb]) and (lasty0 + 64 == By0[bb]))) or ((x < (lastx - 124) and x >= (lastx0 - 124)
                         and y >= (lasty0 + 124) and y < (lasty + 124)) and ((lastx0-64 == Bx0[bb]) and (lasty0 + 64 == By0[bb])))):

                        Label(image=logo4, width=60, height=60).place(x=Fbx0[i], y=Fby0[i])
                        Label(image=logo, width=60, height=60).place(x=lastx0, y=lasty0)
                        Label(image=logo, width=60, height=60).place(x=(Fbx0[i] + lastx0) / 2, y=(Fby0[i] + lasty0) / 2)

                        Rx.append(Fbx[i]);
                        Rx0.append(Fbx0[i]);
                        Ry.append(Fby[i]);
                        Ry0.append(Fby0[i]);

                        Fbx.append(lastx);                                      #The lists are updates according to the move.
                        Fbx0.append(lastx0);
                        Fby.append(lasty);
                        Fby0.append(lasty0);

                        Fbx.append((Fbx[i] + lastx) / 2);
                        Fbx0.append((Fbx0[i] + lastx0) / 2);
                        Fby.append((Fby[i] + lasty) / 2);
                        Fby0.append((Fby0[i] + lasty0) / 2);


                        del Fbx0[i]  # free
                        del Fbx[i]
                        del Fby0[i]  # free
                        del Fby[i]

                        del Bx0[ffx]  # free
                        del Bx[ffx]
                        del By0[ffx]  # free
                        del By[ffx]

                        del Rx0[k]  # red
                        del Rx[k]
                        del Ry0[k]  # red
                        del Ry[k]

                        killer=True
                        return killer

            elif(king == True):                                    #Similarly this condition is for the king.
                for bb in range(len(Bx0)):
                    if (((x < (lastx + 124) and x >= (lastx0 + 124) and y >= (lasty0 + 124) and y < (lasty + 124) and (
                        (lastx0+64 == Bx0[bb]) and (lasty0 + 64 == By0[bb]))) or ((x < (lastx - 124) and x >= (lastx0 - 124)
                        and y >= (lasty0 + 124) and y < (lasty + 124)) and ((lastx0-64 == Bx0[bb]) and
                        (lasty0 + 64 == By0[bb])))) or ((x < (lastx + 124) and x >= (lastx0 + 124) and y >= (lasty0 - 124) and y < (lasty - 124) and (
                        (lastx0+64 == Bx0[bb]) and (lasty0 - 64 == By0[bb]))) or ((x < (lastx - 124) and x >= (lastx0 - 124)
                        and y >= (lasty0 - 124) and y < (lasty - 124)) and ((lastx0-64 == Bx0[bb]) and
                        (lasty0 - 64 == By0[bb]))))) :

                        Label(image=logork, width=60, height=60).place(x=Fbx0[i], y=Fby0[i])
                        Label(image=logo, width=60, height=60).place(x=lastx0, y=lasty0)
                        Label(image=logo, width=60, height=60).place(x=(Fbx0[i] + lastx0) / 2, y=(Fby0[i] + lasty0) / 2)

                        Rkx.append(Fbx[i]);
                        Rkx0.append(Fbx0[i]);
                        Rky.append(Fby[i]);
                        Rky0.append(Fby0[i]);

                        Fbx.append(lastx);
                        Fbx0.append(lastx0);
                        Fby.append(lasty);
                        Fby0.append(lasty0);

                        Fbx.append((Fbx[i] + lastx) / 2);
                        Fbx0.append((Fbx0[i] + lastx0) / 2);
                        Fby.append((Fby[i] + lasty) / 2);
                        Fby0.append((Fby0[i] + lasty0) / 2);                #Lists are updated for the king's move.

                        del Fbx0[i]  # free
                        del Fbx[i]
                        del Fby0[i]  # free
                        del Fby[i]

                        del Bx0[ffx]  # free
                        del Bx[ffx]
                        del By0[ffx]  # free
                        del By[ffx]

                        del Rkx0[k]  # red
                        del Rkx[k]
                        del Rky0[k]  # red
                        del Rky[k]

                        kingkiller = True
                        return kingkiller


        else:                                                         #These two conditions are for the non-kill moves.

            if (king == True):
                if (((x < (lastx + 64) and x >= (lastx0 + 64) and y >= (lasty0 + 64) and y < (lasty + 64)) or
                    ( x < (lastx - 64) and x >= (lastx0 - 64) and y >= (lasty0 + 64) and y < (lasty + 64))) or
                    ((x < (lastx + 64) and x >= (lastx0 + 64) and y >= (lasty0 - 64) and y < (lasty - 64)) or
                    ( x < (lastx - 64) and x >= (lastx0 - 64) and y >= (lasty0 - 64) and y < (lasty - 64)))) :
                    Label(image=logork, width=60, height=60).place(x=Fbx0[i], y=Fby0[i])
                    Label(image=logo, width=60, height=60).place(x=lastx0, y=lasty0)
                    killer = False
                    listadd(i)
                    return kingkiller


            elif(king == False):
                if ((x < (lastx + 64) and x >= (lastx0 + 64) and y >= (lasty0 + 64) and y < (lasty + 64)) or
                    ( x < (lastx - 64) and x >= (lastx0 - 64) and y >= (lasty0 + 64) and y < (lasty + 64))):
                    Label(image=logo4, width=60, height=60).place(x=Fbx0[i], y=Fby0[i])
                    Label(image=logo, width=60, height=60).place(x=lastx0, y=lasty0)
                    killer = False
                    listadd(i)
                    return killer


    elif black == True:                                                     #Here it checks for the Black player. Then it checks whether a kill was made.
                                                                            #Accordingly the loop traverses through possible kill moves and if a suitable
                                                                            #move is found, it moves the images of game pieces to move them on board.
        if (killed == True):
            if (king == False):

                for bb in range(len(Rx0)):
                    if ((x < (lastx + 124) and x >= (lastx0 + 124) and y >= (lasty0 - 124) and y < (lasty - 124) and
                        ((lastx0 + 64 == Rx0[bb]) and (lasty0 - 64 == Ry0[bb]))) or (
                        (x < (lastx - 124) and x >= (lastx0 - 124) and y >= (lasty0 - 124) and y < (lasty - 124)) and (
                        (lastx0 - 64 == Rx0[bb]) and (lasty0 - 64 == Ry0[bb])))):

                        Label(image=logo5, width=60, height=60).place(x=Fbx0[i], y=Fby0[i])
                        Label(image=logo, width=60, height=60).place(x=lastx0, y=lasty0)
                        Label(image=logo, width=60, height=60).place(x=(Fbx0[i] + lastx0) / 2, y=(Fby0[i] + lasty0) / 2)

                        Bx.append(Fbx[i]);
                        Bx0.append(Fbx0[i]);
                        By.append(Fby[i]);
                        By0.append(Fby0[i]);

                        Fbx.append(lastx);
                        Fbx0.append(lastx0);
                        Fby.append(lasty);
                        Fby0.append(lasty0);

                        Fbx.append((Fbx[i] + lastx) / 2);
                        Fbx0.append((Fbx0[i] + lastx0) / 2);
                        Fby.append((Fby[i] + lasty) / 2);
                        Fby0.append((Fby0[i] + lasty0) / 2);                      #List for black player is updated.

                        del Fbx0[i]  # free
                        del Fbx[i]
                        del Fby0[i]  # free
                        del Fby[i]

                        del Rx0[ffx]  # free
                        del Rx[ffx]
                        del Ry0[ffx]  # free
                        del Ry[ffx]

                        del Bx0[k]  # red
                        del Bx[k]
                        del By0[k]  # red
                        del By[k]

                        killer = True
                        return killer

            elif (king == True):                             #This case is for king's killing move for the Black player.
                for bb in range(len(Rx0)):
                    if (((x < (lastx + 124) and x >= (lastx0 + 124) and y >= (lasty0 + 124) and y < (lasty + 124) and (
                        (lastx0 + 64 == Rx0[bb]) and (lasty0 + 64 == Ry0[bb]))) or ((x < (lastx - 124) and
                        x >= (lastx0 - 124) and y >= (lasty0 + 124) and y < (lasty + 124)) and ((lastx0 - 64 == Rx0[bb])
                        and(lasty0 + 64 == Ry0[bb])))) or ((x < (lastx + 124) and x >= (lastx0 + 124) and y >=
                        (lasty0 - 124) and y < (lasty - 124) and ((lastx0 + 64 == Rx0[bb]) and (lasty0 - 64 == Ry0[bb]))
                        ) or ((x < (lastx - 124) and x >= (lastx0 - 124) and y >= (lasty0 - 124) and y < (lasty - 124))
                        and ((lastx0 - 64 == Rx0[bb]) and (lasty0 - 64 == Ry0[bb]))))):

                        Label(image=logobk, width=60, height=60).place(x=Fbx0[i], y=Fby0[i])
                        Label(image=logo, width=60, height=60).place(x=lastx0, y=lasty0)
                        Label(image=logo, width=60, height=60).place(x=(Fbx0[i] + lastx0) / 2, y=(Fby0[i] + lasty0) / 2)

                        Bkx.append(Fbx[i]);
                        Bkx0.append(Fbx0[i]);
                        Bky.append(Fby[i]);
                        Bky0.append(Fby0[i]);                                  #The code checks for diagonal viable moves.
                                                                               #if a permissible move is found, it updates the images for those
                        Fbx.append(lastx);                                     #co-ordinates where the mouse was clicked.
                        Fbx0.append(lastx0);
                        Fby.append(lasty);
                        Fby0.append(lasty0);

                        Fbx.append((Fbx[i] + lastx) / 2);
                        Fbx0.append((Fbx0[i] + lastx0) / 2);
                        Fby.append((Fby[i] + lasty) / 2);
                        Fby0.append((Fby0[i] + lasty0) / 2);

                        del Fbx0[i]  # free
                        del Fbx[i]
                        del Fby0[i]  # free
                        del Fby[i]

                        del Rx0[ffx]  # free
                        del Rx[ffx]
                        del Ry0[ffx]  # free
                        del Ry[ffx]

                        del Bkx0[k]  # red
                        del Bkx[k]
                        del Bky0[k]  # red
                        del Bky[k]

                        kingkiller = True
                        return kingkiller


        else:                             #These two conditions works for non-kill king moves.

            if (king == True):

                if (((x < (lastx + 64) and x >= (lastx0 + 64) and y >= (lasty0 + 64) and y < (lasty + 64)) or (
                    x < (lastx - 64) and x >= (lastx0 - 64) and y >= (lasty0 + 64) and y < (lasty + 64))) or (
                    (x < (lastx + 64) and x >= (lastx0 + 64) and y >= (lasty0 - 64) and y < (lasty - 64)) or (
                    x < (lastx - 64) and x >= (lastx0 - 64) and y >= (lasty0 - 64) and y < (lasty - 64)))):

                    Label(image=logobk, width=60, height=60).place(x=Fbx0[i], y=Fby0[i])
                    Label(image=logo, width=60, height=60).place(x=lastx0, y=lasty0)

                    killer = False
                    listadd(i)
                    return kingkiller


            elif (king == False):

                if ((x < (lastx + 64) and x >= (lastx0 + 64) and y >= (lasty0 - 64) and y < (lasty - 64)) or (
                    x < (lastx - 64) and x >= (lastx0 - 64) and y >= (lasty0 - 64) and y < (lasty - 64))):
                    Label(image=logo5, width=60, height=60).place(x=Fbx0[i], y=Fby0[i])
                    Label(image=logo, width=60, height=60).place(x=lastx0, y=lasty0)
                    killer = False
                    listadd(i)
                    return killer


def canKill(a,b):                                #This function checks whether a kill is available to the player or not.
                                                #so a killing move is prioritized.
    if black == False:

        for ji in range(len(Fbx0)):
            for li in range(len(Bx0)):
                for ii in range(a,b):
                    if (((((Rx0[ii] - 64) == Bx0[li]) and ((Ry0[ii] + 64) == By0[li])) and (
                        ((Rx0[ii] - 128) == Fbx0[ji]) and ((Ry0[ii] + 128) == Fby0[ji]))) or (
                        (((Rx0[ii] + 64) == Bx0[li]) and ((Ry0[ii] + 64) == By0[li])) and (
                        ((Rx0[ii] + 128) == Fbx0[ji]) and ((Ry0[ii] + 128) == Fby0[ji])))):

                        return True
        return False

    else:                                      #This ones for black player.

        for ji in range(len(Fbx0)):
            for li in range(len(Rx0)):
                for ii in range(a, b):
                    if (((((Bx0[ii] - 64) == Rx0[li]) and ((By0[ii] - 64) == Ry0[li])) and (
                        ((Bx0[ii] - 128) == Fbx0[ji]) and ((By0[ii] - 128) == Fby0[ji]))) or (
                        (((Bx0[ii] + 64) == Rx0[li]) and ((By0[ii] - 64) == Ry0[li])) and (
                        (Bx0[ii] + 128) == Fbx0[ji]) and ((By0[ii] - 128) == Fby0[ji]))):

                        return True
        return False


def canKingKill(a,b):                            #This function checks whether a king can make a killing make to prioritze that over
                                                #any other non-killing move.
    if black == False:

        for ji in range(len(Fbx0)):
            for li in range(len(Bx0)):
                for iik in range(a,b):

                            if ((((((Rkx0[iik] - 64) == Bx0[li]) and ((Rky0[iik] + 64) == By0[li])) and (
                                ((Rkx0[iik] - 128) == Fbx0[ji]) and ((Rky0[iik] + 128) == Fby0[ji]))) or (
                                (((Rkx0[iik] + 64) == Bx0[li]) and ((Rky0[iik] + 64) == By0[li])) and (
                                ((Rkx0[iik] + 128) == Fbx0[ji]) and ((Rky0[iik] + 128) == Fby0[ji])))) or(
                                ((((Rkx0[iik] - 64) == Bx0[li]) and ((Rky0[iik] - 64) == By0[li])) and (
                                ((Rkx0[iik] - 128) == Fbx0[ji]) and ((Rky0[iik] - 128) == Fby0[ji]))) or (
                                (((Rkx0[iik] + 64) == Bx0[li]) and ((Rky0[iik] - 64) == By0[li])) and (
                                ((Rkx0[iik] + 128) == Fbx0[ji]) and ((Rky0[iik] - 128) == Fby0[ji]))))):
                                return True


        return False

    else:                                      #This condtion does the same as above but fot the black player.

        for ji in range(len(Fbx0)):
            for li in range(len(Rx0)):
                for iik in range(a, b):

                    if ((((((Bkx0[iik] - 64) == Rx0[li]) and ((Bky0[iik] + 64) == Ry0[li])) and (
                        ((Bkx0[iik] - 128) == Fbx0[ji]) and ((Bky0[iik] + 128) == Fby0[ji]))) or (
                        (((Bkx0[iik] + 64) == Rx0[li]) and ((Bky0[iik] + 64) == Ry0[li])) and (
                        ((Bkx0[iik] + 128) == Fbx0[ji]) and ((Bky0[iik] + 128) == Fby0[ji])))) or (
                        ((((Bkx0[iik] - 64) == Rx0[li]) and ((Bky0[iik] - 64) == Ry0[li])) and (
                        ((Bkx0[iik] - 128) == Fbx0[ji]) and ((Bky0[iik] - 128) == Fby0[ji]))) or (
                        (((Bkx0[iik] + 64) == Rx0[li]) and ((Bky0[iik] - 64) == Ry0[li])) and (
                        ((Bkx0[iik] + 128) == Fbx0[ji]) and ((Bky0[iik] - 128) == Fby0[ji]))))):

                        return True

        return False


def play():                                      #This is the main game function. It gets called everytime a left click occurs.
                                                 #All variable and flags are made global which are required in other functions.

    global select , black, k, kk, killed, killer, ffx, index0, index,kingmade, kingbmade
    global lastx0, lastx, lasty, lasty0, kill, king, kingkiller, indexk, indexk0
    global Fbx, Fbx0, Fby, Fby0
    global Ry, Ry0, Rx, Rx0
    global By, By0, Bx, Bx0

    x = root.winfo_pointerx() - root.winfo_rootx()           #This formula returns the x,y co-ordinates of the mouse pointer relative to the board.
    y = root.winfo_pointery() - root.winfo_rooty()
    print("Click at: ", x, y)

    if (black == False):                                     #flag to start Red player's turn
        if (select == False):                                #If no block is selected.

            if killer == True:                               #flag to check is the player has killed a game piece, so narrows the selection.
                 index = kill                                #down to that game piece that made the kill.
                 index0 = (kill-1)
                 indexk = 0
                 indexk0 = 0

                 if(canKill(index0, index) == False):        #if second move is not possible. Turn is over.
                     killer = False
                     black = True
                     return

            if kingkiller == True:                          #Checks if the king has killed.
                indexk = kill
                indexk0 = (kill-1)
                index = 0
                index0 = 0

                if (canKingKill(indexk0, indexk) == False):                 #If king cant kill, turn is over.
                    kingkiller = False
                    black = True
                    return

            else:
                index = len(Rx)
                index0 = 0
                indexk = len(Rkx)
                indexk0 = 0

            for i in range (index0, index):                      #Traverses through all available block to check where the player has clicked.
                for j in range (len(Fbx0)):
                    for l in range (len(Bx0)):                   #If the click is on the Red blocks. They are selected.

                        if (x < Rx[i] and x >= Rx0[i] and y >= Ry0[i] and y < Ry[i]):

                            if ((canKill(index0, index)==False) and (canKingKill(indexk0, indexk) ==False)):

                                if (killer==True):
                                    killer=False
                                    black=True
                                    return


                                if ((((Rx0[i] - 64) == Fbx0[j]) and ((Ry0[i] + 64) == Fby0[j])) or (((Rx0[i] + 64) ==
                                    Fbx0[j]) and ((Ry0[i] + 64) == Fby0[j]))):
                                    Label(image=logo4, width=60, height=60,relief=SUNKEN).place(x=Rx0[i], y=Ry0[i])
                                    lastx0 = Rx0[i]
                                    lastx = Rx[i]
                                    lasty = Ry[i]                       #This checks if move is permissible. The block is highlighted.
                                    lasty0 = Ry0[i]
                                    k = i
                                    ffx=l
                                    king=False
                                    select = True
                                    return

                            else:                               ##This checks if a kill move is permissible. The block is highlighted.

                                if (((((Rx0[i] - 64) == Bx0[l]) and ((Ry0[i] + 64) == By0[l])) and (
                                    ((Rx0[i] - 128) == Fbx0[j]) and ((Ry0[i] + 128) == Fby0[j]))) or (
                                    (((Rx0[i] + 64) == Bx0[l]) and ((Ry0[i] + 64) == By0[l])) and (
                                    ((Rx0[i] + 128) == Fbx0[j]) and ((Ry0[i] + 128) == Fby0[j])))):
                                    Label(image=logo4, width=60, height=60,relief=SUNKEN).place(x=Rx0[i], y=Ry0[i])
                                    lastx0=Rx0[i]
                                    lastx=Rx[i]
                                    lasty=Ry[i]
                                    lasty0=Ry0[i]
                                    ffx = l
                                    k=i
                                    king = False
                                    select = True
                                    killed = True

                                    return

                                #KING's SELECTION CONDTIONS

            if (kingmade == True):
                for i in range(indexk0,indexk):                #This first check if a king is made. Then is checks for permissible moves.
                    for j in range(len(Fbx0)):                 #It then highlights the block to show it is selected.
                        for l in range(len(Bx0)):
                            if (x < Rkx[i] and x >= Rkx0[i] and y >= Rky0[i] and y < Rky[i]):
                                if ((canKingKill(indexk0, indexk) == False) and (canKill(index0, index))== False):

                                    if (kingkiller == True):
                                        kingkiller = False
                                        black = True
                                        return

                                    if((((Rkx0[i] - 64) == Fbx0[j]) and ((Rky0[i] + 64) == Fby0[j])) or
                                    (((Rkx0[i] + 64) == Fbx0[j]) and ((Rky0[i] + 64) == Fby0[j])) or (
                                    ((Rkx0[i] + 64) == Fbx0[j]) and ((Rky0[i] - 64) == Fby0[j])) or (
                                    ((Rkx0[i] - 64) == Fbx0[j]) and ((Rky0[i] - 64) == Fby0[j]))):

                                        Label(image=logork, width=60, height=60, relief=SUNKEN).place(x=Rkx0[i], y=Rky0[i])
                                        lastx0 = Rkx0[i]
                                        lastx = Rkx[i]
                                        lasty = Rky[i]
                                        lasty0 = Rky0[i]
                                        k = i
                                        ffx = l
                                        king = True
                                        select = True
                                        return
                                else:                             #Here it checks for a kill move.

                                    if ((((((Rkx0[i] - 64) == Bx0[l]) and ((Rky0[i] + 64) == By0[l])) and (
                                        ((Rkx0[i] - 128) == Fbx0[j]) and ((Rky0[i] + 128) == Fby0[j]))) or (
                                        (((Rkx0[i] + 64) == Bx0[l]) and ((Rky0[i] + 64) == By0[l])) and (
                                        ((Rkx0[i] + 128) == Fbx0[j]) and ((Rky0[i] + 128) == Fby0[j])))) or (
                                        ((((Rkx0[i] - 64) == Bx0[l]) and ((Rky0[i] - 64) == By0[l])) and (
                                        ((Rkx0[i] - 128) == Fbx0[j]) and ((Rky0[i] - 128) == Fby0[j]))) or (
                                        (((Rkx0[i] + 64) == Bx0[l]) and ((Rky0[i] - 64) == By0[l])) and (
                                        ((Rkx0[i] + 128) == Fbx0[j]) and ((Rky0[i] - 128) == Fby0[j]))))):

                                        Label(image=logork, width=60, height=60, relief=SUNKEN).place(x=Rkx0[i],y=Rky0[i])
                                        lastx0 = Rkx0[i]
                                        lastx = Rkx[i]
                                        lasty = Rky[i]
                                        lasty0 = Rky0[i]
                                        k = i
                                        ffx = l
                                        king = True
                                        killed = True
                                        select = True
                                        return


        if select == True:            #After the selection is done, this flag becomes true and the moving phase of blocks begin.

            for i in range(len(Fbx)):   #This loop checks the second click by player. If its a free space, it proceeds.

                if (x < (Fbx[i]) and x >= Fbx0[i] and y >= Fby0[i] and y < Fby[i]):
                    if king == False:                                                                #condition to move non king.
                        killer=move(killed,killer, select, black, i, k, ffx,x,y,king,kingkiller)

                    elif (king == True):
                        kingkiller = move(killed, killer, select, black, i, k, ffx, x, y, king,kingkiller)

                    if ((Rx0[len(Rx0)-1] in Lrx0) and (Ry0[len(Ry0)-1] == Lry0)):            #This checks if a game piece has reached the opposite
                                                                                             #end of the board, It is made a king.
                        Label(image=logork, width=60, height=60).place(x=Rx0[len(Rx0)-1], y=Lry0)

                        Rkx.append(Rx[len(Rx)-1]);
                        Rkx0.append(Rx0[len(Rx0)-1]);
                        Rky.append(Ry[len(Ry)-1]);
                        Rky0.append(Ry0[len(Ry0)-1]);

                        del Rx[k]
                        del Rx0[k]
                        del Ry[k]
                        del Ry0[k]

                        kingmade = True                                                #flag represents a king is available.

                    if ((killer != True) and (killer != False)):                      #if no move takes places. The turn is prevented for being over.
                        return

                    if ((kingkiller != True) and (kingkiller != False)):
                        return

                    killed = False

                    if killer == True:
                        kill=(len(Rx))
                        select = False
                        return

                    elif kingkiller == True:                           #if a killing move takes place. The move is started again for double jump.
                        kill = len(Rkx)
                        select = False
                        return

                    select = False
                    black = True
                    messagebox.showinfo(title="Checkers", message="Black's turn!")  #Red players turn is over.

                                      # Flag to start Red player's turn
    if (black == True):
        if (select == False):                       #flag to check is the player has killed a game piece, so narrows the selection.

            if killer == True:
                index = kill
                index0 = (kill - 1)
                indexk = 0
                indexk0 = 0

                if (canKill(index0, index) == False):   #if double jump not availabe. Ends Black's turn
                    killer = False
                    black = False
                    return

            if kingkiller == True:
                indexk = kill
                indexk0 = (kill - 1)
                index = 0
                index0 = 0

                if (canKingKill(indexk0, indexk) == False):     #if double jump for king not availabe. Ends Black's turn
                    kingkiller = False
                    black = False
                    return

            else:
                index = len(Bx)
                index0 = 0
                indexk = len(Bkx)
                indexk0 = 0

            for i in range(index0, index):                      #Traverses through all available block to check where the player has clicked.
                for j in range(len(Fbx0)):
                    for l in range(len(Rx0)):

                        if (x < Bx[i] and x >= Bx0[i] and y >= By0[i] and y < By[i]):

                            if ((canKill(index0, index) == False) and (canKingKill(indexk0, indexk) == False)):

                                if (killer == True):
                                    killer = False
                                    black = False
                                    return
                                                                #If the click is on the Red blocks. They are selected

                                if ((((Bx0[i] - 64) == Fbx0[j]) and ((By0[i] - 64) == Fby0[j])) or (
                                            ((Bx0[i] + 64) == Fbx0[j]) and ((By0[i] - 64) == Fby0[j]))):
                                    Label(image=logo5, width=60, height=60, relief=SUNKEN).place(x=Bx0[i], y=By0[i])
                                    lastx0 = Bx0[i]
                                    lastx = Bx[i]
                                    lasty = By[i]
                                    lasty0 = By0[i]
                                    k = i
                                    ffx = l
                                    king = False
                                    select = True
                                    return

                            else:                       # Game piece is selected here if it is killing.

                                if (((((Bx0[i] - 64) == Rx0[l]) and ((By0[i] - 64) == Ry0[l])) and (
                                            ((Bx0[i] - 128) == Fbx0[j]) and ((By0[i] - 128) == Fby0[j]))) or (
                                            (((Bx0[i] + 64) == Rx0[l]) and ((By0[i] - 64) == Ry0[l])) and (
                                                    ((Bx0[i] + 128) == Fbx0[j]) and ((By0[i] - 128) == Fby0[j])))):
                                    Label(image=logo5, width=60, height=60, relief=SUNKEN).place(x=Bx0[i], y=By0[i])
                                    lastx0 = Bx0[i]
                                    lastx = Bx[i]
                                    lasty = By[i]
                                    lasty0 = By0[i]
                                    ffx = l
                                    k = i
                                    king = False
                                    select = True
                                    killed = True

                                    return

                                    # KING CONDTION

            if (kingbmade == True):                            #This first check if a king is made. Then is checks for permissible moves.
                for i in range(indexk0, indexk):
                    for j in range(len(Fbx0)):
                        for l in range(len(Rx0)):
                            if (x < Bkx[i] and x >= Bkx0[i] and y >= Bky0[i] and y < Bky[i]):
                                if ((canKingKill(indexk0, indexk) == False) and (canKill(index0, index)) == False):

                                    if (kingkiller == True):
                                        kingkiller = False
                                        black = False
                                        return                    #King is highlighted here showning it is selected.

                                    if ((((Bkx0[i] - 64) == Fbx0[j]) and ((Bky0[i] + 64) == Fby0[j])) or
                                            (((Bkx0[i] + 64) == Fbx0[j]) and ((Bky0[i] + 64) == Fby0[j])) or (
                                                ((Bkx0[i] + 64) == Fbx0[j]) and ((Bky0[i] - 64) == Fby0[j])) or (
                                                ((Bkx0[i] - 64) == Fbx0[j]) and ((Bky0[i] - 64) == Fby0[j]))):
                                        Label(image=logobk, width=60, height=60, relief=SUNKEN).place(x=Bkx0[i],
                                                                                                      y=Bky0[i])
                                        lastx0 = Bkx0[i]
                                        lastx = Bkx[i]
                                        lasty = Bky[i]
                                        lasty0 = Bky0[i]
                                        k = i
                                        ffx = l
                                        king = True
                                        select = True
                                        return
                                else:

                                    if ((((((Bkx0[i] - 64) == Rx0[l]) and ((Bky0[i] + 64) == Ry0[l])) and (
                                                ((Bkx0[i] - 128) == Fbx0[j]) and ((Bky0[i] + 128) == Fby0[j]))) or (
                                                (((Bkx0[i] + 64) == Rx0[l]) and ((Bky0[i] + 64) == Ry0[l])) and (
                                                        ((Bkx0[i] + 128) == Fbx0[j]) and (
                                                        (Bky0[i] + 128) == Fby0[j])))) or (
                                                ((((Bkx0[i] - 64) == Rx0[l]) and ((Bky0[i] - 64) == Ry0[l])) and (
                                                            ((Bkx0[i] - 128) == Fbx0[j]) and (
                                                            (Bky0[i] - 128) == Fby0[j]))) or (
                                                        (((Bkx0[i] + 64) == Rx0[l]) and (
                                                            (Bky0[i] - 64) == Ry0[l])) and (
                                                                ((Bkx0[i] + 128) == Fbx0[j]) and (
                                                                (Bky0[i] - 128) == Fby0[j]))))):
                                        Label(image=logobk, width=60, height=60, relief=SUNKEN).place(x=Bkx0[i],y=Bky0[i])
                                        lastx0 = Bkx0[i]
                                        lastx = Bkx[i]
                                        lasty = Bky[i]
                                        lasty0 = Bky0[i]                 #King is selected here for a kill move.
                                        k = i
                                        ffx = l
                                        king = True
                                        killed = True
                                        select = True
                                        return


        if select == True:

            for i in range(len(Fbx)):
                if (x < (Fbx[i]) and x >= Fbx0[i] and y >= Fby0[i] and y < Fby[i]):
                    if king == False:
                        killer = move(killed, killer, select, black, i, k, ffx, x, y, king, kingkiller)

                    elif (king == True):
                        kingkiller = move(killed, killer, select, black, i, k, ffx, x, y, king, kingkiller)

                    if ((Bx0[len(Bx0) - 1] in Lbx0) and (By0[len(By0) - 1] == Lby0)):
                        Label(image=logobk, width=60, height=60).place(x=Bx0[len(Bx0) - 1], y=Lby0)

                        Bkx.append(Bx[len(Bx) - 1]);                   #This checks if a game piece has reached the opposite
                        Bkx0.append(Bx0[len(Bx0) - 1]);                #So a king appears on the game board.
                        Bky.append(By[len(By) - 1]);
                        Bky0.append(By0[len(By0) - 1]);

                        del Bx[k]
                        del Bx0[k]
                        del By[k]
                        del By0[k]

                        kingbmade = True

                    if ((killer != True) and (killer != False)):             #if move in not made, these flags prevents the turn from ending.
                        return

                    if ((kingkiller != True) and (kingkiller != False)):
                        return

                    killed = False

                    if killer == True:
                        kill = (len(Bx))
                        select = False
                        return

                    elif kingkiller == True:
                        kill = len(Bkx)
                        select = False
                        return

                    select = False                                     #Turn for black player is ender with a dialog warning.
                    black = False
                    messagebox.showinfo(title="Checkers", message="Red's turn!")


    if select == True:                                               # This flag checks if the same block is clicked again.
                                                                     #so it is unchecked. The player can select another box.

        if (x < lastx and x >= lastx0 and y >= lasty0 and y < lasty):
            if black == False:
                if king == False:
                    Label(image=logo4, width=60, height=60).place(x=lastx0, y=lasty0)
                    select = False

                else:
                    Label(image=logork, width=60, height=60).place(x=lastx0, y=lasty0)
                    king == False
                    select = False

            elif black == True:
                if king == False:
                    Label(image=logo5, width=60, height=60).place(x=lastx0, y=lasty0)
                    select = False
                else:
                    Label(image=logobk, width=60, height=60).place(x=lastx0, y=lasty0)
                    king == False
                    select = False
        return

    if ((len(Rx0) == 0) and (len(Rkx0) == 0)):        #Winning condition for Black player. All Black pieces are killed.
        toplevel = Toplevel()
        toplevel.geometry('250x80')
        L4 = Label(toplevel, text="Black Wins")
        L4.place(x=100, y=20)
        button = Button(toplevel, text="    Exit    ", command=lambda: root.quit())
        button.place(x=100, y=45)

    elif  ((len(Bx0) == 0) and (len(Bkx0) == 0)):      #Winning condition for Red player. All red pieces are killed.
        toplevel = Toplevel()
        toplevel.geometry('250x80')
        L4 = Label(toplevel, text="Red Wins")
        L4.place(x=50, y=20)
        button = Button(toplevel, text="    Exit    ", command=lambda: root.quit())
        button.place(x=100, y=45)


def leftClick(event):                         #Main play function is called on every left click.
    play()

root.bind("<Button-1>", leftClick)

def Escape():                                 #Quits the game is Esc key is pressed.

        toplevel = Toplevel()
        toplevel.geometry('250x80')

        L3 = Label(toplevel, text="Are you sure you want to quit?")
        L3.place(x=50,y=20)

        button = Button(toplevel, text="    Yes    ",command=lambda: root.quit())
        button.place(x=100, y=45)


def quit(event):                            #Quit windown is called on press of Esc key.

    Escape()

root.bind("<Escape>", quit)


#end section
root.config(menu=menubar)
root.mainloop()








