
import flet as ft
from Colors import colors
from EncapsulateApp import EncapsulateApp
from setup import setup_encapsulate

def main(page: ft.Page):
    setup_encapsulate(page)
    app = EncapsulateApp()
    page.add(app)


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
