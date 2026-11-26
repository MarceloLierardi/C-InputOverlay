import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton

class JanelaConfig(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Overlay do Celin")
        
        layout = QVBoxLayout(self)
        self.botao_ativar = QPushButton("Ativar Overlay")
        layout.addWidget(self.botao_ativar)
        
        self.botao_ativar.clicked.connect(self.ativar)
        
    def ativar(self):
            self.overlay = JanelaOverlay()
            self.overlay.show()
            self.hide()

class JanelaOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Overlay do Celin")
        self.label = QLabel("Overlay do Celin")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        
    


app = QApplication(sys.argv)
config = JanelaConfig()
config.show()
sys.exit(app.exec())
