# import json
 
# # Convert Python dict to JSON string

# x = {"name": "ksh", "age": "23"}

# x_json = json.dumps(x)  # serialize Python dict to JSON string
 
# # Convert JSON string back to Python dict

# z = json.loads(x_json)
 
# print(z["name"])

# print(z["age"])
 
# """

# x = {"name": "pravalika", "age": 22}

# y = json.dumps(x)

# print(y)

# """

import json
 
# Convert Python dict to JSON string
x = {"name": "ksh", "age": "24"}
x_json = json.dumps(x)  # serialize Python dict to JSON string
 
# Convert JSON string back to Python dict
z = json.loads(x_json)
 
print(z["name"])
print(z["age"])
 
"""
x = {"name": "pravalika", "age": 22}
y = json.dumps(x)
print(y)
"""