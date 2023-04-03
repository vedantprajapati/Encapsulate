def markdown_to_string(file):
    """
    Convert a markdown file to a string.

    :param file: The markdown file to convert.
    :type file: str
    :return: The converted markdown file.
    :rtype: str
    """
    with open(file, 'r') as f:
        md_string = f.read()
    return str(md_string)
      