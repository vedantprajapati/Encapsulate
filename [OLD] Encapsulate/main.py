import flet as ft
from colors import colors
from EncapsulateApp import EncapsulateApp
from setup import setup_encapsulate
from oauth.google_oauth import get_google_oauth, save_user, google_get_user, has_token
import os

def main(page: ft.Page):
    def google_login_click(e):
        if provider == "github":
            page.login(google_provider)
        page.login(google_provider)

    def on_login(e):
        print("User logged in: " + page.auth.user.get("email"))
        save_user(page)
        if page.client_storage.get("g_name") is not None and welcome_user.value == "":
            welcome_user.value = "Welcome, " + page.auth.user.get('name')
        google_oauth_button.visible = False
        welcome_user.visible = True
        page.update()

    welcome_user, google_oauth_button, google_provider = get_google_oauth(
        page, google_login_click
    )

    provider = {
        "google": google_provider,
    }
    page.on_login = on_login

    if google_get_user(page)["g_name"] is not None and has_token(page):
        welcome_user.value = "Welcome, " + page.auth.user.get('name')
        google_oauth_button.visible = False
        welcome_user.visible = True
        
    login_bar = ft.Row(controls=[welcome_user, google_oauth_button])

    page.add(login_bar)

    setup_encapsulate(page)
    app = EncapsulateApp()
    page.add(app)


ft.app(target=main, assets_dir="assets")
