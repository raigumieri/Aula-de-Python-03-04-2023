#Repetições aninhadas

tabuada=1
número=1
while tabuada <= 10: 
    print("%d x %d = %d" % (tabuada, número, tabuada * número))
número+=1
if número == 11: 
    número = 1
    tabuada=1

#---------------------------------------------------------------------
#Listagem 6.1 – Uma lista vazia
L=[] 

#Listagem 6.2 – Uma lista com três elementos 
Z=[ 15, 8, 9 ]

#Listagem 6.3 – Acesso a uma lista
Z=[15,8,9]
Z[0]
Z[1]
Z[2]

#Listagem 6.4 – Modificação de uma lista
Z=[15,8,9]
Z[0]

Z[0]=7
Z[0]
Z [7, 8, 9]

#---------------------------------------------------------------------
#Listagem 6.5 – Cálculo da média

notas= [6,7,5,8,9]
soma = 0
x = 0

while x<5:
    soma+= notas[x]
    x+=1
    print("Média: %5.2f" % (soma/x)
          
#---------------------------------------------------------------------
#Listagem 6.6 – Cálculo da média com notas digitadas

notas=[0,0,0,0,0]
soma=0
x=0

while x<5:
    notas[x] = float(input("Nota %d:" % x)) 
    soma += notas[x] 
    x += 1 
X = 0

while x<5:
    print("Nota %d: %6.2f" % (x, notas[x])) 
    x += 1 
    print("Média: %5.2f" % (soma/x))

#---------------------------------------------------------------------
#Listagem 6.7 – Apresentação de números

números=[0,0,0,0,0]
x=0
while x<5:
    números[x]=int(input("Número %d:" % (x+1))) 
    x+=1
while True:
    escolhido= int(input("Que posição você quer imprimir (0 para sair:"))
    if escolhido == 0:
        break
    print("Você escolheu o número: %d" % (números[escolhido-1]))
    
#---------------------------------------------------------------------   
#Listagem 6.8 – Tentativa de copiar listas

L = [1,2,3,4,5]
V = L
L
V

V[0] = 6
V
L

#--------------------------------------------------------------------- 
#Listagem 6.9 – Cópia de listas

L = [1,2,3,4,5]
V = L[:]
V[0] = 6
L
V

#--------------------------------------------------------------------- 
#Listagem 6.10 – Fatiamento de listas

L = [1,2,3,4,5]

L[0:5]
L[:5]
L[:-1]
L[1:3]
L[1:4]
L[3:]
L[:3]
L[-1]

#--------------------------------------------------------------------- 
#Listagem 6.11 – Tamanho de listas

L = [12,9,5]
len(L)

V = []
len(V)

#--------------------------------------------------------------------- 
#Listagem 6.14 – Adição de elementos à lista

L = []
L.append("a")
L

L.append("b")
L

L.append("c")
L 

len(L)

#--------------------------------------------------------------------- 
#Listagem 6.15 – Adição de elementos à lista

L = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n==0:
        break
    L.append(n)
x = 0
while x< len(L):
    print(L[x])
x=x + 1

#--------------------------------------------------------------------- 
#Listagem 6.16 – Adição de listas

L = []
L = L+[1]
L 

L += [2]
L 

L += [3,4,5]
L

#--------------------------------------------------------------------- 
#Listagem 6.17 – Adição de elementos e listas

L = ["a"]
L.append("b")
L

L.extend(["c"])
L

L.append(["d","e"])
L

L.extend(["f","g","h"])
L

#--------------------------------------------------------------------- 
#Listagem 6.19 – Remoção de elementos

L = ["a","b","c"]
del L[1]
L     

del L[0]
L 

#--------------------------------------------------------------------- 
#Listagem 6.20 – Remoção de fatias

L = list(range(101))
del L[1:99]
L

#--------------------------------------------------------------------- 
#Listagem 6.21 – Simulação de uma fila de banco

último = 10
fila = list(range(1,último+1)) 

while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação= input("Operação(F,A ou S):")
    if operação == "A":
        if(len(fila))>0:
            atendido = fila.pop(0)
            print("Cliente %d atendido" % atendido)
    else:
        print("Fila vazia! Ninguém para atender.") 
    elif operação == "F": 
        último += 1  # Incrementa o ticket do novo cliente
        fila.append(último)
    elif operação == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")
        
#---------------------------------------------------------------------
#Listagem 6.23 – Pesquisa sequencial

L = [15,7,27,39]
p = int(input("Digite o valor a procurar:"))
achou = False 
x = 0 
while x < len(L):
    if L[x] == p:
        achou = True
        break
    x += 1
    if achou:
        print("%d achado na posição %d" % (p,x))
    else:
        print("%d não encontrado" % p)
        
#---------------------------------------------------------------------
#Listagem 6.26 – Pesquisa usando for

L = [7,9,10,12]
p = int(input("Digite um número a pesquisar:"))
for e in L:
    if e == p:
        print("Elemento encontrado!")
        break
    else:
        print("Elemento não encontrado.")
        
#---------------------------------------------------------------------


        
        
        
            
        
            
     




      
