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

from typing import Sequence
from rtrace import trace
import images

# TODO
# da anidare in forma ricorsiva il controllo di ogni cuadrante


def ex1(input_file,  output_file):

   

    # prende input immagine
    img_in = images.load(input_file)

    # bg
    bg = img_in[0][0]

    # pulisci
    images.save(img_in, output_file)

    #img_in[1010][856]=(0,0,0)
    #images.save(img_in, output_file)

    colori = []
    colori = trova_divisione_4toCuadrante(img_in, bg, 0, 0, colori)
    # colori = trova_divisione_1erCuadrante(img_in, bg, 128, 128, colori)
    # colori = trova_divisione_2doCuadrante(img_in, bg, 218,402, colori)
    # colori = trova_divisione_3erCuadrante(img_in, bg, 218,100, colori)

    img_out = []
    img_out.append(bg)
    for colore in colori:
        img_out.append(colore)


    images.save(img_out,output_file )


def trova_divisione_4toCuadrante(img_in, bg, y, x, colori):
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
            return trova_divisione_4toCuadrante(img_in, bg, coord_y, coord_x, colori)
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
            colori.append(lista_tagliata[0])
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
            colori.append(lista_tagliata[0])
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
            colori.append(lista_tagliata[0])
            # img_in[coord_y][coord_x] = (255, 255, 255)
            # images.save(img_in, 'medium02TEST.out.png')
            return trova_divisione_3erCuadrante(img_in, bg, coord_y, coord_x, colori)
        
    return trova_divisione_4toCuadrante(img_in, bg,last_center_y,last_center_x, colori)


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


def trova_origine_y(img_in, colore, x, y):
    # max_len=len(img_in[y])
    while (True):
        if img_in[y][x+1] == colore:
            if img_in[y][x-1] == colore:
                break
        y = y+1

    return y


def trova_origine_x(img_in, colore, x, y):
    # max_len=len(img_in[x])
    while (True):
        if img_in[y+1][x] == colore:
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


if __name__ == '__main__':
    ex1('puzzles/hard01.in.png', 'hard01TEST.out.png')
