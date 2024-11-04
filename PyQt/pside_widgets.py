import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QCheckBox, QRadioButton, QTextEdit, QSlider, QSpinBox, QProgressBar, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QWidget

class DemoWindow(QMainWindow):
   def __init__(self):
       super().__init__()

       # Main Widget and Layout
       main_widget = QWidget()
       self.setCentralWidget(main_widget)
       main_layout = QVBoxLayout(main_widget)

       # Function to add widget with label
       def add_widget_with_label(layout, widget, label_text):
           hbox = QHBoxLayout()
           label = QLabel(label_text)
           hbox.addWidget(label)
           hbox.addWidget(widget)
           layout.addLayout(hbox)

       # QLabel
       self.label = QLabel('Hello PySide6!')
       add_widget_with_label(main_layout, self.label, 'QLabel:')

       # QPushButton
       self.button = QPushButton('Click Me')
       self.button.clicked.connect(self.on_button_clicked)
       add_widget_with_label(main_layout, self.button, 'QPushButton:')

       # QLineEdit
       self.line_edit = QLineEdit()
       add_widget_with_label(main_layout, self.line_edit, 'QLineEdit:')

       # QComboBox
       self.combo_box = QComboBox()
       self.combo_box.addItems(['Option 1', 'Option 2', 'Option 3'])
       add_widget_with_label(main_layout, self.combo_box, 'QComboBox:')

       # QCheckBox
       self.check_box = QCheckBox('Check Me')
       add_widget_with_label(main_layout, self.check_box, 'QCheckBox:')

       # QRadioButton
       self.radio_button = QRadioButton('Radio Button')
       add_widget_with_label(main_layout, self.radio_button, 'QRadioButton:')

       # QTextEdit
       self.text_edit = QTextEdit()
       add_widget_with_label(main_layout, self.text_edit, 'QTextEdit:')

       # QSlider
       self.slider = QSlider()
       add_widget_with_label(main_layout, self.slider, 'QSlider:')

       # QSpinBox
       self.spin_box = QSpinBox()
       add_widget_with_label(main_layout, self.spin_box, 'QSpinBox:')

       # QProgressBar
       self.progress_bar = QProgressBar()
       add_widget_with_label(main_layout, self.progress_bar, 'QProgressBar:')

       # QTableWidget
       self.table_widget = QTableWidget(5, 3) 
       for i in range(5):
           for j in range(3):
               item = QTableWidgetItem(f"Cell {i+1},{j+1}")
               self.table_widget.setItem(i, j, item)
       add_widget_with_label(main_layout, self.table_widget, 'QTableWidget:')

   def on_button_clicked(self):
       self.label.setText('Button Clicked!')

# Run the application
app = QApplication(sys.argv)
window = DemoWindow()
window.show()
sys.exit(app.exec_())
