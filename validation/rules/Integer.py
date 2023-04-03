from typing import Any

from validation.rules.BaseRule import BaseRule


class Integer(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return isinstance(value, int)

    def message(self, attribute: str) -> str:
        return f"{attribute} is not an integer"
