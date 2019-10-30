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

    with open(file, "r") as f:
        text = f.read()
        for k, v in GRAMMARS.items():
            text = re.sub(k, v, text)
    exec(text)
