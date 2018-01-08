"""Input cipher key string, get user input on route direction as dict value."""
col_order = """1 3 4 2"""
key = dict()
cols = [int(i) for i in col_order.split()]
for col in cols:
    route = input("Direction to read Column {} (u = up, d = down): "
                  .format(col).lower())
    while route != 'u' and route != 'd':
        print("Input should be 'u' or 'd'")
        route = input("Direction to read Column {} (u = up, d = down): "
                      .format(col).lower())
    key[col] = route
print(key)
