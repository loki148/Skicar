import tkinter, mouse, threading, time
import ctypes
from PIL import ImageGrab
win = tkinter.Tk()
win.title('Skicar')
frame = tkinter.Frame(win)
widthwin = 800
heightwin = 500
canvas = tkinter.Canvas(win, width=widthwin, height=heightwin, bg='white', cursor='tcross')
canvas.pack(fill = tkinter.BOTH, expand=True)
win.attributes('-fullscreen',True)
color= ['white','silver','grey','yellow','gold','#CC7722','orange','pink','magenta', 'red','crimson', 'purple','navy blue', 'dark blue', 'blue','teal', 'cyan', 'turquoise', 'green', 'dark green' , 'brown', 'black']
width = [4,12,16,20,28,36,42,50,60,70,80,100]
listforbeckwards = []
listforbeckwards1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','q','u','v','w','x','y','z','aa','ba','ca','da','ea','fa','ga','ha','ia','ja','ka','la','ma','na','oa','pa','ra','sa','ta','qa','ua','va','wa','xa','ya','za','ab','bb','cb','db','eb','fb','gb','hb','ib','jb','kb','lb','mb','nb','ob','pb','rb','sb','tb','qb','ub','vb','wb','xb','yb','zb','ad','bd','cd','dd','ed','fd','gd','hd','id','jd','kd','ld','md','nd','od','pd','rd','sd','td','qd','ud','vd','wd','xd','yd','zd','aad','bad','cad','dad','ead','fad','gad','had','iad','jad','kad','lad','mad','nad','oad','pad','rad','sad','tad','qad','uad','vad','wad','xad','yad','zad','abd','bbd','cbd','dbd','ebd','fbd','gbd','hbd','ibd','jbd','kbd','lbd','mbd','nbd','obd','pbd','rbd','sbd','tbd','qbd','ubd','vbd','wbd','xbd','ybd','zbd','ae','be','ce','de','ee','fe','ge','he','ie','je','ke','le','me','ne','oe','pe','re','se','te','qe','ue','ve','we','xe','ye','ze','aea','bae','cae','dae','eae','fae','gae','hae','iae','jae','kae','lae','mae','nae','oae','pae','rae','sae','tae','qae','uae','vae','wae','xae','yae','zae','abe','bbe','cbe','dbe','ebe','fbe','gbe','hbe','ibe','jbe','kbe','lbe','mbe','nbe','obe','pbe','rbe','sbe','tbe','qbe','ube','vbe','wbe','xbe','ybe','zbe','ade','bde','cde','dde','ede','fdee','gde','hde','ide','jde','kde','lde','mde','nde','ode','pde','rde','sde','tde','qde','ude','vde','wde','xde','yde','zde','aade','bade','cade','dade','eade','fade','gade','hade','iade','jade','kade','lade','made','nade','oade','pade','rade','sade','tade','qade','uade','vade','wade','xade','yade','zade','abde','bbde','cbde','dbde','ebde','fbde','gbde','hbde','ibde','jbde','kbde','lbde','mbde','nbde','obde','pbde','rbde','sbde','tbde','qbde','ubde','vbde','wbde','xbde','ybde','zbde',]
listforbeckwards2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','q','u','v','w','x','y','z','aa','ba','ca','da','ea','fa','ga','ha','ia','ja','ka','la','ma','na','oa','pa','ra','sa','ta','qa','ua','va','wa','xa','ya','za','ab','bb','cb','db','eb','fb','gb','hb','ib','jb','kb','lb','mb','nb','ob','pb','rb','sb','tb','qb','ub','vb','wb','xb','yb','zb','ad','bd','cd','dd','ed','fd','gd','hd','id','jd','kd','ld','md','nd','od','pd','rd','sd','td','qd','ud','vd','wd','xd','yd','zd','aad','bad','cad','dad','ead','fad','gad','had','iad','jad','kad','lad','mad','nad','oad','pad','rad','sad','tad','qad','uad','vad','wad','xad','yad','zad','abd','bbd','cbd','dbd','ebd','fbd','gbd','hbd','ibd','jbd','kbd','lbd','mbd','nbd','obd','pbd','rbd','sbd','tbd','qbd','ubd','vbd','wbd','xbd','ybd','zbd','ae','be','ce','de','ee','fe','ge','he','ie','je','ke','le','me','ne','oe','pe','re','se','te','qe','ue','ve','we','xe','ye','ze','aea','bae','cae','dae','eae','fae','gae','hae','iae','jae','kae','lae','mae','nae','oae','pae','rae','sae','tae','qae','uae','vae','wae','xae','yae','zae','abe','bbe','cbe','dbe','ebe','fbe','gbe','hbe','ibe','jbe','kbe','lbe','mbe','nbe','obe','pbe','rbe','sbe','tbe','qbe','ube','vbe','wbe','xbe','ybe','zbe','ade','bde','cde','dde','ede','fdee','gde','hde','ide','jde','kde','lde','mde','nde','ode','pde','rde','sde','tde','qde','ude','vde','wde','xde','yde','zde','aade','bade','cade','dade','eade','fade','gade','hade','iade','jade','kade','lade','made','nade','oade','pade','rade','sade','tade','qade','uade','vade','wade','xade','yade','zade','abde','bbde','cbde','dbde','ebde','fbde','gbde','hbde','ibde','jbde','kbde','lbde','mbde','nbde','obde','pbde','rbde','sbde','tbde','qbde','ubde','vbde','wbde','xbde','ybde','zbde',]

for item in listforbeckwards1:
    for items in listforbeckwards1:
        listforbeckwards.append(item+items)

print('lenoflist'+str(len(listforbeckwards)))
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(screensize)
d = 0
y = 0
x = 0
canvas.create_rectangle(0,0,370,10000, fill = 'grey',outline='grey')
canvas.create_rectangle(0,0,100000,40, fill = 'grey',outline='grey')
for i in range(2):
    x = 0
    for j in range(11):
        canvas.create_rectangle(10+x, 10+y, 30+x, 30+y, fill=color[d],tags= ('colors',str(color[d])) )
        print(str(x+10), str(x+30),str(y+10),str(y+30))
        d += 1
        x +=30
    y += 30
x = 0
e = 0
for h in range(12):
        canvas.create_rectangle(10+x, 70, 30+x, 90, fill='silver', tags= ('widthr','w'+str(width[e])) )
        canvas.create_text(20+x ,80 , text = width[e], font='arial 10 bold',tags= ('widtht','n'+str(width[e])))
        e += 1
        x+=30
        
canvas.create_rectangle(340, 10, 360, 30, fill='silver', tags='backspace')
canvas.create_text(350 ,20 , text ='⌫' ,font='arial 12',tags='backspace1' )

canvas.create_rectangle(340, 40, 360, 60, fill='silver', tags='bg')
canvas.create_text(350 ,50 , text ='bg' ,font='arial 12',tags='bg1' )

canvas.create_rectangle(screensize[0]-30, 10, screensize[0]-10, 30, fill='red', tags='exit')
canvas.create_text(screensize[0]-20 ,20 , text ='X' ,font='arial 12',tags='exit' )

canvas.create_rectangle(10, 100, 30, 120, fill='silver', tags=('crcl','tool'))
canvas.create_text(20 ,110 , text ='○' ,font='arial 12',tags=('crcl','tool'))

canvas.create_rectangle(40, 100, 60, 120, fill='silver', tags=('mindworking','linem','tool'))
canvas.create_text(50 ,110 , text ='|' ,font='arial 12',tags=('linem','tool'))

canvas.create_rectangle(70, 100, 90, 120,width = 3, fill='silver', tags=('draw','tool'))
canvas.create_text(80 ,110 , text ='~' ,font='arial 15 bold',tags=('draw','tool'))

canvas.create_rectangle(100, 100, 120, 120, fill='silver', tags=('rectangle','tool'))
canvas.create_text(110 ,110 , text ='□' ,tags=('rectangle','tool'))

canvas.create_rectangle(130, 100, 150, 120, fill='silver', tags=('rectanglefilled','tool'))
canvas.create_text(140 ,110 , text ='■' ,tags=('rectanglefilled','tool'))

canvas.create_rectangle(160, 100, 180, 120, fill='silver', tags=('circlefilled','tool'))
canvas.create_text(170 ,110 , text ='●' ,tags=('circlefilled','tool'))

canvas.create_rectangle(190, 100, 210, 120, fill='silver', tags=('save','tool'))
canvas.create_text(200 ,110 , text ='💾',font='arial 12',tags= ('save','tool'))

canvas.create_rectangle(230, 100, 280, 150, fill='silver', tags=('backarrow','tool'))
canvas.create_text(255 ,125 , text ='⤺',font='arial 40',tags= ('backarrow','tool'))

#canvas.create_rectangle(250, 100, 270, 120, fill='silver', tags=('backarrow','tool'))
#canvas.create_text(260 ,110 , text ='',font='arial 12',tags= ('backarrow','tool'))

canvas.itemconfig('w'+str(width[2]), width=3)
canvas.itemconfig(str(color[21]), width=3)

width_selected = 16
selected_color= 'black'
curr_bg_color = 'white'
antibug = True
canYoubro = False
lineGoGOGO = False
failsafe = False
cubidubidu = False
filledcube = False
filledcircle = False
saving = False
def color_pick(sur):
    x = sur.x
    y = sur.y
    global selected_color
    global color
    global f      
    global width
    global width_selected
    global antibug
    global curr_bg_color
    global canYoubro
    global lineGoGOGO
    global failsafe
    global lx
    global ly
    global cubidubidu
    global filledcube
    global filledcircle
    global saving
    global tagofdrawnitems
    global listforbeckwards
    failsafe = False
    saving == False
    if 10<x<30 and 10<y<30:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[0]
        canvas.itemconfig(str(color[0]), width=3)
        failsafe = False
    elif 40<x<60 and 10<y<30:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[1]
        canvas.itemconfig(str(color[1]), width=3)
        failsafe = False
    elif 70<x<90 and 10<y<30:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[2]
        canvas.itemconfig(str(color[2]), width=3)
        failsafe = False
    elif 100<x<120 and 10<y<30:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[3]
        canvas.itemconfig(str(color[3]), width=3)
        failsafe = False
    elif 130<x<150 and 10<y<30:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[4]
        canvas.itemconfig(str(color[4]), width=3)
        failsafe = False
    elif 160<x<180 and 10<y<30:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[5]
        canvas.itemconfig(str(color[5]), width=3)
        failsafe = False
    elif 190<x<210 and 10<y<30:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[6]
        canvas.itemconfig(str(color[6]), width=3)
        failsafe = False
    elif 220<x<240 and 10<y<30:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[7]
        canvas.itemconfig(str(color[7]), width=3)
        failsafe = False
    elif 250<x<270 and 10<y<30:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[8]
        canvas.itemconfig(str(color[8]), width=3)
        failsafe = False
    elif 280<x<300 and 10<y<30:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[9]
        canvas.itemconfig(str(color[9]), width=3)
        failsafe = False
    elif 310<x<330 and 10<y<30:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[10]
        canvas.itemconfig(str(color[10]), width=3)
        failsafe = False
    elif 10<x<30 and 40<y<60:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[11]
        canvas.itemconfig(str(color[11]), width=3)
        failsafe = False
    elif 40<x<60 and 40<y<60:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[12]
        canvas.itemconfig(str(color[12]), width=3)
        failsafe = False
    elif 70<x<90 and 40<y<60:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[13]
        canvas.itemconfig(str(color[13]), width=3)
        failsafe = False
    elif 100<x<120 and 40<y<60:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[14]
        canvas.itemconfig(str(color[14]), width=3)
        failsafe = False
    elif 130<x<150 and 40<y<60:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[15]
        canvas.itemconfig(str(color[15]), width=3)
        failsafe = False
    elif 160<x<180 and 40<y<60:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[16]
        canvas.itemconfig(str(color[16]), width=3)
        failsafe = False
    elif 190<x<210 and 40<y<60:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[17]
        canvas.itemconfig(str(color[17]), width=3)
        failsafe = False
    elif 220<x<240 and 40<y<60:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[18]
        canvas.itemconfig(str(color[18]), width=3)
        failsafe = False
    elif 250<x<270 and 40<y<60:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[19]
        canvas.itemconfig(str(color[19]), width=3)
        failsafe = False
    elif 280<x<300 and 40<y<60:
        canvas.itemconfig('colors',width=1 )
        selected_color = color[20]
        canvas.itemconfig(str(color[20]), width=3)
        failsafe = False
    elif 310<x<330 and 40<y<60:
        canvas.itemconfig('colors', width=1 )
        selected_color = color[21]
        canvas.itemconfig(str(color[21]), width=3)
        failsafe = False
        
    elif 340<x<360 and 10<y<30:
        canvas.delete('line')
        canvas.itemconfig('backspace', fill = 'red')
        tagofdrawnitems = 0
        canvas.update()
        time.sleep(0.17)
        canvas.itemconfig('backspace', fill = 'silver')
        failsafe = False
    elif 340<x<360 and 40<y<60:
        canvas.config(bg=selected_color)
        canvas.itemconfig('bg', fill = 'yellow')
        canvas.update()
        time.sleep(0.17)
        canvas.itemconfig('bg', fill = 'silver')
        failsafe = False
        curr_bg_color = selected_color
    elif screensize[0]-30<x<screensize[0]-10 and 10<y<30:
        canvas.itemconfig('exit', fill = 'maroon')
        canvas.update()
        time.sleep(0.17)
        canvas.itemconfig('exit', fill = 'red')
        canvas.update()
        win.destroy()
    elif 10<x<30 and 70<y<90:
        canvas.itemconfig('widthr', width=1 )
        width_selected = width[0]
        canvas.itemconfig('w'+str(width[0]), width=3)
        failsafe = False
    elif 40<x<60 and 70<y<90:
        canvas.itemconfig('widthr', width=1 )
        width_selected = width[1]
        canvas.itemconfig('w'+str(width[1]), width=3)
        failsafe = False
    elif 70<x<90 and 70<y<90:
        canvas.itemconfig('widthr', width=1 )
        width_selected = width[2]
        canvas.itemconfig('w'+str(width[2]), width=3)
        failsafe = False
    elif 100<x<120 and 70<y<90:
        canvas.itemconfig('widthr', width=1 )
        width_selected = width[3]
        canvas.itemconfig('w'+str(width[3]), width=3)
        failsafe = False
    elif 130<x<150 and 70<y<90:
        canvas.itemconfig('widthr', width=1 )
        width_selected = width[4]
        canvas.itemconfig('w'+str(width[4]), width=3)
        failsafe = False
    elif 160<x<180 and 70<y<90:
        canvas.itemconfig('widthr', width=1 )
        width_selected = width[5]
        canvas.itemconfig('w'+str(width[5]), width=3)
        failsafe = False
    elif 190<x<210 and 70<y<90:
        canvas.itemconfig('widthr', width=1 )
        width_selected = width[6]
        canvas.itemconfig('w'+str(width[6]), width=3)
        failsafe = False
    elif 220<x<240 and 70<y<90:
        canvas.itemconfig('widthr', width=1 )
        width_selected = width[7]
        canvas.itemconfig('w'+str(width[7]), width=3)
        failsafe = False
    elif 250<x<270 and 70<y<90:
        canvas.itemconfig('widthr', width=1 )
        width_selected = width[8]
        canvas.itemconfig('w'+str(width[8]), width=3)
        failsafe = False
    elif 280<x<300 and 70<y<90:
        canvas.itemconfig('widthr', width=1 )
        width_selected = width[9]
        canvas.itemconfig('w'+str(width[9]), width=3)
        failsafe = False
    elif 310<x<330 and 70<y<90:
        canvas.itemconfig('widthr', width=1 )
        width_selected = width[10]
        canvas.itemconfig('w'+str(width[10]), width=3)
        failsafe = False
    elif 340<x<360 and 70<y<90:
        canvas.itemconfig('widthr', width=1 )
        width_selected = width[11]
        canvas.itemconfig('w'+str(width[11]), width=3)
        failsafe = False
    elif 10<x<30 and 100<y<120:
        canvas.itemconfig('tool', width=1 )
        canvas.itemconfig('crcl', width=3)
        antibug = False
        failsafe = False
        canYoubro = True
        cubidubidu = False
        lineGoGOGO = False
        filledcube = False
        filledcircle = False
        saving = False
        lx.clear()
        ly.clear()
    elif 40<x<60 and 100<y<120:
        canvas.itemconfig('tool', width=1 )
        canvas.itemconfig('mindworking', width=3 )#line
        canvas.update()
        antibug = False
        lineGoGOGO = True
        failsafe = False
        canYoubro = False
        cubidubidu = False
        filledcube = False
        filledcircle = False
        saving = False
        lx.clear()
        ly.clear()
    elif 70<x<90 and 100<y<120:
        canvas.itemconfig('tool', width=1 )
        canvas.itemconfig('draw', width=3)
        antibug = True
        failsafe = False
        lineGoGOGO = False
        canYoubro = False
        cubidubidu = False
        filledcube = False
        filledcircle = False
        saving = False
        lx.clear()
        ly.clear()
    elif 100<x<120 and 100<y<120:
        canvas.itemconfig('tool', width=1 )
        canvas.itemconfig('rectangle', width=3)
        antibug = False
        failsafe = False
        lineGoGOGO = False
        canYoubro = False
        cubidubidu = True
        filledcube = False
        filledcircle = False
        saving = False
        lx.clear()
        ly.clear()
    elif 130<x<150 and 100<y<120:
        canvas.itemconfig('tool', width=1 )
        canvas.itemconfig('rectanglefilled', width=3)
        antibug = False
        failsafe = False
        lineGoGOGO = False
        canYoubro = False
        cubidubidu = False
        filledcube = True
        filledcircle = False
        saving = False
        lx.clear()
        ly.clear()

    elif 160<x<180 and 100<y<120:
        canvas.itemconfig('tool', width=1 )
        canvas.itemconfig('circlefilled', width=3)
        antibug = False
        failsafe = False
        lineGoGOGO = False
        canYoubro = False
        cubidubidu = False
        filledcube = False
        filledcircle = True
        saving = False
        lx.clear()
        ly.clear()
        190, 100, 210, 120
    elif 190<x<210 and 100<y<120:
        canvas.itemconfig('tool', width=1 )
        canvas.itemconfig('save', width=3)
        canvas.update()
        time.sleep(0.17)
        antibug = False
        failsafe = False
        lineGoGOGO = False
        canYoubro = False
        cubidubidu = False
        filledcube = False
        filledcircle = False
        saving = True
        savename()
        save()
        lx.clear()
        ly.clear()
    elif 230<x<280 and 100<y<150:
        canvas.itemconfig('backarrow', width=3 )
        canvas.delete('a'+listforbeckwards[tagofdrawnitems])
        canvas.update()
        time.sleep(0.5)
        canvas.itemconfig('backarrow', width=1 )
        if antibug == True:
            tagofdrawnitems -= 1
        else:
            tagofdrawnitems -= 2
        #deletelaststep()
    else:
        failsafe = True
        
        canvas.itemconfig('save', width=1)
dx = []
dy = []
'working?'
def draw(x,y):
    global selected_color
    global width_selected
    global dx
    global dy
    global curr_bg_color
    global failsafe
    global tagofdrawnitems
    width_adjusted = width_selected /2 
    global listforbeckwards 
    dx.append(x)
    dy.append(y)
    print(len(dx))
    if 370>= x and 130 >= y:
        failsafe = False
    
    d = 0
    if failsafe == True:
        for items in lx:
                
            if items <370:
                dx.pop(d)
                dy.pop(d)
            d+=1
        d = 0
        for items in ly:
                
            if items<40:
                dx.pop(d)
                dy.pop(d)
                d+=1
        try:
            canvas.create_line(dx[-2],dy[-2],dx[-1],dy[-1],fill = selected_color,width =width_selected, tags=('line', 'a'+listforbeckwards[tagofdrawnitems]))
            canvas.create_oval(x-width_adjusted,y-width_adjusted,x+width_adjusted,y+width_adjusted,fill= selected_color, outline= selected_color, tags=('line','line'+str(f), 'a'+listforbeckwards[tagofdrawnitems]))
        except IndexError:
            if y <= 40:
                pass
            else:
                canvas.create_oval(x-width_adjusted,y-width_adjusted,x+width_adjusted,y+width_adjusted,fill= selected_color, outline= selected_color, tags=('line','line'+str(f), 'a'+listforbeckwards[tagofdrawnitems]))
        if len(dx) > 20:
            nono = len(dx) - 2
            del dx[0:nono]
            del dy[0:nono]
            print(str(len(dx))+'<----')
            
event = 0

f = 0
def motion(event):
    global tagofdrawnitems
    global f
    global antibug
    global failsafe
    x = event.x
    y = event.y
    #print(str(x)+ ' ' +str(y))
    if antibug == True:
        if failsafe == True:
            
            if x<370:
                x= 370
            if y<40:
                y = 40
            draw(x,y)
    else:
        pass
lx = []
ly = []
hm = 0
def circle(event):
    global lx
    global ly
    global curr_bg_color
    global selected_color
    global width_selected
    global hm
    global canYoubro
    global tagofdrawnitems
    global listforbeckwards
    x =event.x
    y = event.y
    lx.append(x)
    ly.append(y)
    print(len(lx))
    print(str(lx[hm])+ ' '+ str(ly[hm]))
    if len(lx)<= 2:
        if canYoubro == True:
            d = 0
            for items in lx:
                
                if items <370:
                    lx.pop(d)
                    ly.pop(d)
                d+=1
            d = 0
            for items in ly:
                
                if items<40:
                    lx.pop(d)
                    ly.pop(d)
                d+=1
            if len(lx)== 2:
                canvas.create_oval(lx[0],ly[0],lx[1],ly[1],outline=selected_color,fill='',width =width_selected, tags=('line', 'a'+listforbeckwards[tagofdrawnitems]))
                lx.clear()
                ly.clear()
            else:
                pass
    
ddd = 0
lxl = []
lyl = []
def line(event):
    global lx
    global ly
    global curr_bg_color
    global selected_color
    global width_selected
    global hm
    global lineGoGOGO
    global tagofdrawnitems
    global listforbeckwards
    x =event.x
    y = event.y
    lx.append(x)
    ly.append(y)
    print(len(lx))
    print(str(lx[hm])+ ' '+ str(ly[hm]))
    if len(lx)<= 2:
        if lineGoGOGO == True:
            d = 0
            for items in lx:
                
                if items <370:
                    lx.pop(d)
                    ly.pop(d)
                d+=1
            d = 0
            for items in ly:
                
                if items<40:
                    lx.pop(d)
                    ly.pop(d)
                d+=1
            if len(lx)== 2:
                canvas.create_line(lx[0],ly[0],lx[1],ly[1],fill=selected_color,width =width_selected, tags=('line', 'a'+listforbeckwards[tagofdrawnitems]))
                lx.clear()
                ly.clear()
            else:
                pass

def cube(event):
    global lx
    global ly
    global curr_bg_color
    global selected_color
    global width_selected
    global hm
    global cubidubidu
    global tagofdrawnitems
    global listforbeckwards
    x =event.x
    y = event.y
    lx.append(x)
    ly.append(y)
    print(len(lx))
    print(str(lx[hm])+ ' '+ str(ly[hm]))
    if len(lx)<= 2:
        if cubidubidu == True:
            d = 0
            for items in lx:
                
                if items <370:
                    lx.pop(d)
                    ly.pop(d)
                d+=1
            d = 0
            for items in ly:
                
                if items<40:
                    lx.pop(d)
                    ly.pop(d)
                d+=1
            if len(lx)== 2:
                canvas.create_rectangle(lx[0],ly[0],lx[1],ly[1],outline=selected_color,fill='',width =width_selected, tags=('line', 'a'+listforbeckwards[tagofdrawnitems]))
                lx.clear()
                ly.clear()
            else:
                pass

            
def filledCube(event):
    global lx
    global ly
    global curr_bg_color
    global selected_color
    global width_selected
    global hm
    global filledcube
    global tagofdrawnitems
    global listforbeckwards
    x =event.x
    y = event.y
    lx.append(x)
    ly.append(y)
    print(len(lx))
    print(str(lx[hm])+ ' '+ str(ly[hm]))
    if len(lx)<= 2:
        if filledcube == True:
            d = 0
            for items in lx:
                
                if items <370:
                    lx.pop(d)
                    ly.pop(d)
                d+=1
            d = 0
            for items in ly:
                
                if items<40:
                    lx.pop(d)
                    ly.pop(d)
                d+=1
            if len(lx)== 2:
                canvas.create_rectangle(lx[0],ly[0],lx[1],ly[1],outline=selected_color,fill=selected_color,tags=('line', 'a'+listforbeckwards[tagofdrawnitems]))
                lx.clear()
                ly.clear()
            else:
                pass
            
def filledCircle(event):
    global tagofdrawnitems
    global lx
    global ly
    global curr_bg_color
    global selected_color
    global width_selected
    global hm
    global filledcircle
    global listforbeckwards
    x =event.x
    y = event.y
    lx.append(x)
    ly.append(y)
    print(len(lx))
    print(str(lx[hm])+ ' '+ str(ly[hm]))
    if len(lx)<= 2:
        if filledcircle == True:
            d = 0
            for items in lx:
                
                if items <370:
                    lx.pop(d)
                    ly.pop(d)
                d+=1
            d = 0
            for items in ly:
                
                if items<40:
                    lx.pop(d)
                    ly.pop(d)
                d+=1
            if len(lx)== 2:
                canvas.create_oval(lx[0],ly[0],lx[1],ly[1],outline=selected_color,fill=selected_color,tags=('line', 'a'+listforbeckwards[tagofdrawnitems]))
                lx.clear()
                ly.clear()
            else:
                pass

bdg = False
tagofdrawnitems = 0

def decider(event):
    global lineGoGOGO
    global canYoubro
    global antibug
    global cubidubidu
    global filledcube
    global filledcircle
    global bdg
    global tagofdrawnitems
    x = event.x
    y = event.y
    if x >= 370:
        if tagofdrawnitems >= 312:
            tagofdrawnitems = 0
        tagofdrawnitems += 1
    if bdg ==True:
        late_grab()
    
    if lineGoGOGO == True:
        line(event)
    elif canYoubro == True:
        circle(event)
    elif antibug == True:
        drawcall(event)
    elif cubidubidu == True:
        cube(event)
    elif filledcube == True:
        filledCube(event)
    elif filledcircle == True:
        filledCircle(event)

    color_pick(event)
    if x<370 or y < 40:
        pass
    elif antibug == True:
        draw(x,y)
    else:
        pass
def drawcall(event):
    x = event.x
    y = event.y
    if x <= 370:
        failsafe = False
    else:
        draw(x,y)
def setter(event):
    global lx
    global ly
    global tagofdrawnitems
    global listforbeckwards
    dx.clear()
    dy.clear()
    #tagofdrawnitems += 1
    print(str(tagofdrawnitems) +''+listforbeckwards[tagofdrawnitems])
    print('''^\n|||||||||''')

def show_entry_fields():
    print('well i got further')
    global e1
    global filename
    global master
    global win
    global antibug
    global bdg
    print(e1.get())
    filename = e1.get()
    time.sleep(0.3)
    master.destroy()
    antibug = True
    canvas.itemconfig('draw', width=3)
    canvas.itemconfig('save', width=1)
    bdg = True
    

def caller(event):
    show_entry_fields()
def savename():
    print('well i got so far')
    global filename
    global saving
    global e1
    global master
    global antibug
    master = tkinter.Tk()
    master.title('Save as')
    master.geometry('250x100')
    master.configure(background='navy blue')
    tkinter.Label(master,bg ='deep sky blue', text="File name:").grid(row=0,column=1)
    e1 = tkinter.Entry(master)
    e1.grid(row=0, column=3,)
    tkinter.Button(master, 
          text='Save', command=show_entry_fields).grid(  row=2, 
                                                         column=1, 
                                                         sticky=tkinter.W, 
                                                         pady=4)
    master.bind('<Return>', caller)
    saving = False
    
    
    master.mainloop()
def save():
    global saving
    saving = False
    
def late_grab():
    global screensize
    global filename
    global bdg
    x=370
    y=40
    x1=screensize[0]
    y1=screensize[1]
    win.focus()
    ImageGrab.grab( include_layered_windows=False).crop((x,y,x1,y1)).save(str(filename)+'.jpg')
    bdg = False

canvas.bind_all('<B1-Motion>', motion)
canvas.bind_all("<Button-1>", decider)
canvas.bind_all("<ButtonRelease-1>",setter)
win.mainloop()
