#создай приложение для запоминания информации

#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QRadioButton, QVBoxLayout, QMessageBox, QGroupBox, QButtonGroup
)
from random import shuffle
from random import randint

class Question:
    def __init__(self, question, rans, wans1, wans2, wans3):
        self.quest = question
        self.rans = rans
        self.wans1 = wans1
        self.wans2 = wans2
        self.wans3 = wans3
        
def show_question():
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
    ans_group.hide()
    rbt_group.show()
    btn.setText('Ответить') 

def show_result():
    txt3.setText('Количество заданых вопросов: ' + str(total))
    txt4.setText('Количество правельных вопросов: ' + str(score))
    txt5.setText('Рейтинг: ' + str(int(score/total*100)) +'%')
    rbt_group.hide()
    ans_group.show()
    btn.setText('Следующий вопрос')   

def start_test():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question() 

def next_question():
    global total
    total += 1
    ask(q_list[randint(0, len(q_list) -1 )])

def ask(q):
    shuffle(answers)
    answers[0].setText(q.rans)
    answers[1].setText(q.wans1)
    answers[2].setText(q.wans2)
    answers[3].setText(q.wans3)
    text.setText(q.quest)
    txt2.setText('Правильный ответ:' + q.rans)
    show_question()

def check_answer():
    global score
    if answers[0].isChecked():
        score += 1
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')


def show_correct(res):
    txt1.setText(res)
    show_result()

#создание элементов интерфейса
num = 0
total = 1
score = 0

app = QApplication([])
main_win = QWidget()
main_win.resize(500, 250)
main_win.setWindowTitle('Конкурс')

text = QLabel('Какой национальности не существует?')

#создание группы с радио кнопками
rbt_group =QGroupBox('Варианты ответов')

rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')

answers = [rbtn1, rbtn2,rbtn3, rbtn4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QVBoxLayout()

line1.addWidget(rbtn1)
line1.addWidget(rbtn2)
line2.addWidget(rbtn3)
line2.addWidget(rbtn4)
line3.addLayout(line1)
line3.addLayout(line2)

rbt_group.setLayout(line3)

#создание группы  1
ans_group = QGroupBox('Результат теста')

btn = QPushButton('Ответить')

txt1 = QLabel('Правильно/Неправильно')
txt2 = QLabel('Правильный ответ')
txt3 = QLabel()
txt4 = QLabel()
txt5 = QLabel()

line4 = QVBoxLayout()
line4.addWidget(txt1, alignment = Qt.AlignLeft, stretch = 3)
line4.addWidget(txt2, alignment = Qt.AlignCenter, stretch = 3)
line4.addWidget(txt3, alignment = Qt.AlignLeft, stretch = 0.5)
line4.addWidget(txt4, alignment = Qt.AlignLeft, stretch = 0.5)
line4.addWidget(txt5, alignment = Qt.AlignLeft, stretch = 0.5)

ans_group.setLayout(line4)

#привязка элементов к вертикальной линии
main_line = QVBoxLayout()
hline1 = QHBoxLayout()
hline2 = QHBoxLayout()

hline1.addWidget(text, alignment = Qt.AlignCenter)
hline2.addWidget(btn, alignment = Qt.AlignCenter)

main_line.addLayout(hline1)
main_line.addWidget(rbt_group, stretch = 1)
main_line.addWidget(ans_group, stretch = 1)
main_line.addLayout(hline2)

main_win.setLayout(main_line)

#обработка событий
q_list = list()
q1 = Question('Государственный язык Бразилии', 'Португальский', 'Белорусский', 'Русский', 'Немецкий')
q_list.append(q1)
q2 = Question('Государственный язык Турции', 'Турецкий', 'Японский', 'Китайский', 'Английский')
q_list.append(q2)
q3 = Question('Государственный язык Франции', 'Французский', 'Польский', 'Итальянский', 'Греческий')
q_list.append(q3)
q4 = Question('Государственный язык Германии', 'Немецкий', 'Корейский', 'Итальянский', 'Арабский')
q_list.append(q4)
q5 = Question('Государственный язык Китая', 'Китайский', 'Грузинский', 'Турецкий', 'Греческий')
q_list.append(q5)
q6 = Question('Государственный язык Казахстана', 'Казахский', 'Испанский', 'Украинский', 'Финский')
q_list.append(q6)
q7 = Question('Государственный язык Танзании', 'Английский', 'Ирландский', 'Абхазский', 'Нидерландский')
q_list.append(q7)
q8 = Question('Государственный язык Мальты', 'Английский', 'Французский', 'Кечуа', 'Рунди')
q_list.append(q8)
q9 = Question('Государственный язык Эстонии', 'Эстонский', 'Дзонг-кэ', 'Тетум', 'Пулар')
q_list.append(q9)
q10 = Question('Государственный язык Польши', 'Польский', 'Испанский', 'Ирит', 'Урду')
q_list.append(q10)

ask(q_list[0])
btn.clicked.connect(start_test)

#button.clicked.connect(generate)

#запуск приложения
main_win.show()
app.exec_()