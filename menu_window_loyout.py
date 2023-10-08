from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QSpinBox,QWidget,QPushButton,QLabel,QHBoxLayout,QVBoxLayout
                    ,QRadioButton,QGroupBox,QLineEdit)

app=QApplication([])
main_win=QWidget()

question_label=QLabel("Введть запитання")
correct_answer_label=QLabel("ведіть правильну відповідь")
answer1_label=QLabel("Введіть першу хибну відповідь")
answer2_label=QLabel("Введіть другу хибну відповідь")
answer3_label=QLabel("Введіть третю хибну відповідь")

question=QLineEdit()
correct_answer= QLineEdit()
answer1=QLineEdit()
answer2=QLineEdit()
answer3=QLineEdit()

line1=QHBoxLayout()
line2=QHBoxLayout()
line3=QHBoxLayout()
line4=QHBoxLayout()
line5=QHBoxLayout()


main_line=QVBoxLayout()

line1.addWidget(question_label)
line1.addWidget(question)

line2.addWidget(correct_answer_label)
line2.addWidget(correct_answer)

line3.addWidget(answer1_label)
line3.addWidget(answer1)

line4.addWidget(answer2_label)
line4.addWidget(answer2)

line5.addWidget(answer3_label)
line5.addWidget(answer3)

main_line.addLayout(line1)
main_line.addLayout(line2)
main_line.addLayout(line3)
main_line.addLayout(line4)
main_line.addLayout(line5)

btn_add=QPushButton("Додати запитання")
btn_clean=QPushButton("Очистити")

btn_back=QPushButton("Назад")

line6=QHBoxLayout()
line6.addWidget(btn_add)
line6.addWidget(btn_clean)

main_line.addLayout(line6)

stats_label=QLabel("СТАТИСТИКА")
corrects=QLabel("Вірних вілповідей")
succsesfull=QLabel("Успішність")
attempts=QLabel("Разів відповіли")

stats_label.setStyleSheet("font-weight:bold")

line7=QHBoxLayout()
line8=QVBoxLayout()

line8.addWidget(stats_label,alignment=Qt.AlignLeft)
line8.addWidget(corrects,alignment=Qt.AlignLeft)
line8.addWidget(succsesfull,alignment=Qt.AlignLeft)
line8.addWidget(attempts,alignment=Qt.AlignLeft)
line8.addWidget(btn_back,alignment=Qt.AlignCenter)


line7.addWidget(stats_label)

main_line.addLayout(line7)
main_line.addLayout(line8)

main_win.setLayout(main_line)
main_win.show()
app.exec_()