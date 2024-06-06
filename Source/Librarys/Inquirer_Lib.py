
from typing import Any
from InquirerPy                 import inquirer, get_style
from InquirerPy.utils           import InquirerPyStyle
from InquirerPy.base.control    import Choice
from InquirerPy.separator       import Separator
from os                         import system

# Style Class
class Style():
    "Simplifies `InquirerPy's` Styling system"

    # application example
    {"questionmark" : "fg:#ffffff bg:#ffffff underline bold"}
    # https://inquirerpy.readthedocs.io/en/latest/pages/style.html

    def __init__(self) -> None:
        "Instantiate the variables"
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
        "Returns the style according to the object variables"

        style = {
            "questionmark"      : self.questionmark         ,
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

class Option():
    def __init__(self, message:str, value:any = None) -> None:
        self.message = message
        self.value = value
    
    def __call__(self) -> Any:
        self.value = self.message if self.value == None else self.value
        return Choice(self.value, self.message)

class Entry():
    def __init__(self,
            message             : str = '',
            style               : Style = None,
            default             : str = '',
            question_mark       : str = '|',
            answer_mark         : str = '|',
            instruction         : str = '',
            long_instruction    : str = '',
            auto_complete       : dict[dict | str | None] = None,
            validate            : callable = None,
            invalid_message     : str = 'Invalid Input',
            transformer         : callable = None,
            is_password         : bool = False,
            mandatory           : bool = False,
            mandatory_message   : str = 'Mandatory prompt'
        ) -> None:

        self.message            = message
        self.style              = style
        self.default            = default
        self.question_mark      = question_mark
        self.answer_mark        = answer_mark
        self.instruction        = instruction
        self.long_instruction   = long_instruction
        self.auto_complete      = auto_complete
        self.validate           = validate
        self.invalid_message    = invalid_message
        self.transformer        = transformer
        self.is_password        = is_password
        self.mandatory          = mandatory
        self.mandatory_message  = mandatory_message
        self.keybindings        = {
            "skip": [{"key": "c-b"}],
            "interrupt": [{"key": "c-c"}]
        }
    
    def __call__(self) -> str:
        return inquirer.text(
            self.message, self.style, False, self.default,
            self.question_mark,self.answer_mark, self.instruction,
            self.long_instruction, self.auto_complete, False, False,
            self.validate, self.invalid_message, self.transformer,
            None, self.keybindings, True, False, self.is_password, self.mandatory,
            self.mandatory_message
        ).execute()

class Select():
    def __init__(self,
            messagem            : str = '',
            choices             : list[Option] = [Option('Option 1', None)],
            default             : str = None,
            style               : Style = None,
            question_mark       : str = '|',
            answer_mark         : str = '|',
            pointer             : str = '>',
            instruction         : str = '',
            long_instruction    : str = '',
            transformer         : callable = None,
            height              : int | None = None,
            multiselect         : bool = False,
            marker_select       : str = '[x]',
            marker_empty        : str = '[ ]',
            border              : bool = False,
            validate            : callable = None,
            invalid_message     : str = 'Invalid Input',
            show_cursor         : bool = False,
            cycle               : bool = False,
            mandatory           : bool = False,
            mandatory_message   : str = 'Mandatory prompt'
        ) -> None:

        self.messagem           = messagem
        self.choices            = choices
        self.default            = default
        self.style              = style
        self.question_mark      = question_mark
        self.answer_mark        = answer_mark
        self.pointer            = pointer
        self.instruction        = instruction
        self.long_instruction   = long_instruction
        self.transformer        = transformer
        self.height             = height
        self.multiselect        = multiselect
        self.marker_select      = marker_select
        self.marker_empty       = marker_empty
        self.border             = border
        self.validate           = validate
        self.invalid_message    = invalid_message
        self.show_cursor        = show_cursor
        self.cycle              = cycle
        self.mandatory          = mandatory
        self.mandatory_message  = mandatory_message
        self.keybindings        = {
            "skip": [{"key": "c-b"}],
            "interrupt": [{"key": "c-c"}]
        }

    def __call__(self) -> str:
        return inquirer.select(
            self.messagem, self.choices, self.default, self.style,
            True, self.question_mark, self.answer_mark, self.pointer,
            self.instruction, self.long_instruction, self.transformer,
            None, self.height, None, self.multiselect, self.marker_select,
            self.marker_empty, self.border, self.validate, self.invalid_message,
            self.keybindings, self.show_cursor, self.cycle, True, True,
            self.mandatory, self.mandatory_message, None
        ).execute()
    
