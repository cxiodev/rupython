import sys
import re

GRAMMARS = {"асинк функция": "async def",
            "функция": "def",
            "эвейт": "await",
            "пиши": "print",
            "импорт": "import",
            "из": "from",
            "погнали": "for",
            "пока": "while",
            "в": "in",
            "как": "as",
            "строка": "str",
            "число": "int",
            "Правда": "True",
            "Ложь": "False"
            }

if __name__ == '__main__':
    try:
        file = sys.argv[1]
    except:
        raise SyntaxError("Bad file name")

    try:
        mode = sys.argv[2]
    except:
        mode = "compile"

    if mode not in ["compile", "translate"]:
        raise SyntaxError("Bad mode")

    if mode == "translate":
        GRAMMARS = {v: k for k, v in GRAMMARS.items()}

    with open(file, "r") as f:
        text = f.read()
        for k, v in GRAMMARS.items():
            text = re.sub(k, v, text)
    if not mode == "translate":
        exec(text)
    else:
        with open(f"ru{file}", "w") as f:
            f.write(text)
