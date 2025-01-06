# A code by cuom0_ (https://github.com/cuom0)
from patient import Patient
from illnesses import get_predefined_illnesses
import datetime  # Modulo per gestire date e orari
import json

class Hospital:
    def __init__(self):
        # Inizializza il sistema caricando i pazienti e le malattie dai file
        self.patients = self.load_patients()
        self.illnesses = self.load_illnesses()

    def load_patients(self):
        # Carica i pazienti salvati in un file JSON, se non esiste restituisce lista vuota
        try:
            with open("patients.json", "r") as file:
                data = json.load(file)
                return [
                    Patient(
                        patient["name"],
                        patient["surname"],
                        patient["tax_code"],
                        datetime.datetime.strptime(patient["birth_date"], "%Y-%m-%d").date(),
                        patient["birth_place"]
                    ) for patient in data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_patients(self):
        # Salva i pazienti attualmente in memoria su un file JSON
        with open("patients.json", "w") as file:
            json.dump([
                {
                    "name": p.name,
                    "surname": p.surname,
                    "tax_code": p.tax_code,
                    "birth_date": p.birth_date.strftime("%Y-%m-%d"),
                    "birth_place": p.birth_place,
                    "illnesses": p.illnesses,
                    "admission_date": p.admission_date.strftime("%Y-%m-%d") if p.admission_date else None, #Questa condizione permette di stampare la data di ammissione solo se è stata assegnata, altrimenti stampa None
                    "recovery_date": p.recovery_date.strftime("%Y-%m-%d") if p.recovery_date else None
                } for p in self.patients
            ], file, indent=4)

    def load_illnesses(self):
        try:
            with open("illnesses.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return get_predefined_illnesses()

    def save_illnesses(self):
        with open("illnesses.json", "w") as file:
            json.dump(self.illnesses, file, indent=4)

    def add_patient(self):
        name = input("Enter patient's name: ")
        surname = input("Enter patient's surname: ")
        tax_code = input("Enter patient's tax code: ")
        birth_date = input("Enter patient's date of birth (YYYY-MM-DD) (In that exact format): ")
        birth_place = input("Enter patient's place of birth: ")

        try:
            birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Patient not added.")
            return

        patient = Patient(name, surname, tax_code, birth_date, birth_place)
        self.patients.append(patient)
        self.save_patients()
        print("Patient added successfully.")

    def modify_patient(self):
        self.list_patients()
        patient_index = input("Select a patient by number to modify: ")

        if not patient_index.isdigit() or not (1 <= int(patient_index) <= len(self.patients)):
            print("Invalid selection.")
            return

        patient = self.patients[int(patient_index) - 1]
        print(f"Modifying patient: {patient.name} {patient.surname}")

        patient.name = input(f"Enter new name (or press Enter to keep '{patient.name}'): ") or patient.name
        patient.surname = input(f"Enter new surname (or press Enter to keep '{patient.surname}'): ") or patient.surname
        patient.tax_code = input(f"Enter new tax code (or press Enter to keep '{patient.tax_code}'): ") or patient.tax_code
        patient.birth_place = input(f"Enter new birth place (or press Enter to keep '{patient.birth_place}'): ") or patient.birth_place

        self.save_patients()
        print("Patient modified successfully.")

    def delete_patient(self):
        self.list_patients()
        patient_index = input("Select a patient by number to delete: ")

        if not patient_index.isdigit() or not (1 <= int(patient_index) <= len(self.patients)):
            print("Invalid selection.")
            return

        patient = self.patients.pop(int(patient_index) - 1)
        self.save_patients()
        print(f"Patient {patient.name} {patient.surname} has been deleted.")

    def manage_illnesses(self):
        print("""
        ========== Manage Illnesses ==========
        1. Add a new illness
        2. Remove an existing illness
        3. List all illnesses
        """)

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter illness name: ")
            description = input("Enter illness description: ")
            self.illnesses.append({"name": name, "description": description})
            self.save_illnesses()
            print("Illness added successfully.")
        elif choice == "2":
            for i, illness in enumerate(self.illnesses, 1): #enumarate() restituisce una tupla con l'indice e l'elemento della lista, in questo caso l'indice è i e l'elemento è illness
                print(f"{i}. {illness['name']}") #Poi stampa l'indice e il nome della malattia, partendo da 1
            illness_index = input("Select an illness by number to remove: ") #Chiede all'utente di selezionare una malattia da rimuovere

            if not illness_index.isdigit() or not (1 <= int(illness_index) <= len(self.illnesses)): #Controlla se l'input è un numero e se è compreso tra 1 e il numero di malattie
                print("Invalid selection.") #Se non lo è, stampa un messaggio di errore e ritorna
                return

            removed = self.illnesses.pop(int(illness_index) - 1)
            self.save_illnesses()
            print(f"Illness '{removed['name']}' has been removed.")
        elif choice == "3":
            print("Illnesses:")
            print("\n".join([
                f"- {illness['name']}: {illness['description']}" for illness in self.illnesses
            ]))
        else:
            print("Invalid option.")

    def list_patients(self):
        if not self.patients:
            print("No patients currently in the hospital.")
            return

        print("\n========== List of Patients ==========")
        for patient in self.patients:
            print(f"""
            Name: {patient.name}
            Surname: {patient.surname}
            Tax Code: {patient.tax_code}
            Birth Date: {patient.birth_date}
            Birth Place: {patient.birth_place}
            Illnesses: {', '.join([ill['name'] for ill in patient.illnesses]) if patient.illnesses else 'None'} 
            Admission Date: {patient.admission_date}
            Recovery Date: {patient.recovery_date}
            ----------------------------------------
            =======================================
            """)
            #join() è un metodo che unisce gli elementi di una lista in una stringa, separandoli con una virgola, si è scelta la virgola come separatore al .join()
        

    def assign_illness_to_patient(self):
        self.list_patients()
        patient_index = input("Select a patient by number to assign an illness: ")

        if not patient_index.isdigit() or not (1 <= int(patient_index) <= len(self.patients)): #Controlla se l'input è un numero e se è compreso tra 1 e il numero di pazienti
            print("Invalid selection.") #Se non lo è, stampa un messaggio di errore e ritorna
            return

        patient = self.patients[int(patient_index) - 1] #Prende il paziente selezionato, togliendo 1 perchè l'indice parte da 0
        print("\nAvailable illnesses:") #Stampa le malattie disponibili
        for i, illness in enumerate(self.illnesses, 1): #enumarate() restituisce una tupla con l'indice e l'elemento della lista, in questo caso l'indice è i e l'elemento è illness
            print(f"{i}. {illness['name']}") #Poi stampa l'indice e il nome della malattia, partendo da 1

        illness_index = input("Select an illness by number: ") #Chiede all'utente di selezionare una malattia

        if not illness_index.isdigit() or not (1 <= int(illness_index) <= len(self.illnesses)): #Controlla se l'input è un numero e se è compreso tra 1 e il numero di malattie
            print("Invalid selection.") #Se non lo è, stampa un messaggio di errore e ritorna
            return

        selected_illness = self.illnesses[int(illness_index) - 1] #Prende la malattia selezionata, togliendo 1 perchè l'indice parte da 0
        patient.assign_illness(selected_illness["name"], selected_illness["description"]) #Assegna la malattia al paziente attraverso il metodo assign_illness() definito nella classe Patient in patient.py

        # Imposta la data di ammissione solo se non è già presente
        if not patient.admission_date: #Se la data di ammissione non è stata assegnata (è None)
            patient.admission_date = datetime.date.today() #Assegna la data di oggi come data di ammissione

        self.save_patients() #Salva i pazienti modificati
        print(f"Illness '{selected_illness['name']}' assigned to patient {patient.name} {patient.surname}.") #E infine lo comunica all'utente
        print(f"Admission date set to {patient.admission_date}.")


    def discharge_patient(self):
        self.list_patients()
        patient_index = input("Select a patient by number to discharge: ")

        if not patient_index.isdigit() or not (1 <= int(patient_index) <= len(self.patients)): #Questa condizione controlla se l'input è un numero e se è compreso tra 1 e il numero di pazienti. len(self.patients) restituisce il numero di pazienti
            #or not sarebbe come scrivere "if not (patient_index.isdigit() and (1 <= int(patient_index) <= len(self.patients))):" o in C# "if (!(patient_index.isdigit() && (1 <= int(patient_index) <= len(self.patients))):"
            print("Invalid selection.")
            return

        patient = self.patients[int(patient_index) - 1] #Prende il paziente selezionato, togliendo 1 perchè l'indice parte da 0
        patient.discharge() #Va a modificare la data di guarigione del paziente attraverso il metodo discharge() definito nella classe Patient in patient.py
        self.save_patients() #Ovviamente salva i pazienti modificati
        print(f"Patient {patient.name} {patient.surname} has been discharged successfully.") #E infine lo comunica all'utente

    def run(self):
        while True:
            print("""
            ========== Hospital Management ==========
            1. Add a new patient
            2. Modify a patient
            3. Delete a patient
            4. Assign an illness to a patient
            5. Discharge a patient
            6. List all patients
            7. Manage illnesses
            8. Exit
            """)

            choice = input("Select an option: ")

            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.modify_patient()
            elif choice == "3":
                self.delete_patient()
            elif choice == "4":
                self.assign_illness_to_patient()
            elif choice == "5":
                self.discharge_patient()
            elif choice == "6":
                self.list_patients()
            elif choice == "7":
                self.manage_illnesses()
            elif choice == "8":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    hospital = Hospital()
    hospital.run()
