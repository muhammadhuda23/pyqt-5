from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])

window = QMainWindow()

label = QLabel(window)
label.setText("Label Anjay")
label.move(200,0)

button = QPushButton(window)
button.setText("First Button")

window.show()
app.exec_()