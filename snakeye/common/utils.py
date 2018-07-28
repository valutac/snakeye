from string import Template


def ask_input(label, validate=True):
    valid = False
    result: str = ""
    while not valid:
        result = input(label)
        valid = validate and result != ""

    return result


def parse_template(path, ctx):
    setup = open(path)
    src = Template(setup.read())
    return src.substitute(ctx)
