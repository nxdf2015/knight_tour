

def validation(exception, message):
    def validate(f):
        def wrapper(*args):
            try:
                return f(*args)
            except ValueError as e:
                print(message)
                return False
        return wrapper
    return validate

@validation(ValueError, "Invalid position!")
def get_input(message):
        print(message)
        values =  tuple(  map(int,input().split(" ")))
        if len(values) == 2:
            return values
        else:
            raise ValueError()



def in_range(limit=8):
    def valid(x):
        return 1 <= x <= 8
    return valid
