def calculate_structure_sum(data):
    total_summ=0
    if isinstance(data,(int, float)):
        return data
    elif isinstance(data, str):
        return  len(data)
    elif isinstance(data, (list, set, tuple)):
        for item in data:
            total_summ+= calculate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            total_summ+= calculate_structure_sum(key)
            total_summ+= calculate_structure_sum(value)
    return total_summ

if __name__== '__main__':
    data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
        ]
    result = calculate_structure_sum(data_structure)
    print (result)