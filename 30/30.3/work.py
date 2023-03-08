from typing import List



users: List[str] = ['user1', 'user2', 'user30', 'user3', 'user22', 'user100']

sorted_users = sorted(users, key=lambda elem: int(elem[4:]))
print(sorted_users)

x = lambda a: a + 10
print(x(5))