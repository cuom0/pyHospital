# Hospital Management / Fantasy Hospital

Hospital Management (or Fantasy Hospital) is a Python-based console application designed to simulate a hospital management system. It allows users to manage patient records, illnesses, and admissions seamlessly. 
I would like to point out that the program is created as if it were intended for a real hospital, therefore the program itself is called "Hospital Management", while the project is called "Fantasy Hospital".
The program operates on three files:

- **main.py**: The entry point of the program, which manages the hospital logic and user interaction. (Of course this is the file you must open to make everything work)
- **patient.py**: Contains the `Patient` class that represents patient details and operations.
- **illnesses.py**: Provides predefined illnesses and utilities for illness management.

## Features

- **Patient Management**:
  - Add new patients with details like name, surname, tax code, date of birth, and place of birth.
  - Modify or delete existing patient records.
  - List all patients along with their details (e.g., illnesses, admission and recovery dates).

- **Illness Management**:
  - Assign predefined or custom illnesses to patients.
  - Add or remove illnesses from the system.
  - Automatically set an admission date when assigning an illness (if not already set).

- **Patient Recovery**:
  - Mark a patient as discharged and set their recovery date.

## Requirements

### System Requirements
- Python 3.10 or newer installed.
- Basic familiarity with the command line or terminal.

### Python Modules Used
This program uses only standard Python libraries, so no external dependencies are required:
- `datetime`: For handling dates (e.g., birth date, admission date, recovery date).
- `json`: For reading and writing patient and illness data to JSON files.

## Installation and Setup

1. **Clone or Download the Repository**:
   Download the repository or clone it using the command:
   ```bash
   git clone https://github.com/cuom0_/FantasyHospital.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd FantasyHospital
   ```

3. **Create and Activate a Virtual Environment (Optional)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   .\venv\Scripts\activate  # Windows
   ```

4. **Run the Program**:
   Execute the `main.py` file:
   ```bash
   python main.py
   ```

## How to Use

1. **Start the Program**:
   After running the program, you will see a menu of options:
   ```
   ========== Hospital Management ==========
   1. Add a new patient
   2. Modify a patient
   3. Delete a patient
   4. Assign an illness to a patient
   5. Discharge a patient
   6. List all patients
   7. Manage illnesses
   8. Exit
   ```

2. **Select an Option**:
   Enter the corresponding number for the desired action (e.g., `1` to add a new patient).

3. **Follow Prompts**:
   For each option, the program will guide you through inputting the required information.

## Data Storage

- **Patients**:
  Stored in `patients.json`, containing all patient details including illnesses, admission, and recovery dates.

- **Illnesses**:
  Stored in `illnesses.json`, containing a list of predefined and user-added illnesses.

## Example Workflow

1. **Add a Patient**:
   Enter patient details like name, tax code, etc.

2. **Assign an Illness**:
   Assign a predefined or custom illness to a patient. This also sets the admission date if not already set.

3. **List Patients**:
   View all patient details, including illnesses and dates.

4. **Discharge a Patient**:
   Mark a patient as recovered and set their recovery date.

## Contributing
Feel free to fork the repository and contribute to improving FantasyHospital. Submit a pull request with detailed changes and improvements.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
Developed with ❤️ by [cuom0_](https://github.com/cuom0_) with the amazing help of my Project Group.
Cuomo Salvatore 4E 2024-2025
