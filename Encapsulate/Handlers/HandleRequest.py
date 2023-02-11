import Handlers.HandleMessage as hm
import Handlers.HandleMessageError as hme
from Handlers.Command_Handlers import OpenHandler, HelpHandler, ClearHandler, ExitHandler, OpenHandler
class HandleRequest:
    def __init__(self):
        self.main_commands = {
            "help": HelpHandler.route_help,
            "h": HelpHandler.route_help,
            "H": HelpHandler.route_help,
            "o": OpenHandler.route_open,
            "open": OpenHandler.route_open,
            "O": OpenHandler.route_open,
            "C": ClearHandler.route_clear,
            "c": ClearHandler.route_clear,
            "clear": ClearHandler.route_clear,
            "exit": ExitHandler.route_exit,
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

