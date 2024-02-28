# Links
#   https://inquirerpy.readthedocs.io/en/latest/index.html
#   https://github.com/magmax/python-inquirer/tree/main/examples
#
# Auto Complite example:
#   {"python":{
#        "esta":{
#            "presente aqui": None
#        },
#        "é":{
#            "minha linguagem favorita": None
#        }
#   }}

STYLES = [
	{	# underline, italic, bold, reverse, hidden, blink
		"questionmark": "fg:#e5c07b bg:#ffffff underline bold"
	},
	{
		# Marcações conhecidas
		"questionmark"      : "#e5c07b",    # Marcador do input (qmark)
		"question"			: "",           # Cor da mensagem no input
		"input"			    : "#98c379",    # cor do input
		
		"answermark"        : "#e5c07b",    # Marcador da resposta (amark)
		"answered_question" : "",           # Cor da mensagem na resposta
		"answer"			: "#61afef",    # Cor da resposta

		"validator"		    : "#ff0000",	# Cor da mensagem de erro do validador

		"pointer"			: "#ff0000",	# Cor do ponteiro do Select

		"instruction"		: "#ff0000",	# Cor da instrução no questionmark
		"long_instruction"	: "#ff0000",	# Cor da instrução no roda pé

		# Marcações não mapeadas
		"checkbox"			: "#ff0000",
		"separator"		    : "#ff0000",
		"skipped"			: "#ff0000",
		
		"marker"			: "#ff0000",
		"fuzzy_prompt"		: "#ff0000",
		"fuzzy_info"		: "#ff0000",
		"fuzzy_border"		: "#ff0000",
		"fuzzy_match"		: "#ff0000",
		"spinner_pattern"	: "#ff0000",
		"spinner_text"		: "#ff0000"	
	}
]
