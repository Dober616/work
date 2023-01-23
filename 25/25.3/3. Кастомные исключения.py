class MyError(Exception):
    pass


with open('number.txt', 'r') as number:
    for line in number:
        try:
            clear_line = line.rstrip()
            first, secnd = clear_line.split(' ')
            if int(first) < int(secnd):
                raise MyError('Меньшее на большее делить нельзя')
        except (ValueError, MyError) as exc:
            print(exc, type(exc), first, secnd)


