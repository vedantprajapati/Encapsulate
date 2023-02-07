from Colors import colors
import flet as ft

def setup_encapsulate(page):
    page.title = "Encapsulate"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.fonts = {
        "Yorha": "https://metakirby5.github.io/yorha/yorha.ttf",
    }
    page.theme = ft.theme.Theme(font_family="Yorha", color_scheme_seed="#dcd8c0")
    page.bgcolor = colors["BEIGE"]

    page.title = "Encapsulate"
    page.update()
