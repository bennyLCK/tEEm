# A stub for databases using dictionaries. Patient names are used as primary keys, though this may not be feasible in the real world.

patients_personal_info = {
    "John" : "8650 9987, 123 Lorong 1 Toa Payoh 02-515, 01-01-1990",
    "Alice" : "9876 1234, BLK 185 TOA PAYOH CENTRAL 01-318, 12-12-1995",
    "Benny" : "9671 2765, Blk 13, Haig Rd #01-01, 14-05-2001",
    "Charles" : "9912 3768, 1092 LOWER DELTA ROAD 03-14, 03-04-1995",
    "Dennis" : "6333 1461, 310a Anchorvale Road, 13-31, 13-12-1993",
    "Eugene" : "9555 2368, 19 Tanglin Road #02-11 Tanglin Shopping Centre, 04-04-2004"
}

patients_health_info = {
    "John" : "Allergies : None, Pre-existing conditions : None, Current medications : None",
    "Alice" : "Allergies : Nuts, Pre-existing conditions : Diabetes, Current medications : Insulin",
    "Benny" : "Allergies : Animal fur, Pre-existing conditions : Hypertension, Current medications : Inhibitors",
    "Charles" : "Allergies : Shellfish, Pre-existing conditions : None, Current medications : None",
    "Dennis" : "Allergies : Milk, Pre-existing conditions : Diabetes, Current medications : Insulin",
    "Eugene" : "Allergies : Pollen, Pre-existing conditions : Asthma, Current medications : None"
}

def get_personal_info (name):
    return patients_personal_info.get(name)

def get_health_info (name):
    return patients_health_info.get(name)

