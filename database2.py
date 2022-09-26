# def create_patient_entry(patient_name, patient_id, patient_age): 
#     new_patient = [patient_name, patient_id, patient_age, []]
#     return new_patient 

def create_patient_dictionary(patient_first_name, patient_last_name, patient_Id, patient_Age):
    new_patient= {"First Name": patient_first_name,
                      "Last Name": patient_last_name,
                      "Id": patient_Id, 
                      "Age": patient_Age,
                      "Tests": []}
    return new_patient


def main(): 
    db = []
    db.append(create_patient_dictionary("Ann", "Ables", 1, 30))
    db.append(create_patient_dictionary("Bob", "Boyles", 2, 34))
    db.append(create_patient_dictionary("Chris", "Chou", 3, 25))
    print_database(db)
    add_test_to_patient(db, 3, "HDL", 100)
    print_database(db) 
    print("Patient {} is a {}".format(get_full_name(db[2]),
                                      adult_or_minor(db[2])))

def print_database(db):
    for patient in db:
        print("Name: {}, id: {}, age: {}".format(get_full_name(patient), 
                                                 patient["Id"], 
                                                 patient["Age"]))


def get_full_name(patient):
    full_name = "{} {}".format(patient["First Name"], patient["Last Name"])
    return full_name 


def find_patient(db, id_no):
    for patient in db: 
        if patient["Id"] == id_no:
            return patient 
    return False 


def add_test_to_patient(db, id_no, test_name, test_value): 
    patient = find_patient(db, id_no)
    patient["Tests"].append((test_name, test_value))


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else: 
        return "minor"
# def patient_lookup(db, patient_id):
#     for patient in db: 
#         if patient[1] == patient_id:
#             return patient
#         return False
        
# def add_patient_test(db, patient_id, test_name, test_value):
#     patient = patient_lookup(db, patient_id)
#     patient[3].append(test_name, test_value)

if __name__ == "__main__":
    main()

