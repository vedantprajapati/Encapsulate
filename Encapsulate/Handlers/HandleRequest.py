import Handlers.HandleMessage as hm
import Handlers.HandleMessageError as hme
from Handlers.Command_Handlers.ClearHandler import route_clear

class HandleRequest:
    def __init__(self):
        self.main_commands = {
            "help": self.route_help,
            "h": self.route_help,
            "H": self.route_help,
            "o": self.route_open,
            "open": self.route_open,
            "O": self.route_open,
            "C": route_clear,
            "c": route_clear,
            "clear": route_clear,
            "exit": self.route_exit,
        }

        self.saved_links = {
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

    def route_command(self, **kwargs):
        command = kwargs.get("command")
        main_command = command.split(" ")[0]

        if not main_command:
            return ""
        elif main_command in self.main_commands:
            return self.main_commands[main_command](kwargs=kwargs)
        else:
            return hme.error_command_not_found()

    def route_help(self, **kwargs):
        # TODO insert help logic here or in a different function
        return hm.help_message()

    def route_open(self, **kwargs):
        command = kwargs.get("kwargs").get("command")

        if len(command.split(" ")) > 1 and command.split(" ")[1] in self.saved_links:
            link = self.saved_links[command.split(" ")[1]]
            kwargs.get("kwargs").get("page").launch_url(url=link)
            return hm.open_link_message(link)
        else:
            return hme.error_open_link_not_found()



    #Close the page
    def route_exit(self, **kwargs):
        page = kwargs.get("kwargs").get("page")
        if page:
            page.window_prevent_close=False
            page.window_destroy()
        return ""
