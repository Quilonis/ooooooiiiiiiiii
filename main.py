from PyQt5.Qtcore import Qt
from PyQt5.QtWidgets import (QApplication,QSpinBox,QWidget,QPushButton,QLabel,QHBoxLayout,QVBoxLayout,QRadioButton,QGroupBox)




layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)