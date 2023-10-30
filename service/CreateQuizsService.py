from service.data.quiz.quiz_bsort import *
from service.data.quiz.quiz_BstHeapNormalTree import *
from service.data.quiz.quiz_PostfixPrefix import *
from service.data.quiz.quiz_WorstComplexity import *


class CreateQuizsService:

    def __init__(self):
        self.quizes=[]
        self.candidate=[]
        bsort=quiz_bsort()
        BSTHeapNormal=quiz_BstHeapNormalTree()
        PostfixPrefix=quiz_PostfixPrefix()
        WorstComplexity=quiz_WorstComplexity()
        self.candidate.append(bsort)
        self.candidate.append(BSTHeapNormal)
        self.candidate.append(PostfixPrefix)
        self.candidate.append(WorstComplexity)

    def createQuizs(self, number):
        for i in range(0, int(number)):
            self.candidate[i].setQuiz(i+1)
            quiz=self.candidate[i].quiz
            #여기까지 문제 생성
            quiz.mixAnswer()
            #직렬화
            self.quizes.append(quiz.changToDict())
        return self.quizes
