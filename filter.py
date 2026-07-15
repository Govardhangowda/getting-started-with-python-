cities = ["Bengaluru", "Mysuru", "Mandya", "Hubballi", "Ballari", "Hassan"]
mcity=filter(lambda x: x.startswith("M"), cities)
print(list(mcity))