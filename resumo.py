import math


####################
# Impressão na tela
####################

# Impressão dos dados de entrada:
def imprime_entrada(ponto, vinculos, barra, quantidade_de_barras):
    print('\nDADOS DE ENTRADA: ')

    print('\n*************** Nós *****************')
    for i in range(len(ponto)):
        print(f'Ponto {ponto[i]}: x = {ponto[i][1]}, y = {ponto[i][2]}')

    print('\n************* Vínculos **************')
    for i in range(len(ponto) * 2):
        if i in vinculos:
            if i % 2 == 0:
                print(f'Vínculo no GLD = {i} (Nó {i / 2 - 1}, direção y)')
            else:
                print(f'Vínculo no GLD = {i} (Nó {i / 2 - 1 / 2}, direção x)')

    print('\n************* Barras ****************')
    for i in range(quantidade_de_barras):
        E, A, L, theta, ponto1, ponto2 = barra[i][0], barra[i][1], barra[i][2], barra[i][3], barra[i][8][0], \
            barra[i][9][0]
        print(
            f'Barra {i}: E = {E}, A = {A:.2f}, comprimento = {L:.2f}, theta = {theta:.2f} '
            f'rad ({math.degrees(theta):.2f})º, nós início -> fim: {ponto1} -> {ponto2}')


# Impressão dos cálculos:
def imprime_calculos(quantidade_de_barras, matrizes_de_rigidez_locais, matrizes_de_transformacao,
                       matrizes_de_rigidez_globais, matrizes_de_incidencia, matrizes_espalhadas, K, Kaa, Kbb, Kab, Kba):
    print('\nCÁLCULOS: ')
    for i in range(quantidade_de_barras):
        print(f'\n**Barra {i}**')
        print('\nMatriz de rigidez no sistema local:')
        print(matrizes_de_rigidez_locais[i])
        print('\nMatriz de transformacao da barra: ')
        print(matrizes_de_transformacao[i])
        print('\nMatriz de rigidez da barra no sistema global:')
        print(matrizes_de_rigidez_globais[i])
        print('\nMatriz de incidência da barra: ')
        print(matrizes_de_incidencia[i])
        print('\nMatriz de rigidez da barra espalhada para todos os graus de liberdade da estrutura: ')
        print(matrizes_espalhadas[i])
    print('\n** Estrutura completa**')
    print('Matriz de rigidez da estrutura completa:')
    print(K)
    print('\nKaa:')
    print(Kaa)
    print('\nKbb:')
    print(Kbb)
    print('\nKab:')
    print(Kab)
    print('\nKba:')
    print(Kba)


# Impressão dos resultados:
def imprime_resultados(Fb, graus_de_liberdade, quantidade_de_barras, esforcos_nas_barras, U):
    print('\nRESULTADOS:')
    print('\nReação de apoio:')
    print(Fb)
    print('\nDeslocamentos:')
    for i in range(graus_de_liberdade):
        print(f'Grau de liberdade {i}: deslocamento = {U[i]}')

    print('\nEsforços nas barras:')
    for i in range(quantidade_de_barras):
        if esforcos_nas_barras[i][0] >= 0:
            print(f'Barra {i}: {esforcos_nas_barras[i]} --> -{abs(esforcos_nas_barras[i][0]):.2f} (Compressão)')
        else:
            print(f'Barra {i}: {esforcos_nas_barras[i]} --> +{abs(esforcos_nas_barras[i][0]):.2f} (Tração)')
