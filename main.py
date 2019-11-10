import sys

__version__ = "1.0.0"

GRAMMARS = {"асинк функция": "async def",
            "функция": "def",
            "эвейт": "await",
            "пиши": "print",
            "импорт": "import",
            "погнали": "for",
            "пока": "while",
            "нуилиж": "elif",
            "если": "if",
            "иначе": "else",
            "вернуть": "return",
            "ввести": "input",
            "класс": "class",
            "сумма": "sum",
            "районе": "range",
            "дальше": "continue",
            "ниче": "pass",
            "харош": "break",
            "попробуй": "try",
            "сломалось": "except",
            "анонфункция": "lambda",
            "длина": "len",
            "супер": "super",
            "заокругли": "round",
            "@статикфунка": "@staticmethod()"
            }

CONDITIONS_AND_ETC = {"из": "from", "в": "in", "как": "as"}

TYPES = {"Правда": "True",
         "Ложь": "False",
         "строка": "str",
         "число": "int",
         "хз": "bool",
         "словарь": "dict",
         "список": "list",
         "недосписок": "tuple",
         "множество": "set"
        }

GRAMMARS.update(TYPES)
GRAMMARS.update(CONDITIONS_AND_ETC)


def get_file_name() -> str:
    try:
        name = sys.argv[1]
        return name
    except IndexError:
        raise ValueError("Bad file name")


def get_mode() -> str:
    # run - try run RUPYTHON code
    # compile - compile python to rupython.
    try:
        mode = sys.argv[2]
    except IndexError:
        mode = "run"

    if mode not in ["compile", "run"]:
        raise ValueError("Bad mode")

    return mode


def translate(file_name: str, grammars: dict) -> str:
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
        for k,v in grammars.items():
            text = text.replace(k, v)
    return text


def compile(code: str):  # noqa
    with open(f"ru{file}", "w") as f:
        pre = f"""
# TRANSLATED BY RUPYTHON {__version__}
#
# При поддержке шизов!
"""
        f.write(pre + code)


if __name__ == '__main__':

    file = get_file_name()
    mode = get_mode()
    if mode == "run":
        grammars = GRAMMARS
    else:
        grammars = {v: k for k, v in GRAMMARS.items()}
    code = translate(file, grammars)

    if mode == "run":
        exec(code)
    elif mode == "compile":
        compile(code)

