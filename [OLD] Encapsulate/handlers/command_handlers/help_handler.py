from ..helpers import markdown_to_string

def route_help(**kwargs):
    help_routes = {
        "open": ["o", "open", "O"],
        "clear": ["c", "clear", "C"],
    }
    command = kwargs["command"]
    if len(command.split(" "))>1:
        secondarg = command.split(" ")[1]
        for key in help_routes:
            if secondarg in help_routes[key]:
                return markdown_to_string(f"handlers/messages/help_messages/help_{key}_message.md")
        else:
            return markdown_to_string(f"handlers/messages/help_messages/help_{key}_message.md")
    else:
        return markdown_to_string(f"handlers/messages/help_messages/help_message.md")


