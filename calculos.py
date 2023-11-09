from math import sqrt, sin, cos, acos
import numpy as np

def calcula_comprimento(ponto1, ponto2):
    """
    Dado o ponto inicial e final da barra, calcula seu comprimento
    """
    x1, y1 = ponto1[1], ponto1[2]
    x2, y2 = ponto2[1], ponto2[2]

    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def calcula_angulo(ponto1, ponto2):
    """
    Dado o ponto inicial e final da barra, calcula o ângulo (em radianos) entre ela e a horizontal
    """
    x1, y1 = ponto1[1], ponto1[2]
    x2, y2 = ponto2[1], ponto2[2]
    L = calcula_comprimento(ponto1, ponto2)
    x1_versor = 1
    y1_versor = 0
    delta_x = x2 - x1
    delta_y = y2 - y1
    cos_theta = (delta_x * x1_versor + delta_y * y1_versor) / L

    theta = acos(cos_theta)
    if y2 - y1 < 0:
        theta = 2 * np.pi - theta

    return theta


def cria_barra(E, A, ponto1, ponto2):
    """
    Dados os valores de módulo de elasticidade, área, ponto inicial e final, retorna uma lista com os parâmetros
    necessários para manipulação das barras nos cálculos: E, A, theta, gdl1, gdl2, gdl3, gdl3, ponto1, ponto2
    onde: E = módulo de elasticidade, A = área da seção transvesal, theta = ângulo entre a barra e a horizontal,
    gdl1, gdl2, gdl3, gdl4 = graus de liberdade referentes aos nós da barra, ponto1 = nó inicial da barra,
    ponto2 = nó final da barra
    :param E:
    :param A:
    :param ponto1:
    :param ponto2:
    :return:
    """
    gdl1 = ponto1[0] * 2
    gdl2 = ponto1[0] * 2 + 1
    gdl3 = ponto2[0] * 2
    gdl4 = ponto2[0] * 2 + 1

    L = calcula_comprimento(ponto1, ponto2)
    theta = calcula_angulo(ponto1, ponto2)

    return [E, A, L, theta, gdl1, gdl2, gdl3, gdl4, ponto1, ponto2]


def matriz_de_rigidez_local(E, A, L):
    k = np.array([[E * A / L, 0, -E * A / L, 0], [0, 0, 0, 0], [-E * A / L, 0, E * A / L, 0], [0, 0, 0, 0]])
    return k


def matriz_de_transformacao(theta):
    c = cos(theta)
    s = sin(theta)
    return np.array([[c, s, 0, 0], [-s, c, 0, 0], [0, 0, c, s], [0, 0, -s, c]])


def matriz_de_rigidez_global_barra(matriz_de_rigidez_local, matriz_de_transformacao):
    transf = matriz_de_transformacao
    transf_tranposta = np.transpose(transf)
    return np.matmul(transf_tranposta, np.matmul(matriz_de_rigidez_local, transf))


def matriz_de_incidencia(gdl, graus_de_liberdade, dimensao):
    # Uma maneira possível:
    # incid = []
    # for j in range(0, 4):
    #   incidencia = [1 if gdl[j]==i else 0 for i in range(graus_de_liberdade)]
    #   incid.append(incidencia)
    # return np.array(incid)

    # Uma maneira mais elegante:
    # incidencia = [[1 if gdl[j]==i else 0 for i in range(graus_de_liberdade)] for j in range(0,4)]
    # print (incidencia)

    # Uma maneira chiquérrima:
    incidencia = [list(map(lambda i: int(gdl[j] == i), range(graus_de_liberdade))) for j in range(0, dimensao * 2)]

    return np.array(incidencia)