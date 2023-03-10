#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Una proprietaria terriera in California, Lida, eredita un
appezzamento di terreno. La superficie è modellata come un lotto
rettangolare di grandezza variabile. Il lotto di terra è
rappresentato come un'immagine codificata come lista di liste.

Per far fruttare l'appezzamento di terra, Lida decide di affittare la
terra ad altre persone. Per fare ciò, può decidere di dividere la
terra in quattro parti. Nel caso in cui decida di non affittare la sua
proprietà nessuna divisione è effettuata. Al contrario, nel caso in
cui la proprietà venga divisa in quattro sotto parti, delle linee di
demarcazione colorate vengono create, per tutelare i confini, appunto.
Le linee hanno uno spessore di un solo pixel. Non è dato sapere come
e dove le line verranno poste (non vi è una regolarità), e neppure
sappiamo quale è il colore che verrà usato a priori.  Conosciamo
solamente che le linee sono allineate agli assi.

I quattro locatari che ricevono le quattro proprietà potrebbero
prendere la solita decisione che Lida ha preso in precedenza oppure
no: essi potrebbero subaffittare ancora una volta le loro piccole
proprietà ad altre persone, oppure, potrebbero decidere di tenere la
terra tutta per loro. La decisione della suddivisione per ogni
locatario è indipendente alle altre. Per esempio, il locatario #1 può
decidere di subaffittare ancora, mentre il locatario #2 può tenere la
proprietà, mentre i locatari #3, #4 possono suddividere ancora. Quello
che sappiamo è che se subaffittano, dividono sempre in quattro
parti. Infatti, nel caso in cui dividano ancora la proprietà,
seguiranno una strategia simile di impostare i loro confini tracciando
delle linee di demarcazione degli stessi. Sicuramente useranno un
colore che è diverso dai colori usati da Lida (e da altri eventuali in
precedenza) tuttavia i quattro locatari usano il solito colore fra
loro, allo stesso livello di suddivisione.

NOTA: E' importante ricordare che il colore del background (bg) dell'
appezzamento non è dato (cioè non sappiamo a priori se il bg è
nero, bianco oppure blue). Sappiamo però che il colore di background
della terra NON è usato da nessuno dei locatari (ne da Lida) per
marcare i confini.

Il processo di suddivisione può continuare fino a quando tutti i
locatari in tutte gli appezzamenti decidono di smettere col subaffitto.
Questo processo descritto fino ad ora, ci porta all'immagine che è
data in input al vostro programma.

NOTA: Potete assumere che l'ipotetico appezzamento di terreno più
piccolo (rettangolo più piccolo possibile) abbia il lato più corto di
due pixel.

Riflettete bene sul problema e una volta che siete sicuri di una
soluzione, progettate su carta una soluzione (questa soluzione poi
deve essere descritta nella pseudo codice) e poi implementate un
programma ex1(input_file, output_file) che:
   - legge il file indicato dal parametro 'input_file' usando
     il modulo libreria 'images'.
   - pre-processa l'immagine, se necessario, e implementa una funzione
     *ricorsiva* per risolvere i requisiti sottostanti.
   - si deve contare tutte gli appezzamenti di terra che sono nell'
     immagine e restituire questo conteggio. Il programma deve
     restituire il numero di rettangoli con il colore del background
     dell'immagine che vi sono presenti. Riferendosi alla figura
     semplificata sottostante:

        # +++++++++++++++++++
        # +-1-|-2-|---------+
        # ++++a+++|----5----+
        # +-3-|-4-|---------+
        # ++++++++b++++++++++
        # +-------|--7-|-8--+
        # +---6---|++++c+++++
        # +-------|-10-|-9--+
        # +++++++++++++++++++

    l'approccio deve restituire un intero che corrisponde a 10 in
    questo caso (numero totale di rettangoli). I numeri posti nella
    figura soprastante sono stati inseriti solo per chiarire il
    concetto. (I dati sono privi di tali numeri inseriti, ovviamente).
    - infine, dato che l'agenzia immobiliare deve registrare
    tutti i confini che sono creati, il programma deve costruire un'
    immagine di output di grandezza 1x(N+1). L'immagine codifica come
    primo pixel il colore del background. Poi, deve codificare la
    gerarchia dei colori di tutti gli N colori usati per suddividere
    la terra in sotto rettangoli. La gerarchia dei colori e' definita
    "visitando" prima in profondita' il lotto in alto a sx, poi in
    alto a dx, poi in basso a sx, e infine in basso a dx. I colori
    devono essere salvati in ordine inverso rispetto alla visita
    effettuata. Con riferimento all'immagine semplificata precedente,
    assumendo che i colori dei confini di demarcazione siano descritti
    dalla lettere al loro centro, allora l'immagine di output deve
    contenere:
             out_colors = bg b c a


    Un altro esempio un pochino piu' complesso:

         +++++++++++++++++++++++++++++++++++++
         +-1-|-2-|---------|--------|--------+
         ++++a+++|----5----|---6----|----7---+
         +-3-|-4-|---------|--------|--------+
         ++++++++b+++++++++|++++++++c+++++++++
         +-------|--9-|-10-|--------|--------+
         +--8----|++++d++++|---13---|---14---+
         +-------|-11-|-12-|--------|--------+
         ++++++++++++++++++e++++++++++++++++++
         +-15|-16|---------|--------|-21|-22-+
         ++++f+++|---19----|---20---|+++g+++++
         +-17|-18|---------|--------|-23|--24+
         ++++++++h+++++++++|++++++++l+++++++++
         +-------|-26-|-27-|--------|-31-|-32+
         +--25---|++++m++++|---30---|+++n+++++
         +-------|-29-|-28-|--------|-33-|-34+
         +++++++++++++++++++++++++++++++++++++

         num. rect: 34
         gerarchia dei colori:
         bg e l n g h m f c b d a


NOTA: è vietato importare/usare altre librerie o aprire file tranne
quello indicato

NOTA: il sistema di test riconosce la presenza di ricorsione SOLO se
    la funzione/metodo ricorsivo è definita a livello esterno.  NON
    definite la funzione ricorsiva all'interno di un'altra
    funzione/metodo altrimenti fallirete tutti i test.
"""

# from typing import Sequence
# from rtrace import trace
import images


###

def ex1(input_file,  output_file):
    # prende input immagine
    img_in = images.load(input_file)

    # pulisci
    #images.save(img_in, output_file)

    # bg
    bg = img_in[0][0]
    lista_immaggine=[]
    lista_immaggine.append(img_in)
    colori=[]
    num_lotti=0
    colori,num_lotti=divide_et_impera(lista_immaggine,bg,colori,num_lotti)
    
    #Output dei colori
    img_out = [[]]
    img_out[0].append(bg)

    if colori :
        num_lotti=num_lotti
        for colore in colori:
            img_out[0].append(colore)
    else:
        num_lotti=1

    images.save(img_out,output_file )

    return num_lotti



#da farte una struttura ad albero quatiternario

#fare una funzione divide_et_impera
#che riceve in input una immaggine
#verifica se questa è una sottodivisione
#se è si, divide i quattro cuadranti della immmaggine, 
#  e richiama la stessa funzione in maniera ricorsiva passando come 
#parametro la lista delle immaggine (l'ordine di divisione sarebbe,
#  4to cuadrante, 1mo cuadrante, 2do cuadrante e 3er cuadrante)
# se è no, allora fare return del colore dell'immmagine.

def divide_1erCuadrante(immaggine,x,y,bg):
    centro_y=y
    centro_x=x
    #fare ciclo fino a zero (top y) O fino a trovare un'altra sottodivisione
    for y in range(y-1, 0, -1):
        
        if trova_fine_colonna_y_cuadrante_v2(immaggine[y][x-1:x+2],bg) == True:
            return  taglia_primo_cuadrante(immaggine,centro_x,centro_y)
    else:
        #vuol dire che è arrivato alla fine dell'immaggine 
        #senza trovare la divisione
        #taglia per il bordo con il colore
        # return taglia_primo_cuadrante(immaggine,centro_y-3,centro_x+2)
        return taglia_primo_cuadrante(immaggine,centro_x,centro_y)
    
def divide_2doCuadrante(immaggine,x,y,bg):
    centro_y=y
    centro_x=x
    #fare ciclo fino a zero (top y) O fino a trovare un'altra sottodivisione
    for y in range(y-1, 0, -1):
        if trova_fine_colonna_y_cuadrante_v2(immaggine[y][x-1:x+2],bg) == True:
            return  taglia_secondo_cuadrante(immaggine,centro_x,centro_y)
    else:
        #vuol dire che è arrivato alla fine dell'immaggine 
        #senza trovare la divisione
        #taglia per il bordo con il colore
        return taglia_secondo_cuadrante(immaggine,centro_x,centro_y)
    
def divide_3erCuadrante(immaggine,x,y,bg):
    centro_y=y
    centro_x=x
    #fare ciclo fino a max_y fino a trovare un'altra sottodivisione
    for y in range(y+1, len(immaggine), +1):
        if trova_fine_colonna_y_cuadrante_v2(immaggine[y][x-1:x+2],bg) == True:
            return  taglia_terzo_cuadrante(immaggine,centro_x,centro_y)
    else:
        #vuol dire che è arrivato alla fine dell'immaggine 
        #senza trovare la divisione
        #taglia per il bordo con il colore
        return taglia_terzo_cuadrante(immaggine,centro_x,centro_y)
    
def divide_4toCuadrante(immaggine,x,y,bg):
    centro_y=y
    centro_x=x
    #fare ciclo fino a max_y fino a trovare un'altra sottodivisione
    for y in range(y+1, len(immaggine), +1):
        if trova_fine_colonna_y_cuadrante_v2(immaggine[y][x-1:x+2],bg) == True:
            return  taglia_quarto_cuadrante(immaggine,centro_x,centro_y)
    else:
        #vuol dire che è arrivato alla fine dell'immaggine 
        #senza trovare la divisione
        #taglia per il bordo con il colore
        return taglia_quarto_cuadrante(immaggine,centro_x,centro_y)

def taglia_quarto_cuadrante(immaggine, da_x, da_y):
    immaggine= immaggine[da_y:]
    immaggine_tagliata=[]
    for y in range(len(immaggine)):
        immaggine_tagliata.append(immaggine[y][da_x:])
    return immaggine_tagliata

def taglia_terzo_cuadrante(immaggine, da_x, da_y):
    immaggine= immaggine[da_y:]
    immaggine_tagliata=[]
    for y in range(len(immaggine)):
        immaggine_tagliata.append(immaggine[y][:da_x])
    return immaggine_tagliata

def taglia_primo_cuadrante(immaggine, da_x, da_y):
    immaggine= immaggine[:da_y]
    immaggine_tagliata=[]
    for y in range(len(immaggine)):
        immaggine_tagliata.append(immaggine[y][da_x:])

    return immaggine_tagliata

def taglia_secondo_cuadrante(immaggine, da_x, da_y):
    immaggine= immaggine[:da_y]
    immaggine_tagliata=[]
    for y in range(len(immaggine)):
        immaggine_tagliata.append(immaggine[y][:da_x])

    return immaggine_tagliata

def divide_et_impera(lista_immaggini,bg,colori:list,num_lotti):

    for immaggine in lista_immaggini:
        if contiene_sottodivisioni(immaggine,bg)   ==True:
            
            #si deve trovare l'origine dell'immaggine
            #da divedere i 4 cuadranti dell'immaggine
            #aggiungere dentro una lista di immaggine
            #passarlo a divide_et_impera
            colore, origine_Y=colore_Y_sottodivisioni(immaggine,bg)
            #images.save(immaggine, 'fullcase01TEST.out.png')
            origine_x =trova_origine_x(immaggine,colore,0,origine_Y)

            #salvo il colore del origine del nodo
            colori.append(colore)

            new_list_immmaggine=[]

            #4to cuadrante
            immaggine_divisa_4tocuadrante=divide_4toCuadrante(immaggine,origine_x,origine_Y,bg)
            #images.save(immaggine_divisa_4tocuadrante, 'fullcase01TEST.out.png')
            new_list_immmaggine.append(immaggine_divisa_4tocuadrante)

            #3er cuadrante
            immaggine_divisa_3ercuadrante=divide_3erCuadrante(immaggine,origine_x,origine_Y,bg)
            #images.save(immaggine_divisa_3ercuadrante, 'fullcase01TEST.out.png')
            new_list_immmaggine.append(immaggine_divisa_3ercuadrante)

            #1er cuadrante
            immaggine_divisa_1ercuadrante=divide_1erCuadrante(immaggine,origine_x,origine_Y,bg)
            #images.save(immaggine_divisa_1ercuadrante, 'fullcase01TEST.out.png')
            new_list_immmaggine.append(immaggine_divisa_1ercuadrante)

            #2do cuadrante
            immaggine_divisa_2docuadrante=divide_2doCuadrante(immaggine,origine_x,origine_Y,bg)
            #images.save(immaggine_divisa_2docuadrante, 'fullcase01TEST.out.png')
            new_list_immmaggine.append(immaggine_divisa_2docuadrante)

            null,num_lotti= divide_et_impera(new_list_immmaggine,bg,colori,num_lotti) 
        else:
            # se non contiene sottodivissione, vuol dire che
            #si è arrivato alla fine se si deve ritornare il colore corrente
            #colore_corrente=immaggine[0][0]
            num_lotti+=1
            continue 
           
    return colori,num_lotti
            #return  None , num_lotti+1#colori.append(colore_corrente)

def contiene_sottodivisioni(immaggine, bg):
    for y in range(1, len(immaggine)):
        lista_tagliata = immaggine[y][1:]
        if trova_divisione(lista_tagliata, bg) == True:
            return True
    return False

def colore_Y_sottodivisioni(immaggine, bg):
    for y in range(1, len(immaggine)):
        lista_tagliata = immaggine[y][1:]
        if trova_divisione(lista_tagliata, bg) == True:
            return lista_tagliata[0] , y
    #TODO sistemare ritorno     
    #return False

def trova_divisione_4toCuadrante(img_in, bg, y, x, colori,lista_centri):
    #last_center
    last_center_y=y
    last_center_x=x
    for y in range(y+1, len(img_in)):
        lista_tagliata = img_in[y][x+1:]
        if trova_divisione(lista_tagliata, bg) == True:
            coord_y = y
            coord_x = trova_origine_x(img_in, lista_tagliata[0], x, y)
            colori.append(lista_tagliata[0])
            # img_in[coord_y][coord_x] = (255, 255, 255)
            # images.save(img_in, 'hard01TEST.out.png')
            lista_centri.append((coord_y,coord_x))
            return trova_divisione_4toCuadrante(img_in, bg, coord_y, coord_x, colori,lista_centri)
        
    # lista_centri=lista_centri[1:]
    # for centro in  reversed(lista_centri):
    #   x=trova_divisione_1erCuadrante(img_in, bg,centro[0],centro[1], [])
    #   colori.append(x)
    #   x=trova_divisione_2doCuadrante(img_in, bg,centro[0],centro[1], [])
    #   colori.append(x)
    #   x=trova_divisione_3erCuadrante(img_in, bg,centro[0],centro[1], [])
    #   colori.append(x)

    return trova_divisione_1erCuadrante(img_in, bg,last_center_y,last_center_x, colori)

def trova_divisione_1erCuadrante(img_in, bg, y, x, colori):
    #last_center
    last_center_y=y
    last_center_x=x
    for y in range(y-1, 0, -1):
        if trova_fine_colonna_y_cuadrante(img_in[y][x-1:x+2],bg) == True:
            break
        lista_tagliata = img_in[y][x+1:]
        if trova_divisione(lista_tagliata, bg) == True:
            coord_x = trova_origine_x(img_in, lista_tagliata[0], x, y)
            coord_y = y
            #colori.append(lista_tagliata[0])
            # img_in[coord_y][coord_x] = (255, 255, 255)
            # images.save(img_in, 'hard01TEST.out.png')
            return trova_divisione_1erCuadrante(img_in, bg, coord_y, coord_x, colori)
        
    return trova_divisione_2doCuadrante(img_in, bg, last_center_y,last_center_x, colori)

def trova_divisione_2doCuadrante(img_in, bg, y, x, colori):
    #last_center
    last_center_y=y
    last_center_x=x
    for y in range(y-1, 0, -1):
        if trova_fine_colonna_y_cuadrante(img_in[y][x-1:x+2],bg) == True:
            break
        lista_tagliata = img_in[y][:x]
        if trova_divisione(lista_tagliata, bg) == True:
            coord_x = trova_origine_x_inverso(img_in, lista_tagliata[0], x, y)
            coord_y = y
            #colori.append(lista_tagliata[0])
            # img_in[coord_y][coord_x] = (0, 0, 0)
            # images.save(img_in, 'rect02TEST.out.png')
            return trova_divisione_2doCuadrante(img_in, bg, coord_y, coord_x, colori)
    
    return trova_divisione_3erCuadrante(img_in, bg, last_center_y, last_center_x, colori)

def trova_divisione_3erCuadrante(img_in, bg, y, x, colori):
    #last_center
    last_center_y=y
    last_center_x=x
    for y in range(y+1, len(img_in)):
        if trova_fine_colonna_y_cuadrante(img_in[y][x-1:x+2],bg) == True:
            break
        lista_tagliata = img_in[y][:x]
        if trova_divisione(lista_tagliata, bg) == True:
            coord_x = trova_origine_x_inverso(img_in, lista_tagliata[0], x, y)
            coord_y = y
            #colori.append(lista_tagliata[0])
            # img_in[coord_y][coord_x] = (255, 255, 255)
            # images.save(img_in, 'medium02TEST.out.png')
            return trova_divisione_3erCuadrante(img_in, bg, coord_y, coord_x, colori)
        
    return colori

    #ritorno ultimo colore trovato
    #return img_in[last_center_y][last_center_x]

# tutti i colori devono essere uguali e diversi del colore_bg della lista X o Y passata
def trova_divisione(lista_colori, colore_bg):
    colore_iniziale = lista_colori[0]
    for colore in lista_colori:
        # se già uno è diverso, return false
        if colore_iniziale != colore or colore == colore_bg:
            return False
    return True

# controlla se gli estremi sono uguali colore, vuol dire
# che ha trovato la fine
# della colonna di colori
def trova_fine_colonna_y_cuadrante(lista_colori, colore_bg):
    if lista_colori[0] != colore_bg:
        if lista_colori[2] != colore_bg:
            return True
        
def trova_fine_colonna_y_cuadrante_v2(lista_colori, colore_bg):
    if lista_colori[0] != colore_bg:
        if lista_colori[1] != colore_bg:
            if lista_colori[2] != colore_bg:
             return True

def trova_origine_y(img_in, colore, x, y):
    # max_len=len(img_in[y])
    while (True):
        if img_in[y][x+1] == colore:
            if img_in[y][x-1] == colore:
                break
        y = y+1

    return y

#controlla sopra e sotto nello stesso asse delle X
#se trova che sono uguali, vuol dire che c'è la divisione su quel X
def trova_origine_x(img_in, colore, x, y):
    max_len_y=len(img_in)
    max_len_x=len(img_in[0])
    while (True):
        if y+1>max_len_y:
            if img_in[y+1][x] == colore :
                if img_in[y-1][x] == colore:
                     break
        else:
             if img_in[y-1][x] == colore:
                     break

        x = x+1
    return x

def trova_origine_x_inverso(img_in, colore, x, y):
    # max_len=len(img_in[x])
    while (True):
        if img_in[y+1][x] == colore:
            if img_in[y-1][x] == colore:
                break
        x = x-1
    return x


#if __name__ == '__main__':
    #ex1('puzzles/medium01.in.png', 'medium01TEST.out.png')
    #ex1('puzzles/fullcase01.in.png', 'fullcase01TEST.out.png')




