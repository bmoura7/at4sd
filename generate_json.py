import json


def create_json():

    expression = {"operacao": "/",
                    "left": {
                        "operacao": "-",
                        "op1": 75.0,
                        "op2": 52.0
                    },
                    "right": {
                        "operacao": "*",
                        "left": {
                            "operacao": "+",
                            "op1": 32.0,
                            "op2": 12.0,
                        },
                        "op2": 3.0
                    }
                }

    
    with open("data_file.json", "w") as write_file:
        json.dump(expression, write_file, indent=4)
    
    json_str = json.dumps(expression, indent=4)
    #print(json_str)
    
    return json_str