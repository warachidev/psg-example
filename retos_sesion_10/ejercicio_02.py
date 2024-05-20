# %%
menu_mexicano = {"Tacos", "Enchiladas", "Guacamole", "Tamales"}
menu_italiano = {"Pizza", "Pasta", "Lasagna", "Tiramisú"}
menu_fusion = menu_mexicano | menu_italiano
print(menu_mexicano, menu_italiano)
print(menu_fusion)