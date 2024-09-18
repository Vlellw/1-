import sys
import json
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QComboBox, QTextEdit, QVBoxLayout, QRadioButton, QCheckBox, QLineEdit
)
from PyQt5.QtCore import QRect, QTimer, QTime, Qt


class WelcomeWindow(QWidget):
    def __init__(self, app):
        super().__init__()

        self.app = app  # Ссылка на приложение

        self.setWindowTitle("Welcome")
        self.setGeometry(600, 300, 600, 420)
        self.setStyleSheet("background-color: #2E8B57;")

        self.label = QLabel("Добро пожаловать в \n     Генератор Рецептов!", self)
        self.label.setGeometry(QRect(60, 0, 550, 160))
        self.label.setStyleSheet("font-size: 45px;"
                                 "font-family: 'Times New Roman';"
                                 "color: black;")

        self.label_name = QLabel("Введите свое имя:", self)
        self.label_name.setGeometry(QRect(150, 180, 300, 50))
        self.label_name.setStyleSheet("font-size: 35px;"
                                      "font-family: 'Times New Roman';"
                                      "color: black;")

        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(QRect(150, 240, 300, 40))
        self.name_input.setStyleSheet("font-size: 35px;"
                                      "font-family: 'Times New Roman';"
                                      "color: white;"
                                      "background-color: black;")

        self.start_button = QPushButton("Старт", self)
        self.start_button.setGeometry(QRect(225, 305, 150, 50))
        self.start_button.setStyleSheet("background-color: black; color: white; font-size: 20px;")
        self.start_button.clicked.connect(self.open_main_window)

    def open_main_window(self):
        user_name = self.name_input.text() 
        if user_name.strip() == "":  
            user_name = "Guest"  

        self.main_window = RecipeGenerator(self.app, user_name) 
        self.main_window.show()
        self.close() 


class RecipeGenerator(QWidget):
    def __init__(self, app, user_name):
        super().__init__()

        self.app = app  # Ссылка на приложение для управления окнами
        self.user_name = user_name

        with open('recipes.json', 'r') as f:
            self.recipes = json.load(f)

        self.setWindowTitle("Recipe Generator")
        self.setGeometry(200, 200, 1000, 720)
        self.setStyleSheet("background-color: #2E8B57;")

        self.user_welcome = QLabel(f"Привет, {self.user_name}!", self)
        self.user_welcome.setGeometry(QRect(80, 20, 400, 50))
        self.user_welcome.setStyleSheet("font-size: 50px;"
                                        "font-family: 'Times New Roman';"
                                        "color: black;")

        #
        #
        #

        self.generate_button = QPushButton("Сгенерировать", self)
        self.generate_button.setGeometry(QRect(350, 620, 300, 70))
        self.generate_button.setStyleSheet("background-color: black;"
                                           "color: white;"
                                           "font-size: 30px;"
                                           "font-family: 'Times New Roman';")
        self.generate_button.clicked.connect(self.generate_recipe)

        #
        #
        #

        self.filter_button = QPushButton("Фильтр", self)
        self.filter_button.setGeometry(QRect(50, 620, 250, 70))
        self.filter_button.setStyleSheet("color: black;"
                                         "font-size: 35px;"
                                         "font-family: 'Times New Roman';")
        self.filter_button.clicked.connect(self.open_filter_window)

        #
        #
        #

        self.recipe_display = QTextEdit(self)
        self.recipe_display.setReadOnly(True)
        self.recipe_display.setGeometry(QRect(50, 90, 900, 500))
        self.recipe_display.setStyleSheet("background-color: #3CB371;"
                                          "color: black;"
                                          "font-size: 30px;")

        #
        #
        #

        self.time_label2 = QLabel(self)
        self.time_label2.setGeometry(QRect(670, 25, 200, 40))  # Расположение метки
        self.time_label2.setStyleSheet("font-size: 50px; "
                                       "font-family: 'Arial'; "
                                       "color: black;")
        self.time_label2.setAlignment(Qt.AlignCenter)

        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.update_time) 
        self.timer2.start(1000)  # Обновляем каждую секунду

        #
        #
        #

        self.stopwatch_button = QPushButton("Секундомер", self)
        self.stopwatch_button.setGeometry(QRect(700, 620, 250, 70))
        self.stopwatch_button.setStyleSheet("color: black;"
                                            "font-size: 35px;"
                                            "font-family: 'Times New Roman';")
        self.stopwatch_button.clicked.connect(self.open_stopwatch_window)

        #
        #
        #

        self.category_filter = "All"
        self.sugar_filter = False

    def filter_recipes(self):
        category = self.category_filter
        filtered_recipes = self.recipes

        if category != "All":
            filtered_recipes = [recipe for recipe in filtered_recipes if recipe["category"] == category]

        if self.sugar_filter:
            filtered_recipes = [recipe for recipe in filtered_recipes if not recipe['contains_sugar']]

        return filtered_recipes

    def generate_recipe(self):
        filtered_recipes = self.filter_recipes()
        if not filtered_recipes:
            self.recipe_display.setText("No recipes found for this category.")
            return
        recipe = random.choice(filtered_recipes)

        # Отображение 
        ingredients = ", ".join(recipe['ingredients'])
        text = f"Name: {recipe['name']}\nCategory: {recipe['category']}\nIngredients: {ingredients}\n\nInstructions:\n{recipe['instructions']}"
        self.recipe_display.setText(text)

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm")  # Текущее время
        self.time_label2.setText(current_time)

    def open_filter_window(self):
        self.filter_window = FilterWindow(self.app, self)
        self.filter_window.show()
        self.close()

    def open_stopwatch_window(self):
        self.stopwatch_window = StopwatchWindow()
        self.stopwatch_window.show()


class FilterWindow(QWidget):
    def __init__(self, app, main_window):
        super().__init__()

        self.app = app  # Ссылка на приложение
        self.main_window = main_window 

        self.setWindowTitle("Filter Recipes")
        self.setGeometry(300, 300, 700, 400)
        self.setStyleSheet("background-color: #2E8B57;")

        #
        #
        #

        self.sugar_filter = QCheckBox("No sugar", self)
        self.sugar_filter.setGeometry(QRect(350, 50, 300, 50))  
        self.sugar_filter.setStyleSheet("font-size: 30px; "
                                        "font-family: 'Times New Roman';")

        self.alcohol_filter = QCheckBox("No alcohol", self)
        self.alcohol_filter.setGeometry(QRect(350, 110, 300, 50))  
        self.alcohol_filter.setStyleSheet("font-size: 30px; "
                                          "font-family: 'Times New Roman';")

        self.milk_filter = QCheckBox("No milk", self)
        self.milk_filter.setGeometry(QRect(350, 170, 300, 50))  
        self.milk_filter.setStyleSheet("font-size: 30px; "
                                       "font-family: 'Times New Roman';")

        #
        #
        #

        self.category_filter2 = QComboBox(self)
        self.category_filter2.setGeometry(QRect(50, 50, 250, 70)) 
        self.category_filter2.addItems(["All", "breakfast", "lunch", "dinner", "sweets"])
        self.category_filter2.setStyleSheet("""
                            QComboBox {
                                font-size: 40px; 
                                font-family: 'Times New Roman';
                            }
                            QComboBox QAbstractItemView {
                                selection-background-color: black;  
                                selection-color: white;  
                            }
                            QComboBox:focus {
                                border: 2px solid black;  
                            }
                        """)

        #
        #
        #

        self.apply_button = QPushButton("OK", self)
        self.apply_button.setGeometry(QRect(25, 320, 650, 50)) 
        self.apply_button.setStyleSheet("background-color: black;"
                                        "color: white;"
                                        "font-size: 25px;"
                                        "font-family: 'Times New Roman';")
        self.apply_button.clicked.connect(self.apply_filters)

    def apply_filters(self):
        self.main_window.sugar_filter = self.sugar_filter.isChecked()
        self.main_window.alcohol_filter = self.alcohol_filter.isChecked()
        self.main_window.milk_filter = self.milk_filter.isChecked()
        self.main_window.category_filter = self.category_filter2.currentText()

        self.main_window.show()
        self.close()  


class StopwatchWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stopwatch")
        self.setGeometry(1200, 300, 400, 300)
        self.setStyleSheet("background-color: #2E8B57;")

        self.layout = QVBoxLayout(self)

        self.time_label = QLabel("00:00:00", self)
        self.time_label.setStyleSheet("font-size: 65px; "
                                      "font-family: 'Times New Roman'; "
                                      "color: white;")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.time_label)

        self.start_stop_button = QPushButton("Старт", self)
        self.start_stop_button.setStyleSheet("background-color: black;"
                                             "color: white;"
                                             "font-size: 20px;")
        self.start_stop_button.clicked.connect(self.start_stop)
        self.layout.addWidget(self.start_stop_button)

        self.reset_button = QPushButton("Сброс", self)
        self.reset_button.setStyleSheet("font-size: 20px;"
                                        "background-color: black;"
                                        "color: white;")
        self.reset_button.clicked.connect(self.reset)
        self.layout.addWidget(self.reset_button)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.time = QTime(0, 0, 0)
        self.running = False

    def start_stop(self):
        if not self.running:
            self.timer.start(1000)  
            self.start_stop_button.setText("Стоп")
        else:
            self.timer.stop()
            self.start_stop_button.setText("Старт")
        self.running = not self.running

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0)
        self.time_label.setText(self.time.toString("hh:mm:ss"))
        self.start_stop_button.setText("Старт")
        self.running = False

    def update_timer(self):
        self.time = self.time.addSecs(1)
        self.time_label.setText(self.time.toString("hh:mm:ss"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    welcome_window = WelcomeWindow(app)
    welcome_window.show()

    sys.exit(app.exec_())
