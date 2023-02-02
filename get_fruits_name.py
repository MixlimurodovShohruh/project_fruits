import csv
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    fruits=[]
    data=open('fruits.csv')
    reader=csv.reader(data)
    for i in reader:
       fruits.append(i[:1])
    return fruits[1:]


print(get_frutis_name('data'))

    