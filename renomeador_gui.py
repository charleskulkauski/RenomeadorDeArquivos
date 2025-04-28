# renomeador_gui_bonito.py

import os
import sys
import time
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QFileDialog, QMessageBox, QHBoxLayout
)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, QTimer, QSize

class RenomeadorArquivos(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
     
        self.setWindowTitle("Renomeador de Arquivos")
        self.setFixedSize(450, 350)
        self.setStyleSheet("background-color: #f9f9f9;") 

        fonte_padrao = QFont("Arial", 12)

     
        self.label_pasta = QLabel("Nenhuma pasta selecionada", self)
        self.label_pasta.setFont(fonte_padrao)
        self.label_pasta.setAlignment(Qt.AlignCenter)

        self.botao_pasta = QPushButton("Escolher Pasta", self)
        self.botao_pasta.setFont(fonte_padrao)
        self.botao_pasta.setStyleSheet("""
            QPushButton {
                background-color: #007aff;
                color: white;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
        """)
     
        self.botao_pasta.clicked.connect(self.selecionar_pasta)

        linha_pasta = QHBoxLayout()
        linha_pasta.addWidget(self.botao_pasta)
        linha_pasta.addWidget(self.label_pasta)

     
        self.label_padrao = QLabel("Digite o padrão de nome:", self)
        self.label_padrao.setFont(fonte_padrao)

        self.input_padrao = QLineEdit(self)
        self.input_padrao.setFont(fonte_padrao)
        self.input_padrao.setPlaceholderText("Ex: Documento")
        self.input_padrao.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
            }
            QLineEdit:focus {
                border-color: #007aff;
            }
        """)


        self.botao_renomear = QPushButton("Renomear Arquivos", self)
        self.botao_renomear.setFont(fonte_padrao)
        self.botao_renomear.setFixedSize(QSize(200, 40))
        self.botao_renomear.setStyleSheet("""
            QPushButton {
                background-color: #34c759;
                color: white;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #28a745;
            }
        """)
        self.botao_renomear.clicked.connect(self.animar_renomear)


        self.label_status = QLabel("", self)
        self.label_status.setFont(fonte_padrao)
        self.label_status.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        
        layout.setSpacing(20) 
        layout.setContentsMargins(20, 20, 20, 10)  

        layout.addLayout(linha_pasta)
        layout.addWidget(self.label_padrao)
        layout.addWidget(self.input_padrao)
        layout.addWidget(self.botao_renomear, alignment=Qt.AlignCenter)
        layout.addWidget(self.label_status)

        self.setLayout(layout)

        self.caminho_pasta = ""

    def selecionar_pasta(self):
        pasta = QFileDialog.getExistingDirectory(self, "Selecione uma pasta")
        if pasta:
            self.caminho_pasta = pasta
            nome_pasta = os.path.basename(pasta)
            self.label_pasta.setText(f"📁 {nome_pasta}")

    def animar_renomear(self):
        if not self.caminho_pasta or not self.input_padrao.text():
            QMessageBox.warning(self, "Erro", "Selecione uma pasta e insira um padrão de nome.")
            return

        self.label_status.setText("⏳ Renomeando arquivos...")
        QTimer.singleShot(500, self.renomear_arquivos) 

    def renomear_arquivos(self):
        padrao_nome = self.input_padrao.text()

        try:
            os.chdir(self.caminho_pasta)
            for contador, arq in enumerate(os.listdir()):
                if os.path.isfile(arq):
                    nome_arq, exten_arq = os.path.splitext(arq)
                    nome_novo = f"{padrao_nome} {contador}{exten_arq}"
                    os.rename(arq, nome_novo)

            self.label_status.setText("✅ Arquivos renomeados com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao renomear: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = RenomeadorArquivos()
    janela.show()
    sys.exit(app.exec())
