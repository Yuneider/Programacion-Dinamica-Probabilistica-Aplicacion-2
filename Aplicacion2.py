'''
Imagine que tiene $5000 COP Para invertir y que tendrá la oportunidad de hacerlo
en cualquiera de dos inversiones (A o B) al principio de los proximos tres años.
Existe incertidumbre respecto al rendimiento de ambas invversiones. Si se invierte
en A, se puede perder todo el dinero o (con probabilidad más alta) obtener $10000 COP
(una ganancia de $5000 COP) al final del año. Si se invierte en B, se pueden obtener 
$5000 COP o (con una probabilidad más baja) obtener $10000 al terminar el año.
Las probabilidades para estos eventos son las siguientes:

Inversión |  Cantidad Obtenida (COP) | Probabilidad 
__________|__________________________|_______________
          |                          |                
     A    |             0            |      0.3  
__________|__________________________|_______________
          |                          |        
     A    |           10000          |      0.7
__________|__________________________|_______________
          |                          |       
     B    |            5000          |      0.9  
__________|__________________________|_______________
          |                          |
     B    |           10000          |      0.1
__________|__________________________|_______________

Se le permite hacer (a lo sumo) una inversión al año y solo puede invertir $5000 COP
cada vez (Cualquier cantidad adicional de dinero acumulada queda inútil).

Utilize programación dinámica probabilística para encontrar la política de inversión
que maximice la cantidad de dinero esperada que tendrá despues de los tres años.

Ejecicio tomado de: https://www.youtube.com/watch?v=4YtPUNsg6k4

SOLUCIÓN:

En primer lugar creamos una lista de cuatro listas (por las cuatro etapas), 
en las cuales insertamos la posible cantidad que logramos adquirir anuelamente.
''' 

''' En DecisionOptia guardaremos todas las decisiones, esto con el propósito de guarda
    en cada iteración la decision que maximice el resultado de la inverison. '''

import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread('DiagramaProbabilidades.jpg')
plt.axis('off')
plt.title("Diagrama De Probabilidades")
plt.imshow(image)
plt.show()


DecisionOPtima = []

ValorOptimo = [[5000],[0,5000,10000],[0,5000,10000,15000],[0,5000,10000,15000,20000]]

''' Luego de esto, procedemos a encontrar el valor óptimo de cada estado a partir
    de la formula correspodiente para la decision A:
    f_n (s_n,x_A )=0.3 [f_(n+1)^* (s_(n-5000) )]+0.7 [f_(n+1)^* (s_(n+5000) )] '''

n = len(ValorOptimo)-2

''' Cabe resaltar que la lista de listas debe ser recorrida de atras para adelante,
    insertand el valor óptimo de la fución en la posición de cada estado '''

while n >=0:
     for i in range(len(ValorOptimo[n])):
          if ValorOptimo[n][i]!=0:
               ValorOptimo[n][i] = 0.3*(ValorOptimo[n+1][i-1])+0.7 *(ValorOptimo[n+1][i+1])
               DecisionOPtima.append("A")
     n = n-1

''' De la misma forma, calculamos el valor óptimo de cada estado, pero esta vez, a partir
    de la decision B:
    f_n (s_n,x_B )=0.9 [f_(n+1)^* (s_n )]+0.1 [f_(n+1)^* (s_(n+5000) )] '''

n = len(ValorOptimo)-2

''' Hay que tener en cuenta, que en lugar de reemplzarlo por el valor acutal de la lista   
    debemos comprar si es cual es el mayor, siendo ese el valor que perdurará '''

while n >=0:
     for i in range(len(ValorOptimo[n])):
          if ValorOptimo[n][i]!=0:
               if(ValorOptimo[n][i] < 0.9*(ValorOptimo[n+1][i])+0.1 *(ValorOptimo[n+1][i+1])):
                    ValorOptimo[n][i] = 0.9*(ValorOptimo[n+1][i])+0.1 *(ValorOptimo[n+1][i+1])
                    DecisionOPtima.insert(i,"B")
     n = n-1


image = img.imread('DistribucionProbabilidad.jpg')
plt.axis('off')
plt.title("Distribución De Probabilidad")
plt.imshow(image)
plt.show()


print(DecisionOPtima)

''' Como podemos observar la lista de decisiones optimas está completamente llena de A,
    lo que quiere decir, que en cada año, la desicion que maximizará la inversión,
    es invertir en A'''