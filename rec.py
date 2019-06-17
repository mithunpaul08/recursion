
input="india is my country all indians"
input_split=input.split(" ")
n=[]

def attach_strings(index):
    if (index+1 >= len(input_split)):
        return input_split[index]
    else:
        output=input_split[index]+" "+(attach_strings(index + 1))
    return output


def attach_strings_external_ds(index):
    if (index+1 >= len(input_split)):
        return input_split[index]
    else:
        output=(attach_strings_external_ds(index + 1))
        n.append(output)
    return input_split[index]

def add_numbers_upto(num):
    if num==0:
        return num
    else:
        sum=num+add_numbers_upto(num-1)
    return sum

def print_upto(num):
    if num<=1:
        return num
    else:
        sum= print_upto(num-1)
        print(sum)
    return sum

if __name__ == '__main__':
    output = attach_strings(0)
    print(output)