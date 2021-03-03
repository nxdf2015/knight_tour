


def get_input(message ,errors_message,**size):
    while True:
        try:

            col,row = map(int,list(input(message).split(" ")))
            if (len(size) == 0 and col > 0 and row >0):
                return (col,row)
            elif (len(size) == 2 and 0< row <= size["rows"] and 0 <col <= size["cols"]):
                return (col,row)
            else:
                raise ValueError()

        except ValueError as e:
            print(errors_message, end=" ")

def contains(item, values):
   return  any(map(lambda value :  item == value[:-1], values))
