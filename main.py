import sys
import json
import os
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QLabel, QLineEdit, 
    QPushButton, QVBoxLayout, QWidget, QGroupBox, QHBoxLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUp()
        
    def setUp(self):
        self.setWindowTitle("Notes Taking")
        self.setGeometry(300,200,800,350)
        self.setStyleSheet("background-color: gray;")

        self.notas_file = "notas.json"
        self.notas_data = self.cargar_notas()

        # Zona Busqueda ----------------------------
        buscar = QLineEdit(self)
        buscar.setGeometry(10,10,150,40)
        buscar.setStyleSheet("background-color: white;"
                             "font-size: 20px;"
                             "color: black;")
        buscar.setPlaceholderText("Buscar...")

        buscar_boton = QPushButton("Buscar", self)
        buscar_boton.setGeometry(165,10,95,40)
        buscar_boton.setStyleSheet("background-color: white;"
                                   "font-size: 15px;"
                                   "color: black;")

        # Boton para Crear Nota ----------------------
        crear_boton = QPushButton("Crear Nota", self)
        crear_boton.setGeometry(300,10,100,40)
        crear_boton.setStyleSheet("background-color: white;"
                                  "font-size: 15px;"
                                  "color: black;")
        crear_boton.clicked.connect(self.crear_nota)

        # Boton para Borrar Notas

        # Zona donde aparecerán las notas creadas
        self.notas_widget = QWidget(self)
        self.notas_widget.setGeometry(300,60,400,250)
        self.notas_layout = QVBoxLayout(self.notas_widget)
        self.notas_widget.setLayout(self.notas_layout)

        # Caja para mostrar la lista de notas -------------------
        self.groupBox = QGroupBox("Notas guardadas", self)
        self.groupBox.setGeometry(10,65, 250, 265)
        self.groupBox.setStyleSheet("background-color: white;")
        self.groupBox_layout = QVBoxLayout()
        self.groupBox.setLayout(self.groupBox_layout)

        # Cargar notas guardadas
        for nota in self.notas_data:
            self.mostrar_nota_guardada(nota)


    def crear_nota(self):
        # Layout horizontal para la nota + botones
        nota_layout = QHBoxLayout()

        # Caja de texto
        nota = QLineEdit()
        nota.setPlaceholderText("Escribe tu nota aquí...")
        nota.setFixedHeight(80)
        nota.setStyleSheet("background-color: #f0f0f0; font-size: 20px; color: black; margin: 5px;")

        # Botón Save
        save_btn = QPushButton("✔")
        save_btn.setStyleSheet("background-color: green; color: white; font-size: 23px; padding: 10px;")
        save_btn.clicked.connect(lambda: self.guardar_nota(nota.text()))

        # Boton Delete
        del_btn = QPushButton("✖")
        del_btn.setStyleSheet("background-color: red; color: white; font-size: 23px; padding: 10px;")
        del_btn.clicked.connect(lambda: self.del_layout(nota_layout))

        # Agregar widgets al layout horizontal
        nota_layout.addWidget(nota)
        nota_layout.addWidget(save_btn)
        nota_layout.addWidget(del_btn)

        # Agregar el layout horizontal al layout de notas
        self.notas_layout.addLayout(nota_layout)
        

    def guardar_nota(self, texto):
        if not texto.strip():
            return
        self.notas_data.append(texto)
        with open(self.notas_file, "w", encoding="utf-8") as f:
            json.dump(self.notas_data, f, indent=4, ensure_ascii=False)
        self.mostrar_nota_guardada(texto)


    def mostrar_nota_guardada(self, texto):
        nota_guardada_layout = QHBoxLayout()

        # Texto de la nota
        label = QLabel(texto)
        label.setStyleSheet("font-size: 16px; color: black; margin: 5px;")

        # Botón eliminar
        del_btn = QPushButton("✖")
        del_btn.setStyleSheet("background-color: red; color: white; font-size: 16px; padding: 5px;")
        del_btn.clicked.connect(lambda: self.eliminar_nota(texto, nota_guardada_layout))

        # Agregar widgets al layout horizontal
        nota_guardada_layout.addWidget(label)
        nota_guardada_layout.addWidget(del_btn)

        # Agregar al layout principal de notas guardadas
        self.groupBox_layout.addLayout(nota_guardada_layout)

    def del_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        
        self.notas_layout.removeItem(layout)


    def cargar_notas(self):
        if os.path.exists(self.notas_file):
            with open(self.notas_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return []
    
    def eliminar_nota(self, texto, layout):
        # Borrar de la lista en memoria
        if texto in self.notas_data:
            self.notas_data.remove(texto)
            with open(self.notas_file, "w", encoding="utf-8") as f:
                json.dump(self.notas_data, f, indent=4, ensure_ascii=False)

        # Eliminar de la interfaz
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.groupBox_layout.removeItem(layout)


def main():
    app = QApplication(sys.argv)    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
