def markdown_to_html(markdown_text : str) -> str:
    html_text : str = ""
    return html_text

def html_prettify(text : str) -> str:
    '''Use HTML codes for certain characters.'''
    html_code_dict = {
        " -- " : "&#8202;&mdash;&#8202;",
        "à": "&agrave;",
        "ï": "&iuml;",
        "ø": "&oslash;",
        "æ": "&aelig;"
    }
    return text.translate(str.maketrans(html_code_dict))

def main():
    print("Hello from py-leyden!")


if __name__ == "__main__":
    main()
