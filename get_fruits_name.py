def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    names=[]
    r=data.split()
    for i in r[1:]:
        names.append(i.split(',')[0])

    return names 
data=open('fruits.csv').read()
print(get_frutis_name(data))

    