import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QVBoxLayout

# Create the application object
app = QApplication(sys.argv)

# Create a simple window
window = QWidget()
window.setWindowTitle('Simple PyQt5 Example')
window.setGeometry(100, 100, 300, 200)

#
layout = QVBoxLayout()
#-------------------------------------------------------------------------
grid = QGridLayout()

nameLabel = QLabel('Name: ')
grid.addWidget(nameLabel, 0, 0)

button = QPushButton('OK')
grid.addWidget(button, 1, 0)
button.clicked.connect(lambda: print('Button clicked!'))

# Set up the layout
layout.addLayout(grid)

window.setLayout(layout)

# Show the window
window.show()

# Run the application event loop
sys.exit(app.exec_())
