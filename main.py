import sys
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

        # Zona donde aparecerán las notas creadas
        self.notas_widget = QWidget(self)
        self.notas_widget.setGeometry(300,60,400,250)
        self.notas_layout = QVBoxLayout(self.notas_widget)
        self.notas_widget.setLayout(self.notas_layout)


        # Caja para mostrar la lista de notas -------------------
        groupBox = QGroupBox(self)
        groupBox.setGeometry(10,65, 250, 265)
        groupBox.setStyleSheet("background-color: white;")

        groupBox_layout = QVBoxLayout()
        label = QLabel("Contenido de la caja")
        groupBox_layout.addWidget(label)
        label1 = QLabel("Contenido de la caja")
        groupBox_layout.addWidget(label1)
        label2 = QLabel("Contenido de la caja")
        groupBox_layout.addWidget(label2)
        groupBox.setLayout(groupBox_layout)

   
    def crear_nota(self):
        # Layout horizontal para la nota + botón
        nota_layout = QHBoxLayout()

        # Caja de texto
        nota = QLineEdit()
        nota.setPlaceholderText("Escribe tu nota aquí...")
        nota.setFixedHeight(80)
        nota.setStyleSheet("background-color: #f0f0f0; font-size: 20px; color: black; margin: 5px;")

        # Botón Save
        save_btn = QPushButton("✔")
        save_btn.setStyleSheet("background-color: green; color: white; font-size: 23px; padding: 10px;")

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
        
    
    def del_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        
        self.notas_layout.removeItem(layout)


def main():
    app = QApplication(sys.argv)    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
