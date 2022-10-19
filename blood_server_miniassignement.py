import requests

#get IDS for two patients
request_ID = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/nxs")
request_ID = request_ID.json()

#saves ID
donor_ID = request_ID['Donor']
patient_ID = request_ID['Recipient']

# gets blood type 
request_donor_type = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/" + donor_ID)
donor_type = request_donor_type.text

request_patient_type = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/" + patient_ID)
patient_type = request_patient_type.text

#determines if patient is a match
def blood_matching(donor_type, patient_type):
    a_plus = [ "A+", "A-", "O+", "O-"]
    a_minus = ["A-", "O-"]
    b_plus = ["B+", "B-",  "O+", "O-"]
    b_minus  = ["B-", "O-"]
    ab_plus = ["A+", "A-", "B+", "B-", "AB+", "AB-",  "O+", "O-"]
    ab_minus = ["A-", "B-", "AB-",  "O-"]
    O_plus = ["O+", "O-"]
    O_minus = ["O-"]
    if patient_type == "A+" and donor_type in a_plus:
        return "Yes"
    elif patient_type == "A-" and donor_type in a_minus:
        return "Yes"
    elif patient_type == "B+" and donor_type in b_plus:
        return "Yes" 
    elif patient_type == "B-" and donor_type in b_minus:
        return "Yes"
    elif patient_type == "AB+" and donor_type in ab_plus:
        return "Yes" 
    elif patient_type == "AB-" and donor_type in ab_minus:
        return "Yes"
    elif patient_type == "O+" and donor_type in O_plus:
        return "Yes"
    elif patient_type == "O-" and donor_type in O_minus:
        return "Yes"
    else: 
        return "No"

result = blood_matching(donor_type, patient_type)

#check results
output_info = {"Name": "nxs", "Match": result}
post_match = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json = output_info)
print(post_match.text)