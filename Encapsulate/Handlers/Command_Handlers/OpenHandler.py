from ..HandleMessageError import error_open_link_not_found
from ..HandleMessage import open_link_message

saved_links = {
    "maps": "https://www.google.com/maps",
    "q": "https://q.utoronto.ca",
    "gpt": "https://chat.openai.com",
    "bank": "https://www.td.com/ca/en/personal-banking/",
    "yt": "https://www.youtube.com",
    "drive": "https://drive.google.com",
    "docs": "https://docs.google.com",
    "sheets": "https://sheets.google.com",
    "cal": "https://calendar.google.com",
    "s": "https://www.spotify.com/ca-en/",
}


def route_open(**kwargs):
    command = kwargs.get("kwargs").get("command")

    if len(command.split(" ")) > 1 and command.split(" ")[1] in saved_links:
        link = saved_links[command.split(" ")[1]]
        kwargs.get("kwargs").get("page").launch_url(url=link)
        return open_link_message(link)
    else:
        return error_open_link_not_found()



