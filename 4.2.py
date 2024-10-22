def create_dictionary(ilist):
    idict = {}
    for item in ilist:
        if item in idict:
            idict[item] += 1
        else:
            idict[item] = 1
        
    return idict

ilist = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
result = create_dictionary(ilist)
print(result)
