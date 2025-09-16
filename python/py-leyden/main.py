from utils import mdown_parser, rst_parser

def markdown_to_html(markdown_text : str) -> str:
    html_text : str = mdown_parser.parse_text(markdown_text)
    return html_text

def rst_to_html(rst_text : str) -> str:
    html_text : str = rst_parser.parse_text(rst_text)
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
