from random import random, randint, choice
from html_reader import get_identifiers


PROPRETIES_RANGE = (2,4)

color = ["black", "silver", "gray", "white", "maroon", "red", "purple", "fuchsia", "green", "lime", "olive", "yellow", "navy", "blue", "teal", "aqua"]

identifiers = get_identifiers("index.html")

properties = [
    {
        "name": "background-color",
        "arguments": [color,]
    }
]

def generate_css(identifiers):
    result = ""

    # each rule
    for identifier in identifiers:
        result += identifier+" {\n"

        # each proprety
        for _ in range(randint(*PROPRETIES_RANGE)):
            proprety = choice(properties)

            #name: choice(argument) choice(argument)
            result += "\t{}: {}\n" \
                .format(
                    proprety["name"], 
                    " ".join([choice(argument) for argument in proprety["arguments"]])
                )

        result += "}\n\n"

    return result

print(generate_css(identifiers))