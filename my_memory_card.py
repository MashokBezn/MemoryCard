#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,QPushButton,QLabel,QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3
app=QApplication([])
window=QWidget()
window.setWindowTitle('Memo Card')

window.cur_question = -1

btn_OK=QPushButton('Ответить')
lb_Question=QLabel('Государственный язык Бразилии!')

RadioGroupBox=QGroupBox('Варианты ответов')
rbtn_1=QRadioButton('Португальсуий')
rbtn_2=QRadioButton('Итальянский')
rbtn_3=QRadioButton('Испанский')
rbtn_4=QRadioButton('Бразильский')
answers=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]
RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
AnsGroupBox=QGroupBox('Результат теста')
lb_Result=QLabel('Прав ты или нет?')
lb_Correct=QLabel('Ответ будет тут!')
layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()

layout_line1.addWidget(lb_Question)
layout_line2.addWidget(AnsGroupBox)
layout_line2.addWidget(RadioGroupBox)

AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK,stretch=2)
layout_line3.addStretch(1)

layout_res=QVBoxLayout()
layout_res.addWidget(lb_Result,alignment=(Qt.AlignLeft| Qt.AlignTop))
layout_res.addWidget(lb_Correct,alignment=Qt.AlignHCenter,stretch=2)
layout_res.addWidget(btn_OK,alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_card=QVBoxLayout()

layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
AnsGroupBox.hide() 

def show_results():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def click_OK():
    if 'Ответить'==btn_OK.text():
        check_answer()
    else:
        next_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score+=1
        print('Статистика\n-Всего вопросов:',window.total,'\nПравильных ответов:',window.score)
        print('Рейтинг:',(window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked():
            show_correct('Неверно')
            print('Рейтинг:',(window.score/window.total*100),'%')
def next_question():
    window.total+=1
    print('Статистика\n-Всего вопросов:',window.total,'\nПравильных ответов:',window.score)
    cur_question=randint(0,len(question_list)-1)

    q=question_list[cur_question]
    ask(q)
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_results()
question_list=[]
question_list.append(Question(' Что в Российской империи было вещевым эквивалентом денег?','Шкуры пушных зверей','Крупный рогатый скот','Табак','Женские серьги'))
question_list.append(Question('Российский мультфильм, удостоенный «Оскара», — это…','«Старик и море»','«Простоквашино»','«Винни-Пух»','«Ну, погоди!»'))
question_list.append(Question('Основой для «Сказки о рыбаке и рыбке Пушкина послужила сказка братьев Гримм «Рыбак и его жена». В ней немецкая «коллега» нашей старухи превратилась в:','Папу Римского','Королеву','Директора рыбзавода','Командира отряда водолазов '))
question_list.append(Question('Какую пошлину ввели в XII  веке в Англии для того чтобы заставить мужчин пойти на войну?','Налог на трусость','Налог на отсутсвие формы','Налог на тунеянство','Налог на отсутствие сапог'))
question_list.append(Question('Туристы, приезжающие на Майорку, обязаны заплатить налог…','На солнце','На пальмы','На плавки','На пляж'))
question_list.append(Question('Кто из президентов США написал свой собственный рассказ про Шерлока Холмса?','Франклин Рузвельт','Джон Кеннеди','Рональд Рейган','Дональд Трамп'))
question_list.append(Question('Государственый язык Бразилии','Португальский','Английский','Испанский','Бразильский'))
question_list.append(Question('2+2*2','6','8','4','12'))
question_list.append(Question('Национальная хижина якутов','Ураса','Юрта','Иглу','Хата'))
question_list.append(Question('Где находится 0 меридиан?','Гринвич','Рио-де-жанейро','Берлин','Бразилия'))

window=QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')

btn_OK.clicked.connect(click_OK)

window.score=0
window.total=0
next_question()
window.resize(400,300)
window.show()
app.exec()