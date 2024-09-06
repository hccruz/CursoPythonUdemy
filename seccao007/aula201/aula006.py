''' type: ignore
# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (grid_layout)
#               -> Widget 1 (botão1)
#               -> Widget 2 (botão2)
#               -> Widget 3 (botão3)
#   -> show
# -> exec '''
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow,
                               QWidget, QGridLayout)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha aplicação')

        self.botao1 = QPushButton('Clique aqui')
        self.botao1.setStyleSheet('font-size: 40px; color: red;')
        self.botao1.clicked.connect(self.outro_slot)

        self.botao2 = QPushButton('Clique aqui')
        self.botao2.setStyleSheet('font-size: 40px; color: green;')

        self.botao3 = QPushButton('Clique aqui')
        self.botao3.setStyleSheet('font-size: 40px; color: orange;')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra de status')

        # menuBar
        self.menu_bar = self.menuBar()
        self.menu1 = self.menu_bar.addMenu('Menu 1')
        self.submenu1_2 = self.menu1.addAction('Submenu 1.1')
        self.menu2 = self.menu_bar.addMenu('Menu 2')
        self.submenu2 = self.menu2.addAction('Submenu 2.1')
        self.submenu1_2.triggered.connect(self.slot_example)

        self.submenu1_2 = self.menu1.addAction('Submenu 1.2')
        self.submenu1_2.setCheckable(True)
        self.submenu1_2.toggled.connect(self.outro_slot)
        self.submenu1_2.hovered.connect(self.outro_slot)

    @Slot()
    def slot_example(self):
        self.status_bar.showMessage('Mensagem alterada')

    @Slot()
    def outro_slot(self):
        print('Esta marcado?', self.submenu1_2.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    app.exec()  # loop da aplicação
