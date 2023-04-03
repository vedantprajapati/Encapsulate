import flet as ft
from flet.auth.providers.google_oauth_provider import GoogleOAuthProvider
import os
from dotenv import load_dotenv

load_dotenv()


def google_get_user(page):
    if (
        page.client_storage.get("email") is None
        or page.client_storage.get("username") is None
        # or page.client_storage.get("id") is None
    ):
        if hasattr(page,"auth") and hasattr(page.auth,"user") and page.auth.user is not None:
            save_user(page.auth.user)

    return {
        "g_email": page.client_storage.get("g_email"),
        "g_name": page.client_storage.get("g_name"),
        # "g_id": page.client_storage.get("id"),
        "token": page.client_storage.get("token"),
        "provider": "google",
    }


def has_token(page):
    if hasattr(page.auth,"token") and page.auth.token is not None:
        return page.client_storage.get("token") is not None

def save_user(page):
    page.client_storage.set("g_email", page.auth.user.get("email"))
    page.client_storage.set("g_name", page.auth.user.get("name"))
    try:
        page.client_storage.set("token", page.auth.token.access_token)
    except:
        print("No token found")

def get_google_oauth(page, google_login_click, get_user=google_get_user):
    welcome_user = ft.Text(value="", visible=False)
    google_oauth_button = ft.ElevatedButton(
        "Login with Google", on_click=google_login_click
    )

    google_provider = GoogleOAuthProvider(
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        redirect_url="http://localhost:8560/api/oauth/redirect",
    )
    # google_provider.user_scopes = google_provider.user_scopes + ["https://www.googleapis.com/auth/calendar.events.readonly"]

    return welcome_user, google_oauth_button, google_provider
