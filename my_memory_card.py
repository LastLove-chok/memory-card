from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
QHBoxLayout, QVBoxLayout, QLabel, 
QMessageBox, QRadioButton, QGroupBox, QButtonGroup)
#####################
from random import shuffle, randint

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.setMinimumSize(400, 200)
main_layout = QVBoxLayout()
 
question = QLabel('<b></b>')
btn_answer1 = QRadioButton('')
btn_answer2 = QRadioButton('')
btn_answer3 = QRadioButton('')
btn_answer4 = QRadioButton('')

#####################
radio_group = QButtonGroup()
radio_group.addButton(btn_answer1)
radio_group.addButton(btn_answer2)
radio_group.addButton(btn_answer3)
radio_group.addButton(btn_answer4)
result_label = QLabel('Правильно/Неправильно')
right_label = QLabel('2015')

answer_groupbox = QGroupBox("Варианты")
result_groupbox = QGroupBox("Результат")
btn_next = QPushButton("Ответить") 

column1 = QVBoxLayout()
column1.addWidget(btn_answer1)
column1.addWidget(btn_answer2)
column2 = QVBoxLayout()
column2.addWidget(btn_answer3)
column2.addWidget(btn_answer4)
answers_layout = QHBoxLayout()
answers_layout.addLayout(column1)
answers_layout.addLayout(column2)
answer_groupbox.setLayout(answers_layout)
result_layout = QVBoxLayout()
result_layout.addWidget(result_label)
result_layout.addWidget(right_label, alignment=Qt.AlignHCenter)
result_layout.addSpacing(30)
result_groupbox.setLayout(result_layout)
#####################
result_groupbox.hide()
#####################
main_layout.addWidget(question, alignment=Qt.AlignHCenter)
main_layout.addWidget(answer_groupbox)
main_layout.addWidget(result_groupbox)
main_layout.addWidget(btn_next)

main_win.setLayout(main_layout)

answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]


main_win.total_questions = 0
main_win.correct_answers = 0
main_win.questions_list = []
main_win.cur_question = 0

#####################
def show_result():
    answer_groupbox.hide()
    result_groupbox.show()
    btn_next.setText("Следующий вопрос")
    
def show_question():
    answer_groupbox.show()
    result_groupbox.hide()
    btn_next.setText("Ответить")
    radio_group.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    radio_group.setExclusive(True)

def print_statistics():
    total = main_win.total_questions
    correct = main_win.correct_answers
    if total > 0:
        rating = (correct / total) * 100
        rating = int(rating) 
    else:
        rating = 0
    print(f"Статистика:")
    print(f"Всего вопросов: {total}")
    print(f"Правильных ответов: {correct}")
    print(f"Рейтинг: {rating}%")
    print("-" * 30)

#####################
def ask(q_obj):
    shuffle(answers)
    answers[0].setText(q_obj.right_answer)
    answers[1].setText(q_obj.wrong1)
    answers[2].setText(q_obj.wrong2)
    answers[3].setText(q_obj.wrong3)
    question.setText(q_obj.question)
    right_label.setText(q_obj.right_answer)
    show_question()
    print(q_obj.question)
    print_statistics()

#####################
def check_answer():
    main_win.total_questions += 1
    
    if answers[0].isChecked():
        result_label.setText("Правильно")
        main_win.correct_answers += 1
    else:
        result_label.setText("Неправильно")
    
    show_result()
    print_statistics()

def next_question():
    if main_win.questions_list:
        main_win.cur_question = randint(0, len(main_win.questions_list) - 1)
        ask(main_win.questions_list[main_win.cur_question])

def click_ok():
    if btn_next.text() == "Ответить":
        check_answer()
    else:
        next_question()


questions_data = [
    Question("Сколько будет 2+2?", "4", "2", "3", "5"),
    Question("Столица Франции?", "Париж", "Лондон", "Берлин", "Мадрид"),
    Question("Сколько дней в неделе?", "7", "5", "6", "8"),
    Question("Сколько будет 15-7?", "8", "6", "7", "9"),
    Question("Сколько будет 6*7?", "42", "36", "48", "49"),
    Question("Столица Италии?", "Рим", "Милан", "Венеция", "Флоренция"),
    Question("Какая собака самая быстрая?", "Грейхаунд", "Борзая", "Доберман", "Хаски"),
    Question("Какая планета самая большая?", "Юпитер", "Сатурн", "Нептун", "Земля"),
    Question("Сколько цветов в радуге?", "7", "5", "6", "8"),
    Question("Кто написал «Война и мир»?", "Лев Толстой", "Фёдор Достоевский", "Антон Чехов", "Иван Тургенев"),
    Question("Самый большой океан?", "Тихий", "Атлантический", "Индийский", "Северный Ледовитый"),
    Question("Сколько будет 12*12?", "144", "124", "132", "148"),
    Question("Какое животное самое высокое?", "Жираф", "Слон", "Лошадь", "Верблюд"),
    Question("Столица Японии?", "Токио", "Осака", "Киото", "Нагоя"),
    Question("Сколько минут в часе?", "60", "30", "90", "120"),
    Question("Какой газ преобладает в атмосфере Земли?", "Азот", "Кислород", "Углекислый газ", "Водород"),
    Question("Сколько будет 100-37?", "63", "73", "67", "53"),
    Question("Кто изобрёл лампочку?", "Томас Эдисон", "Никола Тесла", "Александр Белл", "Майкл Фарадей"),
    Question("Самая длинная река в мире?", "Нил", "Амазонка", "Янцзы", "Миссисипи"),
    Question("Сколько сторон у шестиугольника?", "6", "5", "7", "8"),
    Question("Какая страна самая большая по площади?", "Россия", "Канада", "Китай", "США"),
    Question("Сколько будет 9*9?", "81", "72", "89", "99"),
    Question("Какое море самое солёное?", "Мёртвое море", "Красное море", "Средиземное море", "Чёрное море"),
    Question("Кто написал «Гамлета»?", "Уильям Шекспир", "Чарльз Диккенс", "Джордж Оруэлл", "Марк Твен"),
]
main_win.questions_list = questions_data

next_question()

btn_next.clicked.connect(click_ok)
main_win.show()
app.exec_()
