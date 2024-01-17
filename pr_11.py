import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QCheckBox, QTextEdit, QFileDialog, QLineEdit, QMessageBox, QComboBox

class MyApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ФИО Автора")

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.setup_tab1()
        self.setup_tab2()
        self.setup_tab3()

        self.tabs.addTab(self.tab1, "Калькулятор")
        self.tabs.addTab(self.tab2, "Чекбоксы")
        self.tabs.addTab(self.tab3, "Работа с текстом")

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def setup_tab1(self):
        layout = QVBoxLayout()

        num1_input = QLineEdit()
        num2_input = QLineEdit()
        operation_combobox = QComboBox()
        operation_combobox.addItems(["+", "-", "*", "/"])

        result_label = QLabel("Результат:")

        calculate_button = QPushButton("Вычислить")
        calculate_button.clicked.connect(lambda: self.calculate(num1_input, num2_input, operation_combobox, result_label))

        layout.addWidget(num1_input)
        layout.addWidget(operation_combobox)
        layout.addWidget(num2_input)
        layout.addWidget(calculate_button)
        layout.addWidget(result_label)

        self.tab1.setLayout(layout)

    def calculate(self, num1_input, num2_input, operation_combobox, result_label):
        try:
            num1 = float(num1_input.text())
            num2 = float(num2_input.text())
            operation = operation_combobox.currentText()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2

            result_label.setText(f"Результат: {result}")
        except ValueError:
            result_label.setText("Ошибка ввода чисел")

    def setup_tab2(self):
        layout = QVBoxLayout()

        checkbox1 = QCheckBox("Первый вариант")
        checkbox2 = QCheckBox("Второй вариант")
        checkbox3 = QCheckBox("Третий вариант")

        show_message_button = QPushButton("Показать сообщение")
        show_message_button.clicked.connect(lambda: self.show_message(checkbox1, checkbox2, checkbox3))

        layout.addWidget(checkbox1)
        layout.addWidget(checkbox2)
        layout.addWidget(checkbox3)
        layout.addWidget(show_message_button)

        self.tab2.setLayout(layout)

    def show_message(self, checkbox1, checkbox2, checkbox3):
        message = "Вы выбрали: "
        if checkbox1.isChecked():
            message += "первый вариант, "
        if checkbox2.isChecked():
            message += "второй вариант, "
        if checkbox3.isChecked():
            message += "третий вариант, "

        message = message.rstrip(", ")
        QMessageBox.information(self, "Выбор", message)

    def setup_tab3(self):
        layout = QVBoxLayout()

        load_button = QPushButton("Загрузить текст из файла")
        load_button.clicked.connect(self.load_text_from_file)

        text_edit = QTextEdit()

        layout.addWidget(load_button)
        layout.addWidget(text_edit)

        self.tab3.setLayout(layout)

    def load_text_from_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt);;Все файлы (*)", options=options)

        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                self.tabs.widget(2).findChild(QTextEdit).setPlainText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec_())
