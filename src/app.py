

class ConventionClass:
    def __init__(self, some_input: str) -> None:
        self._some_input = some_input

    def some_method(self) -> str:
        return self._some_input

if __name__ == "__main__":
    convention_class = ConventionClass(some_input="Hello World")