from numpy import *
matriz = array([
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,1,1,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
])
coordenadas={
    "x" : [],
    "y" : []
}
area_mapa = len(matriz)-1

def GameOfLife(numero):
    """Funcion que Recibe un numero y modifica la matriz cada turno

    Arguments:
        numero int -- numero de veces a repetir el ciclo de vida
    """
    for _ in range(0,numero):
        coordenadas={
        "x" : [],
        "y" : []
        }
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                contador=0
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        auxX=x; auxY=y
                        if x > area_mapa:  x=0
                        elif x < 0: x = area_mapa
                        if y > area_mapa:  y=0
                        elif y < 0: y = area_mapa
                        if matriz[x][y] == 1: contador+=1 
                        x=auxX; y=auxY
                if matriz[i][j]==0:
                    if contador == 3:
                        coordenadas["x"].append(i)
                        coordenadas["y"].append(j)
                elif matriz[i][j]==1:
                    contador -=1
                    if contador < 2 or contador > 3:
                        coordenadas["x"].append(i)
                        coordenadas["y"].append(j)
        coord = list(coordenadas.values())
        for i in range(len(coord[0])):
            if matriz[coord[0][i]][coord[1][i]] == 0:
                matriz[coord[0][i]][coord[1][i]] = 1
            else:
                matriz[coord[0][i]][coord[1][i]] = 0

if __name__ == "__main__":
    print(matriz)
    GameOfLife(1)
    print(matriz)