from antlr4.error.ErrorListener import ErrorListener

class GrammarError(Exception):
    pass

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"line {line}:{column} {msg}"
        self.errors.append(error_message)

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return "\n".join(self.errors)
