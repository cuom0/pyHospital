import random

def get_predefined_illnesses():
    return [
        {"name": "Flu", "description": "A common viral infection that affects the respiratory system."},
        {"name": "Pneumonia", "description": "An infection that inflames air sacs in one or both lungs."},
        {"name": "Diabetes", "description": "A chronic condition that affects how the body processes blood sugar."},
        {"name": "Hypertension", "description": "A condition in which the force of the blood against the artery walls is too high."},
        {"name": "Covid-19", "description": "A contagious disease caused by the coronavirus SARS-CoV-2."},
        {"name": "Death", "description": "The irreversible cessation of all biological functions."}
    ]

def random_illness():
    illnesses = get_predefined_illnesses()
    return random.choice(illnesses)
