def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    rows=data.split()[1:]
    id=0
    price = float(rows[0].split(',')[1])
    i=1
    while i<len(rows):
        if price>float(rows[i].split(',')[1]):
            price=float(rows[i].split(',')[1])
            id=i+1
        i+=1
    return id
data=open('fruits.csv').read()
print(get_cheapest_fruit_id(data)) 