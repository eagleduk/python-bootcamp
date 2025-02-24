import colorgram

colors = colorgram.extract("image", -1)

rgbs = []

for i in range(len(colors)):
    c = colors[i].rgb
    rgbs.append((c.r, c.g, c.b))

print(rgbs)
