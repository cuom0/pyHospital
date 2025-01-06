import datetime

class Patient:
    def __init__(self, name, surname, tax_code, birth_date, birth_place):
        self.name = name
        self.surname = surname
        self.tax_code = tax_code
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.illnesses = []
        self.admission_date = None
        self.recovery_date = None

    def assign_illness(self, illness_name, description):
        self.illnesses.append({"name": illness_name, "description": description})

    def discharge(self):
        self.recovery_date = datetime.date.today()
