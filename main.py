import sys, signal, json
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt

with open("config.json", encoding="utf-8") as arquivo:
    dados_config = json.load(arquivo)
    

class JanelaConfig(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Overlay do Celin")
        
        layout = QVBoxLayout(self)
        self.botao_ativar = QPushButton("Ativar Overlay")
        layout.addWidget(self.botao_ativar)
        
        self.botao_ativar.clicked.connect(self.ativar)
    
    def ativar(self):
        with open("config.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados_config, arquivo, indent=4)
        
        self.overlay = JanelaOverlay()
        self.overlay.show()
        self.hide()

class JanelaOverlay(QWidget):
    def __init__(self):
        super().__init__()
        
        tela = QApplication.primaryScreen().availableGeometry()
        largura = dados_config["size"]["width"]
        altura = dados_config["size"]["height"]
        
        self.setWindowTitle("Overlay do Celin")
        self.label = QLabel("Overlay do Celin")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.label.setStyleSheet("background: rgba(0, 0, 0, 150); color: white; font-size: 24px;")
        self.resize(largura, altura)
        if dados_config["position"] == "bottom-right":
            self.move(tela.width() - largura, tela.height() - altura)
        elif dados_config["position"] == "bottom-left":
            self.move(0, tela.height() - altura)
        elif dados_config["position"] == "top-right":
            self.move(tela.width() - largura, 0)
        elif dados_config["position"] == "top-left":
            self.move(0, 0)

app = QApplication(sys.argv)
config = JanelaConfig()
config.show()
signal.signal(signal.SIGINT, signal.SIG_DFL)
sys.exit(app.exec())
