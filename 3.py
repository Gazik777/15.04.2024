def format_report_org1(func):
    def wrapper(a):
        print("Ежемесячная прибыль",end=" ")
        result = func(a)
        return result
    return wrapper
def format_report_org2(func):
    def wrapper(b):
        print("Ежемесячный убыток",end=" ")
        result = func(b)
        return result
    return wrapper

@format_report_org1
def generate_report(data):
    formatted_report = data * 2
    return  formatted_report

@format_report_org2
def generate_report1(data):
    formatted_report = data * 4
    return formatted_report


print(generate_report(40))
print(generate_report1(5))




