# Base: https://github.com/magmax/python-inquirer/tree/main/examples

from InquirerPy                 import inquirer, get_style
from InquirerPy.base.control    import Choice
from InquirerPy.separator       import Separator
from InquirerPy.utils           import InquirerPyStyle


class Style():
    """ Simplifies `InqueirerPY's` styling system """
    
    # Notas:
    '"questionmark": "fg:#e5c07b bg:#ffffff underline bold"'
    # https://inquirerpy.readthedocs.io/en/latest/pages/style.html

    def __init__(self) -> None:
        """ Instantiate the variables """
        self.questionmark       = "#e5c07b"
        self.answermark         = "#e5c07b"
        self.answer             = "#61afef"
        self.input              = "#98c379"
        self.question           = ""
        self.answered_question  = ""
        self.instruction        = "#abb2bf"
        self.long_instruction   = "#abb2bf"
        self.pointer            = "#61afef"
        self.checkbox           = "#98c379"
        self.separator          = ""
        self.skipped            = "#5c6370"
        self.validator          = ""
        self.marker             = "#e5c07b"
        self.fuzzy_prompt       = "#c678dd"
        self.fuzzy_info         = "#abb2bf"
        self.fuzzy_border       = "#4b5263"
        self.fuzzy_match        = "#c678dd"
        self.spinner_pattern    = "#e5c07b"
        self.spinner_text       = ""

    def __call__(self) -> InquirerPyStyle:
        """ Returns the style according to the object variables """

        style = {
            "questionmark"      : self.question             ,
            "answermark"        : self.answermark           ,
            "answer"            : self.answer               ,
            "input"             : self.input                ,
            "question"          : self.question             ,
            "answered_question" : self.answered_question    ,
            "instruction"       : self.instruction          ,
            "long_instruction"  : self.long_instruction     ,
            "pointer"           : self.pointer              ,
            "checkbox"          : self.checkbox             ,
            "separator"         : self.separator            ,
            "skipped"           : self.skipped              ,
            "validator"         : self.validator            ,
            "marker"            : self.marker               ,
            "fuzzy_prompt"      : self.fuzzy_prompt         ,
            "fuzzy_info"        : self.fuzzy_info           ,
            "fuzzy_border"      : self.fuzzy_border         ,
            "fuzzy_match"       : self.fuzzy_match          ,
            "spinner_pattern"   : self.spinner_pattern      ,
            "spinner_text"      : self.spinner_text         ,
        }
        return get_style(style, False)


def menu(
        message             : str                               ,
        
        options             : list[str]                         ,
        border              : bool          = False             ,
        
        style               : Style | None  = None              ,
        
        qmark               : str           = "#"               ,
        pointer             : str           = ">"               ,
        
        instruction         : str           = ""                ,
        long_instruction    : str           = ""                ,
        
        key_binds           : dict | None   = None              ,
        
        mandatory           : bool          = True              ,
        mandatory_message   : str           = "Mandatory Menu"  ,
    ) -> int:

    """ Show a menu with the options passed and returns the index of the option in the list.
        
        `message`	| :class:`Str`
            Menu title, message that will be written above the menu.
        `options`	| :class:`list` [ Str , ... ]
            Options listed in the menu, buttons.				
        `style`		| :class:`dict` { Style }
            Menu color style.
        `qmark`     | :class:`str`
            menu message/title marker, shown to the left of them.
    """

    _menu_options = []
    _index = 0
    for _item in options:
        _item = _item.lower()

        if 	 _item in ("separator"):
            _menu_options.append(Separator())
        
        else:
            _menu_options.append(Choice(_index, _item))
        
        _index += 1
    
    return inquirer.select(
        message             = message                ,
        choices             = _menu_options          ,
        keybindings         = key_binds              ,
        style               = get_style(style, False),
        qmark               = qmark                  ,
        instruction         = instruction            ,
        long_instruction    = long_instruction       ,
        mandatory           = mandatory              ,
        mandatory_message   = mandatory_message      ,
        border              = border                 ,
        pointer             = pointer                ,
    ).execute()


def entry(
        message             : str                               ,
        
        validate            : str | None    = None              ,
        invalid_message     : str           = "Invalid Input"   ,
        is_password         : bool          = False             ,
        
        style               : Style | None  = None              ,

        qmark               : str           = ">"               ,
        amark               : str           = "|"               ,

        instruction         : str           = ""                ,
        long_instruction    : str           = ""                ,

        key_binds           : dict | None   = None              ,

        mandatory           : bool          = True              ,
        mandatory_message   : str           = "Mandatory Entry" ,
    ) -> str | int:

    """
    """

    return inquirer.text(
        message 			= message,
		validate			= validate,
		invalid_message		= invalid_message,
		is_password			= is_password,
		style				= get_style(style, False),
		keybindings			= key_binds,
		qmark				= qmark,
		amark				= amark,
		instruction			= instruction,
		long_instruction	= long_instruction,
		mandatory			= mandatory,
		mandatory_message	= mandatory_message
    ).execute()


def confirm(
        message             : str                               ,
        
        confirm_letter		: str			="y"                ,
		reject_letter		: str			="n"                ,

        style               : Style | None  = None              ,

        qmark               : str           = ">"               ,
        amark               : str           = "|"               ,

        instruction         : str           = ""                ,
        long_instruction    : str           = ""                ,

        key_binds           : dict | None   = None              ,

        mandatory           : bool          = True              ,
        mandatory_message   : str           = "Mandatory Entry" ,
    ) -> bool:

    """
    """

    return inquirer.confirm(
        message 			= message,
		confirm_letter		= confirm_letter,
		reject_letter		= reject_letter,
		style				= get_style(style, False),
		qmark				= qmark,
		amark				= amark,
		instruction			= instruction,
		long_instruction	= long_instruction,
		keybindings			= key_binds,
		mandatory			= mandatory,
		mandatory_message	= mandatory_message
    ).execute()