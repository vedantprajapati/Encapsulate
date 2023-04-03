import flet as ft
from colors import colors
from handlers import HandleRequest as hr
from Cell import Cell

Handler = hr.HandleRequest()


class EncapsulateApp(ft.UserControl):
    def build(self):
        self.CLI = ft.TextField(
            label="CMD",
            label_style=ft.TextStyle(color=colors["SLATE"]),
            hint_style=ft.TextStyle(color=ft.colors.BLACK),
            hint_text="Enter a Command",
            helper_text="type /help for a list of commands",
            helper_style=ft.TextStyle(color=colors["BROWN"]),
            border_color=colors["SLATE"],
            text_style=ft.TextStyle(color=colors["BROWN"]),
            prefix_text="ε /",
            prefix_style=ft.TextStyle(color=colors["RED_ORANGE"]),
            cursor_color=colors["SLATE"],
            on_submit=self.call_command,
            expand=True,
            autofocus=True,
        )

        self.output_stack = ft.Column()

        return ft.Column(
            controls=[
                ft.Divider(height=1, thickness=0, color=colors["BEIGE"]),
                ft.Row(
                    controls=[
                        self.CLI,
                    ],
                ),
                ft.Divider(height=1, thickness=1, color=colors["BROWN"]),
                ft.Column(
                    spacing=25,
                    controls=[
                        # self.filter,
                        self.output_stack,
                        ft.Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[],
                        ),
                    ],
                ),
            ],
        )

    def call_command(self, e):
        if self.CLI.value:
            cell_output_value = Handler.route_command(
                command=self.CLI.value,
                page=self._Control__page,
                cells=self.output_stack,
            )
            if self.CLI.value.split(" ")[0] not in ["c", "clear", "C"]:
                cell = Cell(
                    cell_output_value, self.cell_status_change, self.cell_delete
                )
                self.output_stack.controls.insert(0, cell)
            self.CLI.value = ""
            self.CLI.focus()
            self.update()

    def cell_status_change(self, task):
        self.update()

    def cell_delete(self, task):
        self.output_stack.controls.remove(task)
        self.update()

    def clear_display(self, e):
        for cell in self.output_stack.controls[:]:
            self.cell_delete(cell)

    def update(self):
        super().update()
