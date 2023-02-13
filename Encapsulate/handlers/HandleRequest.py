import handlers.HandleMessageError as hme
from handlers.command_handlers import open_handler, help_handler, clear_handler, exit_handler, profile_handler  
class HandleRequest:
    def __init__(self):
        self.commands = {
            ("help", "h", "H"): help_handler.route_help,
            ("o", "open", "O"): open_handler.route_open,
            ("C", "c", "clear"): clear_handler.route_clear,
            ("exit",): exit_handler.route_exit,
            ("profile", "p", "P"): profile_handler.route_profile,
        }

    def route_command(self, **kwargs):
        command = kwargs.get("command")
        main_command = command.split(" ")[0]
        route = next((self.commands[key] for key in self.commands if main_command in key), None)
        if not route and command is not None:
            return hme.error_command_not_found()
        elif route:
            return route(**kwargs)
        else:
            return ""
