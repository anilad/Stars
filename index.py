def draw_stars(arr):
    for element in arr:
        if isinstance(element, int):
            print "*"*element
        elif isinstance(element, str):
            print element[0].lower()*len(element)

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(y)