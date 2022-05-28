from .IQuestion import IQuestion
from .Question import Question

class QuestionFactory:

    @classmethod
    def from_dict(cls, attrDict) -> IQuestion:
        return Question(attrDict["id"],
                        attrDict["question_text"],
                        attrDict["answers"],
                        attrDict["answer"],
                        attrDict["n_times_asked"],
                        attrDict["n_times_correctly_answered"],
                        attrDict["last_asked"],
                        attrDict["skills"],
                        attrDict["tags"])


