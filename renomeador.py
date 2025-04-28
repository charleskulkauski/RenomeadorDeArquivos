import sys
import os
from PySide2.QtWidgets import QApplication, QWidget


caminho_pasta = input('Digite o caminho: ')

os.chdir(caminho_pasta)

padrao_nome = input('Digite o padrão de nome sem a extensão: ')


for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        print(exten_arq)
        nome_arq = padrao_nome + ' ' + str(contador)

        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)

print(f'\nArquivos renomeados')