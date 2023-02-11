def help_message():
    return """/help - displays this help message
            /o, /open (opens link in new tab)
                - maps (opens google maps in new tab)
                - directions ADDRESS(REQUIRES HOME TO BE SET)
                - q (quercus)
                - gpt (link to chat.openai.com)
                - bank (link to td bank)
                - yt (link to youtube)
                - drive (link to google drive)
                - docs  (link to google docs)
                - sheets (link to google sheets)
                - cal (link to google calendar)
            """

def open_link_message(link):
    return f"Opening link: {link}"
