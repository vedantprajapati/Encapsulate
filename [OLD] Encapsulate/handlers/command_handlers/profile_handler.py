import flet as ft
from oauth.google_oauth import google_get_user
def route_profile(**kwargs):
    try:
        user_dict = google_get_user(kwargs.get("page"))
        return f'Email: {user_dict.get("g_email")} \n Name: {user_dict.get("g_name")} \n Token: {user_dict.get("token") != None}'
    except:
        return "Please login to view your profile"

