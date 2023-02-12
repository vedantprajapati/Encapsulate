def route_exit(**kwargs):
    page = kwargs.get("kwargs").get("page")
    if page:
        page.window_prevent_close=False
        page.window_destroy()
