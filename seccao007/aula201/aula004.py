# type: ignore
# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botão1)
#               -> Widget 2 (botão2)
#               -> Widget 3 (botão3)
#   -> show
# -> exec
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow,
                               QWidget, QGridLayout)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha aplicação')

botao1 = QPushButton('Clique aqui')
botao1.setStyleSheet('font-size: 40px; color: red;')

botao2 = QPushButton('Clique aqui')
botao2.setStyleSheet('font-size: 40px; color: green;')

botao3 = QPushButton('Clique aqui')
botao3.setStyleSheet('font-size: 40px; color: orange;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1)
layout.addWidget(botao2, 1, 2)
layout.addWidget(botao3, 3, 1, 1, 2)

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra de status')


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('Mensagem alterada')
    return inner

@Slot()
def outro_slot(checked):
    print('Esta marcado?', checked)


@Slot()
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


# menuBar
menu_bar = window.menuBar()
menu1 = menu_bar.addMenu('Menu 1')
submenu1_2 = menu1.addAction('Submenu 1.1')
menu2 = menu_bar.addMenu('Menu 2')
submenu2 = menu2.addAction('Submenu 2.1')
submenu1_2.triggered.connect(slot_example(status_bar))

submenu1_2 = menu1.addAction('Submenu 1.2')
submenu1_2.setCheckable(True)
submenu1_2.toggled.connect(outro_slot)
submenu1_2.hovered.connect(terceiro_slot(submenu1_2))

botao1.clicked.connect(terceiro_slot(submenu1_2))

window.show()

app.exec()  # loop da aplicação
