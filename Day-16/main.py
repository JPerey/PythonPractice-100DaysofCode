# import turtle
# import another_module

# print(another_module.another_mod)

# timmy = turtle.Turtle()
# timmy.color("chartreuse")
# timmy.forward(10)

# my_screen = turtle.Screen()
# timmy.forward(150)

# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

very_pretty_t = prettytable.PrettyTable()

very_pretty_t.field_names = ["Name", "age", "hobby"]
very_pretty_t.add_row(["Jam", 34, "Guitar"])
very_pretty_t.add_row(["Rachel", 34, "Videography"])

print(very_pretty_t)

table = prettytable.PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)