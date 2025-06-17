DEFAULT_TIMEOUT = 10

POSSIBLE_ERRORS = [
    "404",
    "500",
    "error",
    "Error",
    "ERROR",
    "error"
]

DATE_FORMAT = "%Y-%m-%d_%H-%M-%S"


LOGIN ={
"CREDENTIALS":{
    "valid": {
        "email": "test@lumen.me",
        "password": "qwerty"
    },
    "invalid": {
        "email": "wrong@lumen.me",
        "password": "wrongpass"
    }
},
"ERROR_MSG":"Please fill in all fields"
}
WELCOME_MSG = "Welcome test@lumen.me"

REACH_COUNTER_CASES = [
    {
        "target_value": 3,
        "button_names": ["home"],
    },
    {
        "target_value": 6,
        "button_names": ["home", "messages"],
    },
    {
        "target_value": 9,
        "button_names": ["home", "messages", "profile"],
    },
]