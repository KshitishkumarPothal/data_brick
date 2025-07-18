# def add_all(*numbers):
#     return sum(numbers)
# print(add_all(1,2,3,4,5))

# def info(**details):
#     for key in details:
#         print(key, ":", details[key])
# info(name="kshitish", age="23", city="baripada")

def sub_with_mark(**marks):
    for sub in marks:
        print(sub, ":", marks[sub])
def total_mark(*mark):
    return sum(mark)
sub_with_mark(math= 23,science=24,it=25,phy=24,che=19)
print(f"Total marks: {total_mark(23,24,25,24,19)}")
