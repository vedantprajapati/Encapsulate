import flet as ft
from colors import colors


class Cell(ft.UserControl):
    def __init__(self, value, cell_status_change, cell_delete):
        super().__init__()
        self.value = value
        self.cell_status_change = cell_status_change
        self.cell_delete = cell_delete

    def build(self):
        self.display_cell = ft.Container(
            content=ft.Markdown(
                value=self.value,
                selectable=False,       
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                code_theme="atom-one-dark",
                code_style=ft.TextStyle(font_family="Roboto Mono"),
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

    def save_clicked(self, e):
        self.display_cell.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.cell_status_change(self)

    def delete_clicked(self, e):
        self.cell_delete(self)
