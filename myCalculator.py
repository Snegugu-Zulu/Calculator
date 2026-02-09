import PyQt6.QtCore
import sys
from PyQt6.QtCore import Qt  
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QApplication, QPushButton, QListWidget, QGridLayout, 
                               QDialog, QLabel, QDoubleSpinBox, QLCDNumber)

class MyCalculator(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculator")
        self.last_button_pressed = None  
        self.setup_ui()
    
    def setup_ui(self):
        self.left_list = QListWidget()
        self.left_list2 = QListWidget()
        
        self.doubleSpinBox1 = QDoubleSpinBox()
        self.doubleSpinBox1.setRange(-999999.99, 999999.99) 
        self.doubleSpinBox1.setDecimals(2)  
        self.doubleSpinBox1.setSingleStep(1.0)  
        self.doubleSpinBox1.setMinimumHeight(40)  
        self.doubleSpinBox1.setStyleSheet("font-size: 16px; padding: 5px;")
        self.doubleSpinBox1.setValue(0.0)  
        
        self.doubleSpinBox2 = QDoubleSpinBox()
        self.doubleSpinBox2.setRange(-999999.99, 999999.99)
        self.doubleSpinBox2.setDecimals(2)
        self.doubleSpinBox2.setSingleStep(1.0)
        self.doubleSpinBox2.setMinimumHeight(40)
        self.doubleSpinBox2.setStyleSheet("font-size: 16px; padding: 5px;")
        self.doubleSpinBox2.setValue(0.0)  
        
        self.lcdNumbr = QLCDNumber()
        self.lcdNumbr.setDigitCount(12)  
        self.lcdNumbr.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumbr.setMinimumHeight(60) 
        self.lcdNumbr.setStyleSheet("font-size: 20px; background-color: #f0f0f0; border: 2px solid #ccc;")
        
        self.add_button = QPushButton("+")
        self.add_button.setMinimumSize(80, 50)
        self.add_button.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        self.minus_button = QPushButton("-")
        self.minus_button.setMinimumSize(80, 50)
        self.minus_button.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        self.multiply_button = QPushButton("*")
        self.multiply_button.setMinimumSize(80, 50)
        self.multiply_button.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        self.division_button = QPushButton("/")
        self.division_button.setMinimumSize(80, 50)
        self.division_button.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        self.clear_button = QPushButton("Clear")
        self.clear_button.setMinimumSize(80, 50)
        self.clear_button.setStyleSheet("font-size: 16px;")
        
        self.add_button.clicked.connect(self.add)
        self.minus_button.clicked.connect(self.minus)
        self.multiply_button.clicked.connect(self.multiply)
        self.division_button.clicked.connect(self.divide)
        self.clear_button.clicked.connect(self.clearWidget)

        self.doubleSpinBox1.valueChanged.connect(self.autoCalculate)
        self.doubleSpinBox2.valueChanged.connect(self.autoCalculate)

        layout = QGridLayout(self)
        layout.setSpacing(15)  
        layout.setContentsMargins(20, 20, 20, 20)  

        label1 = QLabel("First Number:")
        label1.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(label1, 0, 0)
        
        label2 = QLabel("Second Number:")
        label2.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(label2, 1, 0)
        
        label3 = QLabel("Result:")
        label3.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(label3, 2, 0)
        
        layout.addWidget(self.doubleSpinBox1, 0, 1)
        layout.addWidget(self.add_button, 0, 2)
        
        layout.addWidget(self.doubleSpinBox2, 1, 1)
        layout.addWidget(self.minus_button, 1, 2)
        
        layout.addWidget(self.lcdNumbr, 2, 1)
        layout.addWidget(self.multiply_button, 2, 2)
        
        layout.addWidget(self.clear_button, 3, 1)
        layout.addWidget(self.division_button, 3, 2)
        
        self.setMinimumSize(500, 400)  
        
    def highlight_button(self, button):
        for btn in [self.add_button, self.minus_button, self.multiply_button, self.division_button, self.clear_button]:
            btn.setStyleSheet(self.get_button_default_style(btn))
        
        if button != self.clear_button:
            button.setStyleSheet("""
                font-size: 20px; 
                font-weight: bold;
                background-color: #4CAF50; 
                color: white;
                border: 2px solid #388E3C;
                border-radius: 5px;
            """)
        
        self.last_button_pressed = button
    
    def get_button_default_style(self, button):
        base_style = """
            font-size: 20px; 
            font-weight: bold;
            background-color: #f0f0f0;
            border: 2px solid #ccc;
            border-radius: 5px;
            padding: 5px;
        """
        if button == self.clear_button:
            return "font-size: 16px; background-color: #f0f0f0; border: 2px solid #ccc; border-radius: 5px; padding: 5px;"
        return base_style
    
    def get_numbers(self):
        item1 = self.doubleSpinBox1.value()
        item2 = self.doubleSpinBox2.value()
        return item1, item2
    
    def clearWidget(self):
        self.doubleSpinBox1.setValue(0.0)        
        self.doubleSpinBox2.setValue(1.0)  
        self.lcdNumbr.display(0)
        self.lcdNumbr.setStyleSheet("font-size: 20px; background-color: #f0f0f0; border: 2px solid #ccc;")

        for btn in [self.add_button, self.minus_button, self.multiply_button, self.division_button, self.clear_button]:
            btn.setStyleSheet(self.get_button_default_style(btn))
        self.last_button_pressed = None
        
    def autoCalculate(self):
        if self.last_button_pressed:
            if self.last_button_pressed == self.add_button:
                self.add()
            elif self.last_button_pressed == self.minus_button:
                self.minus()
            elif self.last_button_pressed == self.multiply_button:
                self.multiply()
            elif self.last_button_pressed == self.division_button:
                self.divide()
        
    def add(self):
        self.highlight_button(self.add_button)
        num1, num2 = self.get_numbers()
        result = num1 + num2
        self.lcdNumbr.display(result)  
        
    def minus(self):
        self.highlight_button(self.minus_button)
        num1, num2 = self.get_numbers()
        result = num1 - num2
        self.lcdNumbr.display(result)  
    
    def multiply(self):
        self.highlight_button(self.multiply_button)
        num1, num2 = self.get_numbers()
        result = num1 * num2
        self.lcdNumbr.display(result) 
    
    def divide(self):
        self.highlight_button(self.division_button)
        num1, num2 = self.get_numbers()
        if num2 != 0:
            result = num1 / num2
            self.lcdNumbr.display(result)  
            self.lcdNumbr.setStyleSheet("font-size: 20px; background-color: #f0f0f0; border: 2px solid #ccc;")
        else:
            self.lcdNumbr.display(0)  
            self.lcdNumbr.setStyleSheet("font-size: 20px; background-color: #ffcccc; border: 2px solid #ff0000;")


app = QApplication(sys.argv)
app.setStyle('Fusion')  

calculator = MyCalculator()
calculator.show()
sys.exit(app.exec())