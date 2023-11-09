from interface import *
from resumo import *
from calculos import *
import tkinter as tk


if __name__ == '__main__':

    dimensao = 2  # Dimensão do modelo, no caso: 2D

    # Dados de entrada:

    # Ler do arquivo
    ponto = np.loadtxt('pontos.csv', delimiter=',')
    vinculos = np.loadtxt('vinculos.csv', delimiter=',')
    carregamentos = np.loadtxt('carregamentos.csv', delimiter=',')
    barras = np.loadtxt('barras.csv', delimiter=',')

    # Criar as barras conforme arquivo de entrada
    barra = []
    for i in range(len(barras)):
        E, area = barras[i][0], barras[i][1]
        ponto_inicial, ponto_final = ponto[int(barras[i][2])], ponto[int(barras[i][3])]
        barra.append(cria_barra(E, area, ponto_inicial, ponto_final))


    # Fim dos dados de entrada

    quantidade_de_barras = len(barra)
    graus_de_liberdade = len(ponto) * 2

    matrizes_de_rigidez_locais = []
    matrizes_de_rigidez_globais = []
    matrizes_de_incidencia = []
    matrizes_de_transformacao = []
    matrizes_espalhadas = []
    esforcos_nas_barras = []
    K = [[0 for i in range(0, graus_de_liberdade)] for j in
         range(0, graus_de_liberdade)]  # Matriz de rigidez da estrutura

    # Cálculo da matriz de rigidez da estrutura:
    for i in range(quantidade_de_barras):
        # Para cada barra, extrair os parâmetros: E (módulo de elasticidade), A (área da seção transversal),
        # L (comprimento), theta (ângulo em relação à horizontal), gdl (graus de liberdade dos pontos inicial e final)

        E, A, L, theta, gdl1, gdl2, gdl3, gdl4 = barra[i][0], barra[i][1], barra[i][2], barra[i][3], barra[i][4], \
        barra[i][
            5], barra[i][6], barra[i][7]
        gdl = [gdl1, gdl2, gdl3, gdl4]

        # Para cada barra, calcular a matriz de rigidez no sistema local:
        k_local = matriz_de_rigidez_local(E, A, L)

        # Para cada barra, calcular a matriz de rigidez no sistema global:
        matriz_de_transf = matriz_de_transformacao(theta)
        k_global = matriz_de_rigidez_global_barra(k_local, matriz_de_transf)

        # Para cada barra, espalhar sua matriz de rigidez nos devidos graus de liberdade da estrutura completa:
        incid = matriz_de_incidencia(gdl, graus_de_liberdade, dimensao)
        kc_barra = np.matmul(np.transpose(incid), np.matmul(k_global, incid))  # Matriz de rigidez espalhada da barra

        # Armazenar as matrizes calculadas para cada barra numa lista para uso futuro:
        matrizes_de_rigidez_locais.append(k_local)
        matrizes_de_rigidez_globais.append(k_global)
        matrizes_de_transformacao.append(matriz_de_transf)
        matrizes_de_incidencia.append(incid)
        matrizes_espalhadas.append(kc_barra)

        # Somar a matriz de rigidez da barra com a matriz de rigidez da estrutura completa:
        K += kc_barra  # Matriz de rigidez da estrutura completa

    # Extração das matrizes de rigidez para os graus de liberdade livres (a) e bloqueados (b)
    Kaa = np.array(
        [[K[i][j] for i in range(0, graus_de_liberdade) if i not in vinculos] for j in range(0, graus_de_liberdade) if
         j not in vinculos])  # Matriz de rigidez reduzida da estrutura

    Kbb = np.array(
        [[K[i][j] for i in range(0, graus_de_liberdade) if i in vinculos] for j in range(0, graus_de_liberdade) if
         j in vinculos])

    Kba = np.array(
        [[K[i][j] for i in range(0, graus_de_liberdade) if i not in vinculos] for j in range(0, graus_de_liberdade) if
         j in vinculos])

    Kab = np.array(
        [[K[i][j] for i in range(0, graus_de_liberdade) if i in vinculos] for j in range(0, graus_de_liberdade) if
         j in vinculos])

    # Montagem do vetor de carregamentos Fa (livre)
    Fa = np.array([carregamentos[i] for i in range(graus_de_liberdade) if i not in vinculos])  # Carregamentos reduzidos

    # Cálculo dos deslocamentos dos nós livres:
    Ua = np.matmul(np.linalg.inv(Kaa), Fa)

    # Cálculo das forças nos nós bloqueados, ou seja, as reações de apoio
    Fb = np.matmul(Kba, Ua)

    # Montagem do vetor de deslocamentos completo:
    U = []
    j = 0
    for i in range(graus_de_liberdade):
        if i in vinculos:
            U.append(0)
        else:
            U.append(Ua[j])
            j += 1

    # Cálculo dos esforços nas barras
    for i in range(quantidade_de_barras):
        k_barra = matrizes_de_rigidez_locais[i]
        incidencia = matrizes_de_incidencia[i]
        transformacao = matrizes_de_transformacao[i]

        esforcos = np.matmul(k_barra, np.matmul(transformacao, np.matmul(incidencia, U)))
        esforcos_nas_barras.append(esforcos)

    # Impressão dos cálculos:
    imprime_entrada(ponto, vinculos, barra, quantidade_de_barras)
    imprime_calculos(quantidade_de_barras, matrizes_de_rigidez_locais, matrizes_de_transformacao,
                     matrizes_de_rigidez_globais, matrizes_de_incidencia, matrizes_espalhadas, K, Kaa, Kbb, Kab, Kba)
    imprime_resultados(Fb, graus_de_liberdade, quantidade_de_barras, esforcos_nas_barras, U)

    janela = tk.Tk()
    janela.title("trussCalc")

    deformada = lambda: grafico_deslocamentos(ponto, barra, quantidade_de_barras, U)
    geometria = lambda: grafico_geometria(ponto, barra, quantidade_de_barras)
    esforcos = lambda: grafico_esforcos(ponto, barra, quantidade_de_barras, esforcos_nas_barras)

    botao_geometria = tk.Button(janela, text="Geometria", width=15, command=geometria)
    botao_deformada = tk.Button(janela, text="Deformada", width=15, command=deformada)
    botao_esforcos = tk.Button(janela, text="Esforços", width=15, command=esforcos)
    credito = tk.Label(janela, text="\n\nEng. Guilherme Vick")

    botao_geometria.pack()
    botao_deformada.pack()
    botao_esforcos.pack()
    credito.pack()


    janela.mainloop()


    grafico_geometria(ponto, barra, quantidade_de_barras)
    grafico_deslocamentos(ponto, barra, quantidade_de_barras, U)


