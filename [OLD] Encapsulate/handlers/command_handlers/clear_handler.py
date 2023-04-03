
def route_clear(**kwargs):
    cells = kwargs.get("cells")
    command = kwargs.get("command")

    if len(command.split(" ")) > 1:
        if command.split(" ")[1] in ["f", "first", "F"]:
            cell_delete_first(cells)
        elif command.split(" ")[1] in ["l", "last", "L"]:
            cell_delete_last(cells)
        else:
            clear_display(cells)
    else:
        clear_display(cells)
    return ""

def cell_delete_first(cells):
    cells.controls = cells.controls[1:]

def cell_delete_last(cells):
    cells.controls = cells.controls[:-1]

def clear_display(cells):
    cells.controls = []