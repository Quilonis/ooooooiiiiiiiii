from PyQt5.QtCore import QAbstractListModel , QModelIndex , Qt
from random import randint,shuffle




class question():
    def __init__(self,question,answer,wrongasnwer1,wronganswer2,wronganswer3):
        self.question=question
        self.answer=answer
        self.wronganswer1=wrongasnwer1
        self.wronganswer2=wronganswer2
        self.wronganswer3=wronganswer3
        self.is_active=True
        self.attempts=0
        self.correct=0

    def got_right(self):
        self.attempts += 1
        self.correct += 1

    def got_wrong(self):
        self.attempts+=1

class questionView():
    def __init__(self,form_model,question,answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.form_model=form_model
        self.question=question
        self.answer=answer
        self.wronganswer1=wrong_answer1
        self.wrong_answer2=wrong_answer2
        self.wrong_answer3=wrong_answer3

    def change(self,form_model):
        self.form_model=form_model

    def show(self):
        self.question.setText(self.form_model.question)
        self.answer.setText(self.form_model.answer)
        self.wrong_answer1.setText(self.form_model.wrong_answer1)
        self.wrong_answer2.setText(self.form_model.wrong_answer2)
        self.wrong_answer3.setText(self,form_model.wrong_answer3)


class questionEdit(questionView):
    def save_question(self):
        self.form_model.question = self.question.text()
    def save_answer(self):
        self.form_model.answer = self.answer.text()

    def save_wrong(self):
        self.form_model.wrong_answer1 = selfwrong_answer1.text()
        self.form_model.wrong_answer2 = selfwrong_answer2.text()
        self.form_model.wrong_answer3 = selfwrong_answer3.text()

    def set_connects(self):
        self.question.editingFinished.connect(self.save_question)
        self.answer.editingFinished.connect(self.save_answer)
        self.wrong_answer1.editingFinished.connect(self.save_wrong)
        self.wrong_answer2.editingFinished.connect(self.save_wrong)
        self.wrong_answer3.editingFinished.connect(self.save_wrong)

    def __init__(self, form_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        questionView.__init__(self,form_model=form_model,question=question,answer=answer,wrong_answer1=wrong_answer1,wrong_answer2=wrong_answer2,wrong_answer3=wrong_answer3)
        self.set_connects()

text_correct="Correct"
text_wrong="InCorrect"




class answerCheck(questionView):
    def __init__(self, form_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3,showed_answer,result):
        questionView.__init__(self,form_model=form_model,question=question,answer=answer,wrong_answer1=wrong_answer1,wrong_answer2=wrong_answer2,wrong_answer3=wrong_answer3)
        self.showed_answer = showed_answer
        self.result = result

    def check(self):
        if self.answer.isChecked():
            self.result.setText(text_correct)
            self.showed_answer.setText(self.form_model.answer)
            self.form_model.got_right()

        else:
            self.result.setText(text_correct)
            self.showed_answer.setText(self.form_model.answer)
            self.form_model.got_wrong()



class questionListModel(QAbstractListModel):
    def __init__(self,parent=None):
        QAbstractListModel.__init__(self,parent)
        self.form_list = []

    def rowCount(self,index):
        return len(self.fomr_list)

    def data(self,index,role):
        if role == Qt.DisplayRole:
            form = self.form_list[index_row()]
            return form.question

    def insertRows(self,parent=QModelIndex()):
        position=len(self.form_list)
        self.beginInsertRows(parent,position,position)
        self.form_list.append(position)
        self.endRemoveRows()
        return True

    def removeRows(self,position,parent=QModelIndex()):
        self.beginRemoveRows(parent,position,position)
        self.form_list.pop(position)
        self.endRemoveRows()
        return True

    def random_question(self):
        total=len(self.form_list)
        current=randint(0,total-1)
        return self.form_list[current]

def random_AnswerCheck(list_model,w_question,widgets_list,w_showed_answer,w_result):
    form=list_model.random_question()
    shuffle(widgets_list)
    form_cards=answerCheck(form,w_question,widgets_list[0],widgets_list[1],widgets_list[2],widgets_list[3],w_showed_answer,w_result)
    return form_card

