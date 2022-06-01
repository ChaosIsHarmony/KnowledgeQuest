import json
import random

from .. import common
from ..interfaces.IQuestion import IQuestion
from ..factories.QuestionFactory import QuestionFactory

from functools import cmp_to_key
from typing import List


def deserialize_questions(questionsJson: List[str]) -> List[IQuestion]:
    questions = []

    for question in questionsJson:
        questions.append(QuestionFactory.from_dict(question))

    return questions


def fetch_questions(path: str) -> List[IQuestion]:
    questionsFileContents = common.load_file(path)
    questions = deserialize_questions(questionsFileContents)

    return questions


def create_inquisition(questions: List[IQuestion], nQuestions: int, accuracy_threshold: float = 0.6) -> List[IQuestion]:
    '''
    Algorithm follows spaced repetition protocol:

        Prioritize in this order:
            - Lowest correct/asked ratio
            - Longest time between last asked and today

    Returns a shuffled array of size min(nQuestions, len(questions))
    '''
    inquisitionQuestions = []

    questions = sorted(questions, key=cmp_to_key(common.compare_questions_by_accuracy))

    # if nQuestions exceeds len(questions)
    if nQuestions > len(questions):
        random.shuffle(questions)
        return questions

    # add questions so long as it satisfies two conditions:
    # 1.) does not exceed nQuestions
    # 2.) does not exceed accuracy_threshold
    ind = 0
    while len(inquisitionQuestions) < nQuestions:
        if questions[ind].get_accuracy() < accuracy_threshold:
            inquisitionQuestions.append(questions[ind])
            ind += 1
        else:
            break

    # if satsifies nQuestions req
    if len(inquisitionQuestions) == nQuestions:
        random.shuffle(inquisitionQuestions)
        return inquisitionQuestions

    # otherwise, add more questions until meets nQuestions or no more questions
    questions = sorted(questions, key=cmp_to_key(common.compare_questions_by_last_asked))
    ind = 0
    while len(inquisitionQuestions) < nQuestions:
        if questions[ind].get_accuracy() >= accuracy_threshold:
            inquisitionQuestions.append(questions[ind])
        ind += 1

    # return list
    random.shuffle(inquisitionQuestions)
    return inquisitionQuestions


def perform_inquisition(questions: List[IQuestion]) -> None:
    '''
    1.) Ask question
    2.) User answers
    3.) Result displayed
    4.) IQuestion stats are updated
    5.) If more questions are left, go to step 1
    '''
    for question in questions:
        # ask question
        print(question.get_text())
        random.shuffle(question.get_answers())
        for i, answer in enumerate(question.get_answers()):
            print(f"{i}.) {answer}")
        # accept input
        nAnswer = ""
        while not isinstance(nAnswer, int):
            nAnswer = int(input("Correct answer [#]: "))
        # show result
        if question.get_answers()[nAnswer] == question.get_answer():
            question.increment_num_times_answered_correctly()
            print("Correct!")
        else:
            print(f"Incorrect.\nThe correct answer is: {question.get_answer()}")
        question.increment_num_times_asked()
        question.update_last_asked()


def run() -> None:
    '''
    0.) Load questions, calculate which questions need asking
    1.) Query for quiz length: Measured in # of questions
    2.) Create quiz based on results of steps 0 & 1
    3.) Take quiz
    '''
    questions = fetch_questions(common.QUESTIONS_FILEPATH)

    if len(questions) < 1:
        return

    while True:
        try:
            nQuestions = int(input("How many questions? "))
            break
        except:
            print("Invalid input. Must be a number.")

    inquisition = create_inquisition(questions, nQuestions)
    perform_inquisition(inquisition)
    # update all question stats
    listOfUpdatedQuestions = list(filter(lambda q: not any(q2.get_id() == q.get_id() for q2 in inquisition), questions))
    listOfUpdatedQuestions.extend(inquisition)
    common.write_file(listOfUpdatedQuestions, common.QUESTIONS_FILEPATH)
