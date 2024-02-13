def resolve(input)-> int:
    counter = 0
    valleys = 0
    valley = False
    for x in input:
        if x == 'U':
            counter = counter + 1
        else:
            counter = counter - 1
            valley = True
            
        if counter == 0 and valley:
            valleys = valleys + 1
            valley = False
    return valleys
def main():
    #Pedir la entrada
    input = "UUUUDDDUDD"
    print(f"Valles: {resolve(input)}")
    return 
main()
