def LendoMatriz():

    global m, n, mat
    arq = open('matriz.dat')
    conteudo = arq.read()
    print(conteudo)

    numeros = conteudo.split()
    print(numeros)

    m = int(numeros[0])
    n = int (numeros[1])

    print('A Matriz tem {} linhas e {} colunas'.format (m, n))

    mat = []

    for i in range(m):
        linha = []
        for j in range(n):

            
            try:
                linha += [float(numeros[2+i*m + j])]
                
            except ValueError as err:
                print(err)
                linha += ['NaN']
                

        
        mat += [linha]

        
    print(mat)

def PrintMatriz():
        for i in range(m):
            for j in range(n):
                print(mat[i][j], end = ' ')
        print()


def MatrizAlinhadaFixa():
    for i in range(m):
        print('+', '-'*48, '+')
        for j in range(n):
            
            print('|{0:^15f}'.format(mat[i][j]), end = ' ')
        print('|')
    print('+', '-'*48, '+')

LendoMatriz()
print('\n\n')
PrintMatriz()
print('\n\n')
MatrizAlinhadaFixa()

