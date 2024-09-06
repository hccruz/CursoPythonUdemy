# type ignore
# QApplication e QPushButton de Pyside6.QtWidgtes
# QApplication -> O Widget principal da aplicação
# QPushButton -> Cria um botão
# PySide.QtWidgets -> Onde estão os widgets do PySide6
import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Clique aqui')
botao.setStyleSheet('font-size: 40px; color: red;')
botao.show()  # Adicionar o widget na hieraquia e exibe a janela

botao2 = QPushButton('Clique aqui')
botao2.setStyleSheet('font-size: 40px; color: green;')
botao2.show()  # Adicionar o widget na hieraquia e exibe a janela

app.exec()  # loop da aplicação
