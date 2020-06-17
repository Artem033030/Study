def task_1_fix_names_start_letter(data):
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    return data.capitalize()
#     for x in data:
#         x['name'] = x['name'].capitalize()
#
#
# data = [{'name': 'alex', 'age': 26}, {'name': 'denys', 'age': 89}, {'name': 'indus','age': 17}]
# task_1_fix_names_start_letter(data)
# print(data)
