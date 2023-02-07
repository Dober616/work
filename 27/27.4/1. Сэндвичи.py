def burger(funk):
    def wrapped_func():
        print('</------\>')
        result = funk()
        print('<\______/>')
        return result
    return wrapped_func


@burger
def ingredients():
    print('#помидоры#')
    print('--ветчина--')
    print('~~салат~~')


ingredients()

