import graphics as gr


def grafico_geometria(pontos, barra, quantidade_de_barras):
    escala = 100
    escala_deformacao = 10.0

    # Desenhando a treliça:
    geometria = gr.GraphWin(width=1000, height=500, title='Geometria')

    origem_x = escala / 2
    origem_y = geometria.height - origem_x

    # Desenhando o número dos nós:
    for i in range(len(pontos)):
        numero_do_no = gr.Text(
            gr.Point(pontos[i][1] * escala + origem_x + escala / 10, origem_y - pontos[i][2] * escala - escala / 10),
            pontos[i][0])
        numero_do_no.draw(geometria)

    for i in range(quantidade_de_barras):

        x_inicial = barra[i][8][1]
        y_inicial = barra[i][8][2]
        x_final = barra[i][9][1]
        y_final = barra[i][9][2]

        ponto_inicial = gr.Point(origem_x + x_inicial * escala, origem_y - y_inicial * escala)
        ponto_final = gr.Point(origem_x + x_final * escala, origem_y - y_final * escala)

        # Desenhando o número das barras:
        numero_da_barra = gr.Text(gr.Point(origem_x + (x_inicial + x_final) / 2 * escala,
                                           origem_y - (y_inicial + y_final) / 2 * escala), i)
        numero_da_barra.setTextColor("blue")
        numero_da_barra.draw(geometria)


        linha = gr.Line(ponto_inicial, ponto_final)
        linha.draw(geometria)
    return geometria


def grafico_deslocamentos(pontos, barra, quantidade_de_barras, U):

    escala = 100
    escala_deformacao = 10.0

    # Desenhando os deslocamentos:
    deslocamentos = gr.GraphWin(width=1000, height=500, title='Deslocamentos')

    origem_x = escala / 2
    origem_y = deslocamentos.height / 2 - origem_x

    # Montagem do vetor de pontos na posição deformada:
    ponto_deslocado = []
    for i in range(len(pontos)):
        lista = [pontos[i][1] + U[i * 2] * escala_deformacao, pontos[i][2] + U[i * 2 + 1] * escala_deformacao]
        ponto_deslocado.append(lista)




    for i in range(quantidade_de_barras):
        # Desenhando a estrutura indeformada:
        ponto_inicial = gr.Point(origem_x + barra[i][8][1] * escala,
                                 origem_y - barra[i][8][2] * escala)
        ponto_final = gr.Point(origem_x + barra[i][9][1] * escala,
                               origem_y - barra[i][9][2] * escala)

        linha = gr.Line(ponto_inicial, ponto_final)
        linha.draw(deslocamentos)

        # Desenhando a estrutura deformada:

        ponto_inicial = gr.Point(origem_x + ponto_deslocado[int(barra[i][8][0])][0] * escala,
                                 origem_y - ponto_deslocado[int(barra[i][8][0])][1] * escala)
        ponto_final = gr.Point(origem_x + ponto_deslocado[int(barra[i][9][0])][0] * escala,
                               origem_y - ponto_deslocado[int(barra[i][9][0])][1] * escala)

        linha = gr.Line(ponto_inicial, ponto_final)
        linha.draw(deslocamentos)

    deslocamentos.mainloop()
    return deslocamentos


def grafico_esforcos(pontos, barra, quantidade_de_barras, esforco_da_barra):
    escala = 100
    escala_deformacao = 10.0

    # Desenhando a treliça:
    geometria = gr.GraphWin(width=1000, height=500, title='Esforços')

    origem_x = escala / 2
    origem_y = geometria.height - origem_x

    for i in range(quantidade_de_barras):
        x_inicial = barra[i][8][1]
        y_inicial = barra[i][8][2]
        x_final = barra[i][9][1]
        y_final = barra[i][9][2]

        ponto_inicial = gr.Point(origem_x + x_inicial * escala, origem_y - y_inicial * escala)
        ponto_final = gr.Point(origem_x + x_final * escala, origem_y - y_final * escala)

        # Desenhando o esforço das barras:
        esforco = gr.Text(gr.Point(origem_x + (x_inicial + x_final) / 2 * escala,
                                           origem_y - (y_inicial + y_final) / 2 * escala), round(esforco_da_barra[i][2],2))
        if esforco_da_barra[i][2] >= 0:
            esforco.setTextColor("blue")
        else:
            esforco.setTextColor("red")
        esforco.draw(geometria)

        linha = gr.Line(ponto_inicial, ponto_final)
        linha.draw(geometria)

    return esforco
