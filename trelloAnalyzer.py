import json
import sys

NAME = "name"
ID = "id"
DESC = "desc"
CLOSED = "closed"
LISTS = "lists"
CARDS = "cards"
CHECKLISTS = "checklists"
IDBOARD = "idBoard"
IDLIST = "idList"
IDCHECKLISTS = "idChecklists"
IDMEMBERS = "idMembers"
MEMBERS = "members"


#Diccionario con lista, tarjeta y miembros
dicListaTar={}

with open(sys.argv [1] , encoding="utf8") as json_file:
    trello_board = json.load(json_file)
print ("Tablero: " + trello_board [NAME])

# Recorremos todas las tarejtas
for trello_card in trello_board [CARDS] :    
    #De cada tarjeta sacamos la lista
    #Creamos entrada en el diccionario de listas, si esta no la tiene ya
    if trello_card [IDLIST]  not in dicListaTar:
        dicListaTar[trello_card [IDLIST] ]={}
    #Metemos la tarjeta en su lista y almacenamos sus miembros
    dicListaTar[trello_card [IDLIST]][trello_card[ID]]=trello_card [IDMEMBERS]
            
print("Tarjetas asignadas actualmente a usuarios por lista")

#Recorremos el diccionario



for trello_list in trello_board [LISTS] :

    print("-------------------------------------------------------")
    print("LISTA:")
    print(trello_list[NAME])
    print("-------------------------------------------------------")
    print("Tarjetas en esa lista : "+ str(len(dicListaTar[trello_list[ID]])))
    print("-------------------------------------------------------")
    print("Usuarios y sus tarjetas asignadas")

    listaUsuarios={}
    for tarjeta in dicListaTar[trello_list[ID]]:
        for usu in dicListaTar[trello_list[ID]][tarjeta]:
            if usu not in listaUsuarios:
                listaUsuarios[usu]=1
            else:
                listaUsuarios[usu]=listaUsuarios[usu]+1

    for usu in listaUsuarios:
        nombreCompleto=""
        for miembro in trello_board[MEMBERS]:
            if miembro[ID]==usu:
                nombreCompleto=miembro["fullName"]

        print (str(nombreCompleto)+ " " + str(listaUsuarios[usu]))
    
    