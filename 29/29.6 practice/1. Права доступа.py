import functools


def check_permission(func, permission):
    functools.wraps(func)
    def wrapper(*args, **kwargs: str):
        if permission == 'admin':
            result = func(*args, **kwargs)
            return result
        return f'Недостаточно прав для удаления сайта'
    return wrapper




user_permissions = 'admin'
@check_permission(permission='admin')
def delete_site():
    print('Удаляем сайт')

def add_comment():
    print('Оставляем коммент')

delete_site()