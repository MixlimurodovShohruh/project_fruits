import csv
def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """

    r=csv.reader(f)
    mal=list(r)
    total=0
    for row in mal[1:]:
        total+=float(row[1])
    return total
f=open('fruits.csv')
print(get_total_price(f))

    