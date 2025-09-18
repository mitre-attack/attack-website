import os

menu_ptr = []
run_ptr = []
pelican_settings = []
master_redirections_dict = {}


def sort_menu_by_priority():
    global menu_ptr
    menu_ptr = sorted(menu_ptr, key=lambda k: k["priority"])


def sort_run_ptr_by_priority():
    global run_ptr
    run_ptr = sorted(run_ptr, key=lambda k: k["priority"])


def check_redirections(redirections_list):
    global master_redirections_dict

    for redirection in redirections_list:
        # If master list already has from redirection
        if master_redirections_dict.get(redirection["from"]):
            # Check if it redirects to the same link, otherwise it is a conflict
            if master_redirections_dict[redirection["from"]] != redirection["to"]:
                print("Redirection conflict!")
                print("\t1. [{} => {}]".format(redirection["from"], redirection["to"]))
                print("\t2. [{} => {}]".format(redirection["from"], master_redirections_dict[redirection["from"]]))
                print("Exiting...")
                exit()
        else:
            master_redirections_dict[redirection["from"]] = redirection["to"]


for module in os.listdir("modules"):
    if os.path.isdir(os.path.join("modules", module)):
        imported_module = __import__("modules" + "." + module, fromlist=[module])
        if hasattr(imported_module, "get_menu"):
            menu_ptr.append(imported_module.get_menu())
        if hasattr(imported_module, "run_module") and hasattr(imported_module, "get_priority"):
            run_ptr.append(
                {
                    "run_module": imported_module.run_module,
                    "module_name": module,
                    "priority": imported_module.get_priority(),
                }
            )
        if hasattr(imported_module, "send_to_pelican"):
            pelican_settings.append({"module_name": imported_module.send_to_pelican()})
        if hasattr(imported_module, "get_redirections"):
            redirections_list = imported_module.get_redirections()
            # Check list for conflicts
            check_redirections(redirections_list)

sort_menu_by_priority()
sort_run_ptr_by_priority()
