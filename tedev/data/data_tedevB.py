from datetime import datetime
dt0 = lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.000Z")

# Meta-data & infos of Employee
#
employee_infos = \
    {
        'entities': 'employees',
        'entity': 'employee',
        'Entity': 'Employee',
        'Entities': 'Employees'
    }

employee_fields = [
            "id",
            "firstname",
            "lastname",
            "city",
            "state",
            "phone",
            "email",
            "address",
            "entreprise"
        ]

# --------------------------------------------------------------------------------------------#
# Data
# --------------------------------------------------------------------------------------------#
#01
employee01 = {
    "id": 1,
    "firstname": "EAli",
    "lastname": "EFolk",  # ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
    "address": "1015 Folsom Street",
    "city": "San Francisco",
    "state": "CA",
    "phone": "123-123-1234",
    "email": "ali@g.com",
    "entreprise": "facebook"
}

#02
employee02 = {
    "id": 2,
    "firstname": "EDueling",
    "lastname": "EPianos",  # ["Classical", "R&B", "Hip-Hop"],
    "address": "335 Delancey Street",
    "city": "New York",
    "state": "NY",
    "phone": "914-003-1132",
    "email": "https@pianos.com",
    "entreprise": "thedueling",
}

#03
employee03 = {
    "id": 3,
    "firstname": "EPark",
    "lastname": "ESquare",  # ["Rock n Roll", "Jazz", "Classical", "Folk"],
    "address": "34 Whiskey Moore Ave",
    "city": "San Francisco",
    "state": "CA",
    "phone": "415-000-1234",
    "email": "parksquarelive@musicandcoffee.com",
    "entreprise": "ParkSquare@Live.ca",
}

employees00 = [ employee01, employee02, employee03 ]

# --------------------------------------------------------------------------------------------#
# Meta-data & infos of Participant
#
participant_infos = \
    {
        'entities': 'participants',
        'entity': 'participant',
        'Entity': 'Participant',
        'Entities': 'Participants'
    }

participant_fields = [
            "id",
            "firstname",
            "lastname",
            "city",
            "state",
            "phone",
            "email",
            "address",
            "entreprise"
        ]

# --------------------------------------------------------------------------------------------#
# Data
# --------------------------------------------------------------------------------------------#
#01
participant01 = {
    "id": 1,
    "firstname": "Ali",
    "lastname": "Folk",  # ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
    "address": "1015 Folsom Street",
    "city": "San Francisco",
    "state": "CA",
    "phone": "123-123-1234",
    "email": "ali@g.com",
    "entreprise": "facebook"
}

#02
participant02 = {
    "id": 2,
    "firstname": "Dueling",
    "lastname": "Pianos",  # ["Classical", "R&B", "Hip-Hop"],
    "address": "335 Delancey Street",
    "city": "New York",
    "state": "NY",
    "phone": "914-003-1132",
    "email": "https@pianos.com",
    "entreprise": "thedueling",
}

#03
participant03 = {
    "id": 3,
    "firstname": "Park",
    "lastname": "Square",  # ["Rock n Roll", "Jazz", "Classical", "Folk"],
    "address": "34 Whiskey Moore Ave",
    "city": "San Francisco",
    "state": "CA",
    "phone": "415-000-1234",
    "email": "parksquarelive@musicandcoffee.com",
    "entreprise": "ParkSquare@Live.ca",
}

participants00 = [ participant01, participant02, participant03 ]

# --------------------------------------------------------------------------------------------#


#
tedevB_model01 = \
    {
        'participant': participants00 ,
        'employee': employees00 ,
    }

#
entities_infos = \
    {
        'participant': participant_infos ,
        'employee': employee_infos ,
    }

#
tedevB_entity_fields = {
    'participant': participant_fields,   #
    'employee': employee_fields,  #
}
