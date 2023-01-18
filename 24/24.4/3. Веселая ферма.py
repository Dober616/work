from garden import Garden

garden = Garden(5)
for _ in range(3):
    garden.grow_all()
garden.are_all_ripe()