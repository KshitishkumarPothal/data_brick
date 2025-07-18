# try:
#     n = int(input("Enter a number"))
# except ValueError:
#     print("Enter a number only")


#custom error

class CustomException(Exception):
    pass
class ValidationError(Exception):
    def __init__(self, args,code = None):
        super().__init__(args)
        self.code = code
#using custom exception
def validate_age(age):

    if age < 0:
        raise ValidationError("Age can't be negative")
    if age > 150:
        raise ValidationError("your are not immortal","hey i am here")
try:
    # validate_age(-9)
    validate_age(160)

except ValidationError as e:
    print(f"Validation Failed: {e}")
    print(f"error code : {e.code}")