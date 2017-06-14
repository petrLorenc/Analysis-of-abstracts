class Thesis():
    """ Object of one entry in table """

    def __init__(self, name_thesis, name_student, abstract_url, thesis_url, supervisor, opponent, grade_supervisor,
                 grade_opponent):
        self.name_thesis = name_thesis
        self.name_student = name_student
        self.abstract_url = abstract_url
        self.thesis_url = thesis_url
        self.supervisor = supervisor
        self.opponent = opponent
        self.grade_opponent = grade_opponent
        self.grade_supervisor = grade_supervisor
