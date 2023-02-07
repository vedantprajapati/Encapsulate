import flet as ft
from Colors import colors


class Cell(ft.UserControl):
    def __init__(self, command_name, cell_status_change, cell_delete):
        super().__init__()
        self.command_name = command_name
        self.cell_status_change = cell_status_change
        self.cell_delete = cell_delete

    def build(self):
        self.display_cell = ft.Container(
            content=ft.Text(
                value=self.command_name,
                color=colors["BROWN"],
            ),
            alignment=ft.alignment.center,
            border_radius=0,
        )

        self.display_view = ft.Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_cell,
            ],
        )
        self.divider = ft.Divider(height=1, thickness=1, color=colors["BEIGE2"])
        return ft.Column(controls=[self.display_view, self.divider])

    def edit_clicked(self, e):
        self.edit_name.value = self.display_cell.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_cell.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.cell_status_change(self)

    def delete_clicked(self, e):
        self.cell_delete(self)
