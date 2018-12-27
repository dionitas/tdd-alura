from src.leilao.dominio import Usuario, Lance, Leilao

gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_gui)

for lance in leilao.lances:
    print('O usuario {} deu um lance de {}'.format(lance.usuario.nome,lance.valor))

# print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')
4