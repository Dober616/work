family_member = {
    'name': 'Jane',
    'surname': 'Doe',
    'hobbies': ['running', 'sky diving', 'singing'],
    'age': 35,
    'children': [
        {
            'name': 'Alice',
            'age': 6,
        },
        {
            'name': 'Bob',
            'age': 8
        }
    ]
}

print(family_member)
some_name = input('Введите какое-нибудь имя: ')
result = [
    family_member.get('name', {})
    for family_member['name'] in family_member.values()
    if some_name in family_member.values()
]
print(result)
