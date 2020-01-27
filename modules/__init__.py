import os
import importlib

menu_ptr = []
run_ptr = []

def sort_menu_by_priority():
    global menu_ptr
    menu_ptr = sorted(menu_ptr, key=lambda k: k['priority'])

for module in os.listdir('modules'):
    if os.path.isdir(os.path.join("modules", module)):
        imported_module = __import__("modules" + "." + module, fromlist=[module])
        if hasattr(imported_module, "get_menu"):
            menu_ptr.append(imported_module.get_menu())
        if hasattr(imported_module, "run_module"):
            run_ptr.append({"run_module":imported_module.run_module, "name": module})

sort_menu_by_priority()