from collections import OrderedDict

# Only ordered based on mana satu kita key-in dulu
ordered = OrderedDict()
ordered['a'] = 145
ordered['z'] = 324
ordered["x"] = 1

print(ordered)

ordered.move_to_end("a")  # gerak ke kedudukan terakhir

print(ordered)

ordered.move_to_end("x", last=False)  # gerak ke kedudukan pertama

print(ordered)

ordered.popitem()

print(ordered)
