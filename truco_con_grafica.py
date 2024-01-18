from random import randint
import tkinter

root = tkinter.Tk()
root.title("Truco")
root.config(bg="light grey")

def ver_repetidas(cantidad_de_cartas):
   
    repartir1 = randint (0,cantidad_de_cartas-1)
    repartir2 = randint (0,cantidad_de_cartas-1)
    repartir3 = randint (0,cantidad_de_cartas-1)
       
    verficar_repetidas = 0
     
    while verficar_repetidas <= 0:
        if repartir1 != repartir2 and repartir1 != repartir3 and repartir2 != repartir3:
            verficar_repetidas += 1
        elif repartir1 == repartir2:
            repartir2 = randint (0,cantidad_de_cartas)
        elif repartir1 == repartir3:
            repartir3 = randint (0,cantidad_de_cartas)
        elif repartir2 == repartir3:
            repartir3 = randint (0,cantidad_de_cartas)
         
    return repartir1, repartir2, repartir3        


def repartir (baraja): 
    baraja_copia = baraja.copy()
    
    for i in range (1,3): #repartirmos cartas a jugador
        
        recibir_carta = ver_repetidas(len(baraja_copia)) # asigna cartas segun indice
        
        if i == 1:
            jugador_1 = [baraja_copia[recibir_carta[0]], baraja_copia[recibir_carta[1]], baraja_copia[recibir_carta[2]]]
            baraja_copia.remove(baraja[recibir_carta[0]])
            baraja_copia.remove(baraja[recibir_carta[1]])
            baraja_copia.remove(baraja[recibir_carta[2]])

        elif i == 2:
            jugador_2 = [baraja_copia[recibir_carta[0]], baraja_copia[recibir_carta[1]], baraja_copia[recibir_carta[2]]]
            return jugador_1, jugador_2


def repartir_cartas():
    global jugador_1, jugador_2, mostrar_boton1, mostrar_boton2, mostrar_boton3, mostrar_boton4, mostrar_boton5, mostrar_boton6
    cartas_de_jugador = repartir(baraja)
    jugador_1, jugador_2 = cartas_de_jugador
    mostrar_boton1 = 0
    mostrar_boton2 = 0
    mostrar_boton3 = 0
    mostrar_boton4 = 0
    mostrar_boton5 = 0
    mostrar_boton6 = 0
    carta1 = tkinter.Label (root, image=baraja_imagen[jugador_1[0]], width=130, height=200).grid(row=5,column=0)
    carta2 = tkinter.Label (root, image=baraja_imagen[jugador_1[1]], width=130, height=200).grid(row=5,column=1)
    carta3 = tkinter.Label (root, image=baraja_imagen[jugador_1[2]], width=130, height=200).grid(row=5,column=2)
    carta4 = tkinter.Label (root, image=baraja_imagen[jugador_2[0]], width=130, height=200).grid(row=5,column=4)
    carta5 = tkinter.Label (root, image=baraja_imagen[jugador_2[1]], width=130, height=200).grid(row=5,column=5)
    carta6 = tkinter.Label (root, image=baraja_imagen[jugador_2[2]], width=130, height=200).grid(row=5,column=6)
    carta_jug_11 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=9,column=1)
    carta_jug_22 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=9,column=5)
    boton1 = tkinter.Button (root, text="Jugar",activebackground="yellow", cursor="hand2",command=tocar_boton_1).grid(row=6,column=0)
    boton2 = tkinter.Button (root, text="Jugar",activebackground="yellow", cursor="hand2",command=tocar_boton_2).grid(row=6,column=1)
    boton3 = tkinter.Button (root, text="Jugar",activebackground="yellow", cursor="hand2",command=tocar_boton_3).grid(row=6,column=2)
    boton4 = tkinter.Button (root, text="Jugar",activebackground="yellow", cursor="hand2",command=tocar_boton_4).grid(row=6,column=4)
    boton5 = tkinter.Button (root, text="Jugar",activebackground="yellow", cursor="hand2",command=tocar_boton_5).grid(row=6,column=5)
    boton6 = tkinter.Button (root, text="Jugar",activebackground="yellow", cursor="hand2",command=tocar_boton_6).grid(row=6,column=6)
    label_tapa_boton_otro_juego = tkinter.Label(root,bg="light grey",width=13, height=2).grid(row=2,column=3)
    label_mostrar_puntos_ronda_jug1 = tkinter.Label(root,bg="light grey", text=f"Puntos de juego {puntos_ronda_jugador1}", font=("arial",12)).grid(row=9,column=0)
    label_mostrar_puntos_ronda_jug2 = tkinter.Label(root,bg="light grey", text=f"Puntos de juego {puntos_ronda_jugador2}", font=("arial",12)).grid(row=9,column=4)
    label_mostrar_partidas_jug1 = tkinter.Label(root,bg="light grey", text=f"Juegos ganados  {puntos_juego_jugador1}", font=("arial",12),justify="left").grid(row=7,column=0)
    label_mostrar_partidas_jug2 = tkinter.Label(root,bg="light grey", text=f"Juegos ganados {puntos_juego_jugador2}", font=("arial",12)).grid(row=7,column=4)
    label_tapar_mensaje1 = tkinter.Label(root,bg="light grey",width=40, height=2).grid(row=7,column=0,columnspan=3)
    label_tapar_mensaje2 = tkinter.Label(root,bg="light grey",width=40, height=2).grid(row=7,column=4,columnspan=3)
    if (puntos_juego_jugador1 + puntos_juego_jugador2) %2 == 0:
        label_su_turno = tkinter.Label(root,text= "Su Turno", font=("arial",14),bg="gold",width=10, height=1).grid(row=4,column=0)
        turno_jug1 ()
    elif (puntos_juego_jugador1 + puntos_juego_jugador2) %2 == 1:
        label_su_turno = tkinter.Label(root,text= "Su Turno", font=("arial",14),bg="gold",width=10, height=1).grid(row=4,column=4)
        turno_jug2 ()


def contar_cartas_jugadas():
    global carta_jugada_n
    carta_jugada_n += 1
    

def tocar_boton_1 ():
            global elegir1, mostrar_boton1
            mostrar_boton1 += 1
            elegir1 = 0 
            carta1 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=5,column=0)
            carta_jug_11 = tkinter.Label (root, image=baraja_imagen[jugador_1[0]], width=130, height=200).grid(row=9,column=1)
            tapar_boton1 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=0)
            contar_cartas_jugadas()
            mostrar_primer_carta()

def tocar_boton_2 ():
            global elegir1, mostrar_boton2
            mostrar_boton2 += 1
            elegir1 = 1
            carta2 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=5,column=1)
            carta_jug_11 = tkinter.Label (root, image=baraja_imagen[jugador_1[1]], width=130, height=200).grid(row=9,column=1) 
            tapar_boton2 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=1)
            contar_cartas_jugadas()
            mostrar_primer_carta()

def tocar_boton_3 ():
            global elegir1, mostrar_boton3
            mostrar_boton3 += 1
            elegir1 = 2 
            carta3 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=5,column=2)
            carta_jug_11 = tkinter.Label (root, image=baraja_imagen[jugador_1[2]], width=130, height=200).grid(row=9,column=1)
            tapar_boton3 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=2)
            contar_cartas_jugadas()
            mostrar_primer_carta()

def tocar_boton_4 ():
            global elegir2, mostrar_boton4
            mostrar_boton4 += 1
            elegir2 = 0 
            carta4 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=5,column=4)
            carta_jug_22 = tkinter.Label (root, image=baraja_imagen[jugador_2[0]], width=130, height=200).grid(row=9,column=5)
            tapar_boton4 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=4)
            contar_cartas_jugadas()
            mostrar_primer_carta()           

def tocar_boton_5 ():
            global elegir2, mostrar_boton5
            mostrar_boton5 += 1
            elegir2 = 1 
            carta5 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=5,column=5)
            carta_jug_22 = tkinter.Label (root, image=baraja_imagen[jugador_2[1]], width=130, height=200).grid(row=9,column=5)
            tapar_boton5 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=5)
            contar_cartas_jugadas() 
            mostrar_primer_carta()

def tocar_boton_6 ():
            global elegir2, mostrar_boton6
            mostrar_boton6 += 1
            elegir2 = 2 
            carta6 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=5,column=6)
            carta_jug_22 = tkinter.Label (root, image=baraja_imagen[jugador_2[2]], width=130, height=200).grid(row=9,column=5)
            tapar_boton6 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=6)
            contar_cartas_jugadas() 
            mostrar_primer_carta()


def inicio (): 
    tapar_texto_inicio3 =tkinter.Label(root, textvariable=salida_nombre_1 ,bg="tomato", width=50, height=1, font=("arial",16,)).grid(row=3,column=0,columnspan=3)
    tapar_texto_inicio2 =tkinter.Label(root, textvariable=salida_nombre_2 ,bg="blue",   width=50, height=1, font=("arial",16,)).grid(row=3,column=4,columnspan=3)
    salida_nombre_1.set(f"{nombre_1.get()}")
    salida_nombre_2.set(f"{nombre_2.get()}")
    repartir_cartas()


def turno_jug1 ():
    if mostrar_boton1 == 0:
        boton1 = tkinter.Button (root, text="Jugar",activebackground="yellow", cursor="hand2",command=tocar_boton_1).grid(row=6,column=0)
    if mostrar_boton2 == 0:
        boton2 = tkinter.Button (root, text="Jugar",activebackground="yellow", cursor="hand2",command=tocar_boton_2).grid(row=6,column=1)
    if mostrar_boton3 == 0:
        boton3 = tkinter.Button (root, text="Jugar",activebackground="yellow", cursor="hand2",command=tocar_boton_3).grid(row=6,column=2)
    if mostrar_boton4 == 0:
        boton4 = tkinter.Button (root, text="------",activebackground="yellow",command=tocar_boton_4, state="disabled").grid(row=6,column=4)
    if mostrar_boton5 == 0:
        boton5 = tkinter.Button (root, text="------",activebackground="yellow",command=tocar_boton_5, state="disabled").grid(row=6,column=5)
    if mostrar_boton6 == 0:
        boton6 = tkinter.Button (root, text="------",activebackground="yellow",command=tocar_boton_6, state="disabled").grid(row=6,column=6)

def turno_jug2 ():
    if mostrar_boton1 == 0:
        boton1 = tkinter.Button (root, text="------",activebackground="yellow",command=tocar_boton_1, state="disabled").grid(row=6,column=0)
    if mostrar_boton2 == 0:
        boton2 = tkinter.Button (root, text="------",activebackground="yellow",command=tocar_boton_2, state="disabled").grid(row=6,column=1)
    if mostrar_boton3 == 0:
        boton3 = tkinter.Button (root, text="------",activebackground="yellow",command=tocar_boton_3, state="disabled").grid(row=6,column=2)
    if mostrar_boton4 == 0:
        boton4 = tkinter.Button (root, text="Jugar",activebackground="yellow", cursor="hand2",command=tocar_boton_4).grid(row=6,column=4)
    if mostrar_boton5 == 0:
        boton5 = tkinter.Button (root, text="Jugar",activebackground="yellow", cursor="hand2",command=tocar_boton_5).grid(row=6,column=5)
    if mostrar_boton6 == 0:
        boton6 = tkinter.Button (root, text="Jugar",activebackground="yellow", cursor="hand2",command=tocar_boton_6).grid(row=6,column=6)            


def tapar_todos_botones ():
    tapar_boton1 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=0)
    tapar_boton2 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=1)
    tapar_boton3 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=2)
    tapar_boton4 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=4)
    tapar_boton5 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=5)
    tapar_boton6 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=6)


def mostrar_primer_carta():
    if (puntos_juego_jugador1 + puntos_juego_jugador2) %2 == 0:
        if carta_jugada_n > 0 and carta_jugada_n %2 == 1:
            label_su_turno = tkinter.Label(root,bg="light grey",width=17, height=2).grid(row=4,column=0)
            label_su_turno = tkinter.Label(root,text= "Su Turno", font=("arial",14),bg="gold",width=10, height=1).grid(row=4,column=4)
            carta_jug_22 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=9,column=5)
            label_tapar_mensaje1 = tkinter.Label(root,bg="light grey",width=40, height=2).grid(row=7,column=0,columnspan=3)
            label_tapar_mensaje2 = tkinter.Label(root,bg="light grey",width=40, height=2).grid(row=7,column=4,columnspan=3)
            turno_jug2()
                
        elif carta_jugada_n > 0 and carta_jugada_n %2 == 0:
            label_su_turno = tkinter.Label(root,bg="light grey",width=17, height=2).grid(row=4,column=4)
            label_su_turno = tkinter.Label(root,text= "Su Turno", font=("arial",14),bg="gold",width=10, height=1).grid(row=4,column=0)
            turno_jug1()
            jugar()


    elif (puntos_juego_jugador1 + puntos_juego_jugador2) %2 == 1:
        if carta_jugada_n > 0 and carta_jugada_n %2 == 1:
            label_su_turno = tkinter.Label(root,bg="light grey",width=17, height=2).grid(row=4,column=4)
            label_su_turno = tkinter.Label(root,text= "Su Turno", font=("arial",14),bg="gold",width=10, height=1).grid(row=4,column=0)
            carta_jug_11 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=9,column=1)
            label_tapar_mensaje1 = tkinter.Label(root,bg="light grey",width=40, height=2).grid(row=7,column=4,columnspan=3)
            label_tapar_mensaje2 = tkinter.Label(root,bg="light grey",width=40, height=2).grid(row=7,column=0,columnspan=3)
            turno_jug1 ()
        elif carta_jugada_n > 0 and carta_jugada_n %2 == 0:
            label_su_turno = tkinter.Label(root,bg="light grey",width=17, height=2).grid(row=4,column=0)
            label_su_turno = tkinter.Label(root,text= "Su Turno", font=("arial",14),bg="gold",width=10, height=1).grid(row=4,column=4)
            turno_jug2 ()
            jugar()


def tareas_punto_jug1 ():
    labelpuntos1 = tkinter.Label(root,text=" Juego Gandado ",bg="green",font=("arial",18)).grid(row=7,column=0,columnspan=3)
    labelpuntos2 = tkinter.Label(root,bg="light grey",width=40, height=2).grid(row=7,column=4,columnspan=3)
    label_su_turno = tkinter.Label(root,bg="light grey",width=17, height=2).grid(row=4,column=0)
    label_su_turno = tkinter.Label(root,bg="light grey",width=17, height=2).grid(row=4,column=4)
    label_mostrar_partidas_jug1 = tkinter.Label(root,bg="light grey", text=f"Juegos ganados {puntos_juego_jugador1}", font=("arial",12)).grid(row=7,column=0)
    label_mostrar_partidas_jug2 = tkinter.Label(root,bg="light grey", text=f"Juegos ganados {puntos_juego_jugador2}", font=("arial",12)).grid(row=7,column=4)
    siguiente_juego= tkinter.Button (root, text=" Repartir ",bg="orange",activebackground="yellow", cursor="hand2",command=repartir_cartas).grid(row=2,column=3)

def tareas_punto_jug2 ():
    labelpuntos2 = tkinter.Label(root,text=" Juego Ganado ",bg="green",font=("arial",18)).grid(row=7,column=4,columnspan=3) 
    labelpuntos1 = tkinter.Label(root,bg="light grey",width=40, height=2).grid(row=7,column=0,columnspan=3)
    label_su_turno = tkinter.Label(root,bg="light grey",width=17, height=2).grid(row=4,column=0)
    label_su_turno = tkinter.Label(root,bg="light grey",width=17, height=2).grid(row=4,column=4)
    label_mostrar_partidas_jug1 = tkinter.Label(root,bg="light grey", text=f"Juegos ganados {puntos_juego_jugador1}", font=("arial",12)).grid(row=7,column=0)
    label_mostrar_partidas_jug2 = tkinter.Label(root,bg="light grey", text=f"Juegos ganados {puntos_juego_jugador2}", font=("arial",12)).grid(row=7,column=4)
    siguiente_juego= tkinter.Button (root, text=" Repartir ",bg="orange",activebackground="yellow", cursor="hand2",command=repartir_cartas).grid(row=2,column=3)


def jugar ():
    global puntos_juego_jugador1, puntos_juego_jugador2, puntos_ronda_jugador1, puntos_ronda_jugador2, ronda

    if ronda <3:
    
            carta_jug_1 = jugador_1[elegir1]
            carta_jug_2 = jugador_2[elegir2]
            

            primer_ronda=""

            if valor_cartas[carta_jug_1] > valor_cartas[carta_jug_2]:
                puntos_ronda_jugador1 += 1
                label_mostrar_puntos_ronda_jug1 = tkinter.Label(root,bg="light grey", text=f"Puntos de juego {puntos_ronda_jugador1}", font=("arial",12)).grid(row=9,column=0)
                label_mostrar_puntos_ronda_jug2 = tkinter.Label(root,bg="light grey", text=f"Puntos de juego {puntos_ronda_jugador2}", font=("arial",12)).grid(row=9,column=4)
                
                if ronda == 0: 
                    primer_ronda = "mano_1_jug_1"

            elif valor_cartas[carta_jug_2] > valor_cartas[carta_jug_1]:
                puntos_ronda_jugador2 += 1
                label_mostrar_puntos_ronda_jug1 = tkinter.Label(root,bg="light grey", text=f"Puntos de juego {puntos_ronda_jugador1}", font=("arial",12)).grid(row=9,column=0)
                label_mostrar_puntos_ronda_jug2 = tkinter.Label(root,bg="light grey", text=f"Puntos de juego {puntos_ronda_jugador2}", font=("arial",12)).grid(row=9,column=4)
                if ronda == 0: 
                    primer_ronda = "mano_1_jug_2"
            else:
                labelpuntos = tkinter.Label(root,text="       Pardas       ",font=("arial",18),bg="gold").grid(row=7,column=0,columnspan=3)
                labelpuntos = tkinter.Label(root,text="       Pardas       ",font=("arial",18),bg="gold").grid(row=7,column=4,columnspan=3)
                puntos_ronda_jugador1 += 1
                puntos_ronda_jugador2 += 1


            ronda += 1



            if puntos_ronda_jugador1 >=2 or puntos_ronda_jugador2 >= 2:
                if puntos_ronda_jugador1 == 2 and puntos_ronda_jugador2 == 2:
                    if primer_ronda == "mano_1_jug_1":
                        puntos_juego_jugador1 += 1
                        tareas_punto_jug1()
                        tapar_todos_botones ()
                        
                    else:
                        puntos_juego_jugador2 += 1
                        tareas_punto_jug2()
                        tapar_todos_botones ()
                        
                elif puntos_ronda_jugador1 == 3 and puntos_ronda_jugador2 == 3:
                    if (puntos_juego_jugador1 + puntos_juego_jugador2) % 2 == 1:
                        puntos_juego_jugador1 += 1
                        tareas_punto_jug1()
                        tapar_todos_botones ()
                        
                    else:
                        puntos_juego_jugador2 += 1
                        tareas_punto_jug2()
                        tapar_todos_botones ()
                
                elif puntos_ronda_jugador1 >= 2 and puntos_ronda_jugador2 <3:
                    puntos_juego_jugador1 += 1
                    tareas_punto_jug1()
                    tapar_todos_botones ()
                    
                
                elif puntos_ronda_jugador2 >= 2 and puntos_ronda_jugador1 <3:
                    puntos_juego_jugador2 += 1
                    tareas_punto_jug2()
                    tapar_todos_botones ()
                    

                if puntos_juego_jugador1 == 3: ### cambiar por 15
                    labelpuntos1 = tkinter.Label(root,text="Ganaste. Felicitaciones!!",bg="green",font=("arial",18)).grid(row=7,column=0,columnspan=3)
                    labelpuntos2 = tkinter.Label(root,bg="light grey",width=40, height=2).grid(row=7,column=4,columnspan=3)
                    boton_otra_partida= tkinter.Button (root, text="¿Otra Partida?",bg="orange", activebackground="yellow", cursor="hand2",command=repartir_cartas).grid(row=2,column=3)
                    
                if puntos_juego_jugador2 == 3: ### cambiar por 15 
                    labelpuntos2 = tkinter.Label(root,text="Ganaste. Felicitaciones!!",bg="green",font=("arial",18)).grid(row=7,column=4,columnspan=3)
                    labelpuntos1 = tkinter.Label(root,bg="light grey",width=40, height=2).grid(row=7,column=0,columnspan=3)
                    boton_otra_partida= tkinter.Button (root, text="¿Otra Partida?",bg="orange", activebackground="yellow", cursor="hand2",command=repartir_cartas).grid(row=2,column=3)
                    
                puntos_ronda_jugador1 = 0
                puntos_ronda_jugador2 = 0
                ronda =0
                    
                    
                  

baraja = ["1 de espada", "1 de basto", 
 "7 de espada", "7 de oro", 
 "3 de oro","3 de basto" ,"3 de copa" , "3 de espada", 
 "2 de oro","2 de basto" ,"2 de copa" , "2 de espada",
 "1 de oro", "1 de copa", 
 "12 de oro","12 de basto" ,"12 de copa" , "12 de espada", 
 "11 de oro","11 de basto" ,"11 de copa" , "11 de espada", 
 "10 de oro","10 de basto" ,"10 de copa" , "10 de espada", 
 "7 de basto", "7 de copa", 
 "6 de oro","6 de basto" ,"6 de copa" , "6 de espada", 
 "5 de oro","5 de basto" ,"5 de copa" , "5 de espada", 
 "4 de oro","4 de basto" ,"4 de copa" , "4 de espada" ]


valor_cartas = {"1 de espada":14,
 "1 de basto":13, 
 "7 de espada":12,
 "7 de oro":11, 
 "3 de oro":10,"3 de basto":10 ,"3 de copa":10 , "3 de espada":10, 
 "2 de oro":9,"2 de basto":9 ,"2 de copa":9 , "2 de espada":9,
 "1 de oro":8, "1 de copa":8, 
 "12 de oro":7,"12 de basto":7 ,"12 de copa":7 , "12 de espada":7, 
 "11 de oro":6,"11 de basto":6 ,"11 de copa":6 , "11 de espada":6, 
 "10 de oro":5,"10 de basto":5 ,"10 de copa":5 , "10 de espada":5, 
 "7 de basto":4, "7 de copa":4, 
 "6 de oro":3,"6 de basto":3 ,"6 de copa":3 , "6 de espada":3, 
 "5 de oro":2,"5 de basto":2 ,"5 de copa":2 , "5 de espada":2, 
 "4 de oro":1,"4 de basto":1 ,"4 de copa":1 , "4 de espada":1}




#imagenes de cartas
espada1 = tkinter.PhotoImage (file="1espada.png")
espada2 = tkinter.PhotoImage (file="2espada.png")
espada3 = tkinter.PhotoImage (file="3espada.png")
espada4 = tkinter.PhotoImage (file="4espada.png")
espada5 = tkinter.PhotoImage (file="5espada.png")
espada6 = tkinter.PhotoImage (file="6espada.png")
espada7 = tkinter.PhotoImage (file="7espada.png")
espada10 = tkinter.PhotoImage (file="10espada.png")
espada11 = tkinter.PhotoImage (file="11espada.png")
espada12 = tkinter.PhotoImage (file="12espada.png")

basto1 = tkinter.PhotoImage (file="1basto.png")
basto2 = tkinter.PhotoImage (file="2basto.png")
basto3 = tkinter.PhotoImage (file="3basto.png")
basto4 = tkinter.PhotoImage (file="4basto.png")
basto5 = tkinter.PhotoImage (file="5basto.png")
basto6 = tkinter.PhotoImage (file="6basto.png")
basto7 = tkinter.PhotoImage (file="7basto.png")
basto10 = tkinter.PhotoImage (file="10basto.png")
basto11 = tkinter.PhotoImage (file="11basto.png")
basto12 = tkinter.PhotoImage (file="12basto.png")

oro1 = tkinter.PhotoImage (file="1oro.png")
oro2 = tkinter.PhotoImage (file="2oro.png")
oro3 = tkinter.PhotoImage (file="3oro.png")
oro4 = tkinter.PhotoImage (file="4oro.png")
oro5 = tkinter.PhotoImage (file="5oro.png")
oro6 = tkinter.PhotoImage (file="6oro.png")
oro7 = tkinter.PhotoImage (file="7oro.png")
oro10 = tkinter.PhotoImage (file="10oro.png")
oro11 = tkinter.PhotoImage (file="11oro.png")
oro12 = tkinter.PhotoImage (file="12oro.png")

copa1 = tkinter.PhotoImage (file="1copa.png")
copa2 = tkinter.PhotoImage (file="2copa.png")
copa3 = tkinter.PhotoImage (file="3copa.png")
copa4 = tkinter.PhotoImage (file="4copa.png")
copa5 = tkinter.PhotoImage (file="5copa.png")
copa6 = tkinter.PhotoImage (file="6copa.png")
copa7 = tkinter.PhotoImage (file="7copa.png")
copa10 = tkinter.PhotoImage (file="10copa.png")
copa11 = tkinter.PhotoImage (file="11copa.png")
copa12 = tkinter.PhotoImage (file="12copa.png")

dorso = tkinter.PhotoImage (file="Vacio.png")


baraja_imagen = {
"1 de espada":espada1, "2 de espada":espada2, "3 de espada":espada3, "4 de espada":espada4, "5 de espada":espada5,
 "6 de espada":espada6, "7 de espada":espada7, "10 de espada":espada10, "11 de espada":espada11, "12 de espada":espada12,

 "1 de basto":basto1, "2 de basto":basto2, "3 de basto":basto3, "4 de basto":basto4, "5 de basto":basto5, 
 "6 de basto":basto6, "7 de basto":basto7, "10 de basto":basto10, "11 de basto":basto11, "12 de basto":basto12, 

 "1 de oro":oro1, "2 de oro":oro2, "3 de oro":oro3, "4 de oro":oro4, "5 de oro":oro5, 
 "6 de oro":oro6, "7 de oro":oro7, "10 de oro":oro10, "11 de oro":oro11, "12 de oro":oro12, 

 "1 de copa":copa1, "2 de copa":copa2, "3 de copa":copa3, "4 de copa":copa4, "5 de copa":copa5, 
 "6 de copa":copa6, "7 de copa":copa7, "10 de copa":copa10, "11 de copa":copa11, "12 de copa":copa12,
 "dorso":dorso}




#titulo de ventana
label =tkinter.Label(root, text="Truco Simple", bg="gold", width=110, height=1, font=("arial",16)).grid(row=0,column=0,columnspan=7)

#Titulos 
nombre_1 = tkinter.StringVar ()
nombre_2 = tkinter.StringVar ()
salida_nombre_1 = tkinter.StringVar ()
salida_nombre_2 = tkinter.StringVar ()

label_ingrese_nombre1 =tkinter.Label(root, text="Ingresá tu nombre", bg="tomato", width=15, height=1, font=("arial",11)).grid(row=3,column=0)
entry_ingreso_nombre1 = tkinter.Entry (root,textvariable=nombre_1, font=("arial",18,),bg="white").grid(row=3,column=1,columnspan=1)
label_ingrese_nombre2 =tkinter.Label(root, text="Ingresá tu nombre", bg="blue", width=15, height=1, font=("arial",11)).grid(row=3,column=4)
entry_ingreso_nombre2 = tkinter.Entry (root,textvariable=nombre_2, font=("arial",18,),bg="white").grid(row=3,column=5,columnspan=1)

boton_comienzo = tkinter.Button (root, text="Iniciar Juego",activebackground="yellow",bg="orange", cursor="hand2",command=inicio).grid(row=2,column=3)

# Mesa de Juego
label2 =tkinter.Label(root, text="Carta jugada", bg="tomato", width=20, height=1, font=("arial",16)).grid(row=8,column=0,columnspan=3)
label3 =tkinter.Label(root, text="Carta jugada", bg="blue", width=20, height=1, font=("arial",16)).grid(row=8,column=4,columnspan=3)

#Separadores 
frame_separador1 = tkinter.Frame(root, bg="light grey",height=20).grid(row=2,column=0)
frame_separador10 = tkinter.Frame(root, bg="light grey",height=20).grid(row=10,column=0)
frame_separador2 = tkinter.Frame(root, bg="light grey",height=20).grid(row=4,column=0)
frame_separador3 = tkinter.Frame(root, bg="light grey",height=60).grid(row=7,column=0)
frame_separador4 = tkinter.Frame(root, bg="light grey",height=20).grid(row=9,column=0)
label4 = tkinter.Label (root, bg="light grey",width=10, height=2).grid(row=6,column=3)
label_su_turno = tkinter.Label(root,bg="light grey",width=2, height=2).grid(row=4,column=4)
label_tamaño_boton_otro_juego = tkinter.Label(root,bg="light grey",width=1, height=2).grid(row=2,column=0)



# Botones tapados
boton1 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=0)
boton2 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=1)
boton3 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=2)
boton4 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=4)
boton5 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=5)
boton6 = tkinter.Label (root, bg="light grey", width=10, height=2).grid(row=6,column=6)


#separadores verticales

frame_separador_vertical = tkinter.Frame(root, bg="black",width=5,height=580).grid(row=2,column=3,rowspan=12)


# Cartas inicio de Jugador 1   
carta1 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=5,column=0)
carta2 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=5,column=1)
carta3 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=5,column=2)
carta_jug_11 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=9,column=1)

# Cartas inicio de Jugador 2
carta4 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=5,column=4)
carta5 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=5,column=5)
carta6 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=5,column=6)
carta_jug_22 = tkinter.Label (root, image=baraja_imagen["dorso"], width=130, height=200).grid(row=9,column=5)



carta_jugada_n = 0


puntos_ronda_jugador1 = 0
puntos_ronda_jugador2 = 0


puntos_juego_jugador1 = 0
puntos_juego_jugador2 = 0

ronda = 0



root.mainloop()
