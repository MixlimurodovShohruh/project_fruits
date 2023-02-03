def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    rows=data.split()
    name=''
    price=0
    for row in rows[1:]:
        fruit=row.split(',')
        if price<float(fruit[-1]):
            price=float(fruit[-1])
            name=fruit[0]
    return name
f=open('fruits.csv').read()
print(get_expensive_fruit(f))
