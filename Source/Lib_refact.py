"""cliente = {
    'cliente 1' : ['banana', 'melancia', 'maça'],
    'Cleinte 2' : ['chocolate', 'pão', 'bolo']
}


for cliente, itens in cliente.items():
    print(f'Itens  do {cliente}')
    print(f'Item: {itens}')
    for item in itens:
        print(item)
    print()"""

















from InquirerPy                 import inquirer, get_style
from InquirerPy.base.control    import Choice
from InquirerPy.separator       import Separator
from InquirerPy.utils           import InquirerPyKeybindings, InquirerPySessionResult, InquirerPyStyle
from InquirerPy.validator       import PathValidator

from os import (
    system,
)

type func = object

def button(name, value) -> dict:
    return {'name': name, "value": value}

def key_bind(keys: list[str] | str, action: str) -> dict[str, list[str] | str]:
    """
        Avaliable `Keys`:
            | Escape - `escape` | Arrows - `left`, `right`, `up`, `down` |\n
            | Tab - `tab` | Delete - `delete` | F-key - `f1`, `f2` |\n
            | Navi - `home`, `end`, `delete`, `pageup`, `pagedown`, `insert` |\n
            | Control - `c-a`, `c-A`, `c-home`, `c-left`, `c-@` |\n
            | Shift - `s-a`, `s-A`, `s-end`, `s-up`, `s-^` |\n
            | Alt - `alt-a`, `alt-A`, `alt-insert`, `alt-down`, `alt-*` |\n
        
        Avaliable `Actions`:
            `skip`, `interrupt`, `toggle-all`
        """
    return {action: [{"key", keys if len(keys)>1 else keys[0]}]}

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





class Entry(inquirer.text):
    def __init__(
            self,
            message             : str           = "Entry:"          ,

            validate            : str | None    = None              ,
            invalid_message     : str           = "Invalid Input"   ,
            is_password         : bool          = False             ,
            auto_complet        : dict | None   = None              ,
            
            style               : Style | None  = None              ,

            qmark               : str           = ">"               ,
            amark               : str           = "|"               ,

            instruction         : str           = ""                ,
            long_instruction    : str           = ""                ,

            key_binds           : dict | None   = None              ,

            mandatory           : bool          = True              ,
            mandatory_message   : str           = "Mandatory Entry" ,
        ) -> int:

        

        super().__init__(
            message 			= message                           ,
            validate			= validate                          ,
            invalid_message		= invalid_message                   ,
            is_password			= is_password                       ,
            style				= get_style(style, False)           ,
            keybindings			= key_binds                         ,
            qmark				= qmark                             ,
            amark				= amark                             ,
            instruction			= instruction                       ,
            long_instruction	= long_instruction                  ,
            mandatory			= mandatory                         ,
            mandatory_message	= mandatory_message                 ,
            completer           = auto_complet                      
        )
    
    def __call__(self, *args: any, **kwds: any) -> any:
        return self.execute()
    

class Menu(inquirer.select):
    def __init__(
            self,
            message : str,
            choices : list[button] | list[dict[str, func]],
            style   : Style | None = None,
            vi_mode : bool = False,
            
            qmark   : str = "?",
            amark   : str = "?",
            pointer : str = ">",
            
            instruction      : str = "",
            long_instruction : str = "",
            
            transformer : func = None,
            filter      : func = None,
            
            height     : int | str = None,
            max_height : int | str = None,
            
            multiselect : bool = False,
            marker      : str  = "*",
            marker_pl   : str  = " ",
            
            border: bool = False,
            
            validate: func = None,
            invalid_message: str = "Invalid input",
            
            keybindings: key_bind = None,

            cycle: bool = True,
            
            mandatory: bool = True,
            mandatory_message: str = "Mandatory prompt"
        ) -> None:

        # DOC
        """
        Transformer:
            Without: | Select regions: ["us-east-1", "us-west-1"]
            With:    | Select regions: 2 regions selected

            ```
                transformer = lambda result:
                    f"{len(result)} region{'s' if len(result) > 1 else ''} selected"
            ```

        """

        super().__init__(
            message, choices, None, style, vi_mode, qmark, amark, pointer, instruction,
            long_instruction, transformer, filter, height, max_height, multiselect,
            marker, marker_pl, border, validate, invalid_message, keybindings,
            True, cycle, True, True, mandatory, mandatory_message, None
        )
        

    def __call__(self) -> any:
        option = self.execute()
        option()



class Entry_Menu(Menu):
    def __init__(
            self,
            message: str,
            entrys: list | list[dict[str, object]],
            style: Style | None = None,
            vi_mode: bool = False,
            qmark: str = "?",
            amark: str = "?",
            pointer: str = ">",
            instruction: str = "",
            long_instruction: str = "",
            transformer: object = None,
            filter: object = None,
            height: int | str = None,
            max_height: int | str = None,
            multiselect: bool = False,
            marker: str = "*",
            marker_pl: str = " ",
            border: bool = False,
            validate: object = None,
            invalid_message: str = "Invalid input",
            keybindings: key_bind = None,
            cycle: bool = True,
            mandatory: bool = True,
            mandatory_message: str = "Mandatory prompt"
        ) -> None:

        _funcs = []
        _names = []
        _values = []
        _len = 0
        for item in entrys:
            if type(item) in (tuple, list):
                _funcs.append(item[1])
                _names.append(item[0])
                _len = len(item[0]) if len(item[0]) > _len else _len
            else:
                _funcs.append(item)
                _names.append(item)
            
            _values.append(" ")

        self.max_button_len = _len
        self.buttons_function = _funcs
        self.buttons_name = _names
        self.entrys_values = _values


        _index = 0
        for item in entrys:
            self.buttons.update({})
            _index += 1

        self.buttons = {}




        self.message = message
        self.choices = entrys
        self.style = style
        self.vi_mode = vi_mode
        self.qmark = qmark
        self.amark = amark
        self.pointer = pointer
        
        self._instruction = instruction

        self.long_instruction = long_instruction
        self.transformer = transformer
        self.filter = filter
        self.height = height
        self.max_height = max_height
        self.multiselect = multiselect
        self.marker = marker
        self.marker_pl = marker_pl
        self.border = border
        self.validate = validate
        self.invalid_message = invalid_message
        self.keybindings = keybindings
        self.cycle = cycle
        self.mandatory = mandatory
        self.mandatory_message = mandatory_message

        
    
    def __call__(self) -> any:
        
        while True:
            _entrys = []
            _index = 0
            for item in self.buttons_name:
                if type(item) == str:
                    _entrys.append(button(f"{item[0]:<{self.max_button_len+1}}: {self.entrys_values[_index]}", _index))
                else:
                    _entrys.append(item)
                _index += 1
        
            self.choices = _entrys        
            super().__init__(
                self.message, self.choices, self.style, self.vi_mode, self.qmark,
                self.amark, self.pointer, self._instruction, self.long_instruction,
                self.transformer, self.filter, self.height, self.max_height, self.multiselect, 
                self.marker, self.marker_pl, self.border, self.validate, self.invalid_message,
                self.keybindings, self.cycle, self.mandatory, self.mandatory_message
            )
            selected = self.execute()

            _return_func = self.buttons_function[selected]()
            
    


def back():
    return "back"


Entry_Menu("teste",
    [
        ("name", Entry("name")),
        Separator(),
        ("teste_ok", back),
        ("back", back)
    ]
)()