def bread(func):
    def wrapped_func():
        print('</------\>')
        func()
    return wrapped_func
def tomatoes(func):
    def wrapped_func():
        print('#помидоры#')
        func()
    return wrapped_func
def beacon(func):
    def wrapped_func():
        print('--ветчина--')
        func()
    return wrapped_func

def salad(func):
    def wrapped_func():
        print('~~салат~~')
        func()
    return wrapped_func








@bread
@tomatoes
@beacon
@salad
def sanswich():
    print('\________/')

sanswich()
