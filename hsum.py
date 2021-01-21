import sys

def hSum(num_terms):
    num_list = []
    i = 0
    sum = 0
    for i in range(num_terms):
        i += 1
        sum = sum + 1/i
        num_list.append(sum)
    return num_list
        

def main():
    inp = input()
    inp = int(inp)
    val_list = hSum(inp)
    i = 0
    for val in val_list:
        print(i, " ", val)
        i += 1

main()