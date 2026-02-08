import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize

class HelloWindow(QMainWindow):
    def __init__(self):
        super().__init__() # Forma correta de inicializar

        self.setMinimumSize(QSize(280, 120))
        self.setWindowTitle("Olá, Mundo! Exemplo PyQt5")

        # Criando o widget central
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # CORREÇÃO: O layout deve ser aplicado ao centralWidget, 
        # e não passar 'self' (o QMainWindow) como pai do QGridLayout.
        gridLayout = QGridLayout(centralWidget) 
        
        title = QLabel("Olá Mundo para PyQt", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        
        # Adicionando ao layout
        gridLayout.addWidget(title, 0, 0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec_())