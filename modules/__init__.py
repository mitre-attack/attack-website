import os
import importlib

menu_ptr = []
run_ptr = []

for module in os.listdir('modules'):
    if os.path.isdir(os.path.join("modules", module)):
        imported_module = __import__("modules" + "." + module, fromlist=[module])
        if hasattr(imported_module, "get_menu"):
            menu_ptr.append(imported_module.get_menu())
        if hasattr(imported_module, "run_module"):
            run_ptr.append(imported_module.run_module)