import flet as ft
from oauth.google_oauth import google_get_user
def route_profile(**kwargs):
    try:
        user_dict = google_get_user(kwargs.get("page"))
        return f'Email: {user_dict.get("g_email")}, Name: {user_dict.get("g_name")}, token: {user_dict.get("Token") != None}'
    except:
        return "Please login to view your profile"

