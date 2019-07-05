
from tkinter import *
tk = Tk() 
canvas = Canvas(tk,width=400, height=400, bg= 'black')
canvas.pack(expand=YES, fill=BOTH)
tk.title("JUEGO DAMAS")

tablero = [['a', '-', 'a', '-', 'a', '-', 'a', '-'],
           ['-', 'a', '-', 'a', '-', 'a', '-', 'a'],
           ['a', '-', 'a', '-', 'a', '-', 'a', '-'],
           ['-', '-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-', '-'],
           ['-', 'b', '-', 'b', '-', 'b', '-', 'b'],
           ['b', '-', 'b', '-', 'b', '-', 'b', '-'],
           ['-', 'b', '-', 'b', '-', 'b', '-', 'b']]

posficha=[['A','B','C','D','E','F','G','H'],
          ['1','2','3','4','5','6','7','8']]
dama=0
global turno 
global indice
global var
for filas in range(0,8):
    for cuadros in range(0,8):
        if tablero[filas][cuadros]==1:
            fichas = "Fichas blancas"
            if dama >=12:
                fichas = "Fichas negras"
            tablero[filas][cuadros] = [fichas,False]
            dama+=1
           
def crear_tablero():    
    for x in range(32):
        canvas.create_rectangle(0,0,50,50, fill='white')        
    for a in range(4):
        canvas.move(a+1,(a)*100,0)
    for b in range(4):
        canvas.move(b+5,(b+(b+1))*50,50)
    for a in range(4):        
        canvas.move(a+9,(a)*100,100)
    for b in range(4): 
        canvas.move(b+13,(b+(b+1))*50,150)
    for a in range(4):        
        canvas.move(a+17,(a)*100,200)
    for b in range(4):
        canvas.move(b+21,(b+(b+1))*50,250)
    for a in range(4):        
        canvas.move(a+25,(a)*100,300)
    for b in range(4):
        canvas.move(b+29,(b+(b+1))*50,350)

fichablanca = PhotoImage(file='Blanca_opt.png')
fichanegra = PhotoImage(file='Negra_opt.png')


def moverBlancas(event):
    y=event.y
    x=event.x
    indice=0
    if(x<50 and y<50):
        indice=33
    if((x>100 and x<150) and (y<50)):
        indice=34
    if((x>200 and x<250) and (y<50)):
        indice=35
    if((x>300 and x<350) and (y<50)):
        indice=36
    if((x>50 and x<100) and (y>50 and y<100)):
        indice=37
    if((x>150 and x<200) and (y>50 and y<100)):
        indice=38
    if((x>250 and x<300) and (y>50 and y<100)):
        indice=39
    if((x>350 and x<400) and (y>50 and y<100)):
        indice=40
    if((x<50) and (y>100and y<150)):
        indice=41
    if((x>100 and x<150) and (y>100 and y<150)):
        indice=42
    if((x>200 and x<250) and (y>100 and y<150)):
        indice=43
    if((x>300 and x<350) and (y>100 and y<150)):
        indice=44
    seleccion(indice)
    
    """MOVIMIENTO BLANCAS A LA DERECHA"""
     
    
    """MOVIMIENTO BLANCAS A LA IZQUIERDA"""
    """canvas.move(indice,-50,50)"""      
def moverDer():
    canvas.move(d1,50,50)
def moverIzq():
    canvas.move(d1,-50,50)
    

def seleccion(indicador):
    num = IntVar(value=1)
    global d1
    d1=indicador
    if(indicador==33):
        c1=Radiobutton(tk, text=posficha[0][1]+' '+posficha[1][1], variable=num, value=0,command=moverDer).pack()
        c2=Radiobutton(tk, text='', variable=num, value=1,command=moverIzq).pack()
    if(indicador==34):
        c1=Radiobutton(tk, text=posficha[0][3]+' '+posficha[1][1], variable=num, value=0,command=moverDer).pack()
        c2=Radiobutton(tk, text=posficha[0][1]+' '+posficha[1][1], variable=num, value=1,command=moverIzq).pack()
    if(indicador==35):
        c1=Radiobutton(tk, text=posficha[0][5]+' '+posficha[1][1], variable=num, value=0,command=moverDer).pack()
        c2=Radiobutton(tk, text=posficha[0][3]+' '+posficha[1][1], variable=num, value=1,command=moverIzq).pack()
    if(indicador==36):
        c1=Radiobutton(tk, text=posficha[0][7]+' '+posficha[1][1], variable=num, value=0,command=moverDer).pack()
        c2=Radiobutton(tk, text=posficha[0][5]+' '+posficha[1][1], variable=num, value=1,command=moverIzq).pack()
    if(indicador==37):
        c1=Radiobutton(tk, text=posficha[0][2]+' '+posficha[1][2], variable=num, value=0,command=moverDer).pack()
        c2=Radiobutton(tk, text=posficha[0][0]+' '+posficha[1][2], variable=num, value=1,command=moverIzq).pack()
    if(indicador==38):
        c1=Radiobutton(tk, text=posficha[0][4]+' '+posficha[1][2], variable=num, value=0,command=moverDer).pack()
        c2=Radiobutton(tk, text=posficha[0][2]+' '+posficha[1][2], variable=num, value=1,command=moverIzq).pack()
    if(indicador==39):
        c1=Radiobutton(tk, text=posficha[0][6]+' '+posficha[1][2], variable=num, value=0,command=moverDer).pack()
        c2=Radiobutton(tk, text=posficha[0][4]+' '+posficha[1][2], variable=num, value=1,command=moverIzq).pack()
    if(indicador==40):
        c1=Radiobutton(tk, text='', variable=num, value=0,command=moverDer).pack()
        c2=Radiobutton(tk, text=posficha[0][6]+' '+posficha[1][2], variable=num, value=1,command=moverIzq).pack()
    if(indicador==41):
        c1=Radiobutton(tk, text=posficha[0][1]+' '+posficha[1][3], variable=num, value=0,command=moverDer).pack()
        c2=Radiobutton(tk, text='', variable=num, value=1,command=moverIzq).pack()
    if(indicador==42):
        c1=Radiobutton(tk, text=posficha[0][3]+' '+posficha[1][3], variable=num, value=0,command=moverDer).pack()
        c2=Radiobutton(tk, text=posficha[0][1]+' '+posficha[1][3], variable=num, value=1,command=moverIzq).pack()
    if(indicador==43):
        c1=Radiobutton(tk, text=posficha[0][5]+' '+posficha[1][3], variable=num, value=0,command=moverDer).pack()
        c2=Radiobutton(tk, text=posficha[0][3]+' '+posficha[1][3], variable=num, value=1,command=moverIzq).pack()
    if(indicador==44):
        c1=Radiobutton(tk, text=posficha[0][7]+' '+posficha[1][3], variable=num, value=0,command=moverDer).pack()
        c2=Radiobutton(tk, text=posficha[0][5]+' '+posficha[1][3], variable=num, value=1,command=moverIzq).pack()

def moverNegras(event):
    y=event. y
    x=event.x
    indice=0
    if((x>50 and x<100) and (y>250 and y<300)):
        indice=45
    elif((x>150 and x<200) and (y>250 and y<300)):
        indice=46
    elif((x>250 and x<300) and (y>250 and y<300)):
        indice=47
    elif((x>350 and x<400) and (y>250 and y<300)):
        indice=48
    elif((x<50) and y>300 and (y<350)):
        indice=49
    elif((x>100 and x<150) and (y>300 and y<350)):
        indice=50
    elif((x>200 and x<250) and (y>300 and y<350)):
        indice=51
    elif((x>300 and x<350) and (y>300 and y<350)):
        indice=52
    elif((x>50 and x<100) and (y>350 and y<400)):
        indice=53
    elif((x>150 and x<200) and (y>350 and y<400)):
        indice=54
    elif((x>250 and x<300) and (y>350 and y<400)):
        indice=55
    elif((x>350 and x<400) and (y>350 and y<400)):
        indice=56
    """canvas.move(indice,50,50)"""
    canvas.move(indice,50,-50)
"""
def Mover_Fichas(coordenadasOr,coordenadasNuevas):
    filaOriginal=coordenadasOr[0]
    columnaOriginal=coordenadasOr[1]
    filaNueva=coordenadasNuevas[0]
    columnaNueva=coordenadasNuevas[1]
    ficha=tablero[filaOriginal][columnaOriginal]
    tablero[filaOriginal][columnaOriginal]=0
    tablero[filaNueva][columnaNueva]=ficha
    if turno=="j1":
        turno="j2"
    else:
        turno="j1"
    return True
"""
def crear_fichas():
    for x in range(12):
        blanca = canvas.create_image(10,10, anchor = NW, image=fichablanca,tags=("fichablanca"))
        canvas.tag_bind("fichablanca",'<Button-1>',moverBlancas)
    for a in range(4):
        canvas.move(a+33,(a)*100,0)
    for b in range(4):
        canvas.move(b+37,(b+(b+1))*50,50)
    for a in range(4):
        canvas.move(a+41,(a)*100,100)
    for x in range(12):
        negra = canvas.create_image(10,10, anchor = NW, image=fichanegra,tags=("fichanegra"))
        canvas.tag_bind("fichanegra",'<Button-1>',moverNegras)
    for b in range(4):
        canvas.move(b+45,(b+(b+1))*50,250)
    for a in range(4):
        canvas.move(a+49,(a)*100,300)
    for b in range(4):
        canvas.move(b+53,(b+(b+1))*50,350)

"""obj = tablero.create_image(pj,pi, anchor = NW, image=fichanegra,tags=("fnegra","ficha")) 
def mover_fichas():
    canvas.tag_bind("fichablanca", "<ButtonPress-1>", canvas.presion_button)


def presion_boton(canvas, evento):
        carta = canvas.canvas1.find_withtag(tk.CURRENT)
        canvas
        .carta_seleccionada = (carta, evento.x, evento.y)"""

"""def MapearTablero(matriz):"""
"""def Mover_Fichas(event):
    y=event.y
    x=event.x

    if()
   """ 

crear_tablero();
crear_fichas();
print();

tk.mainloop()