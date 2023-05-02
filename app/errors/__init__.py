from typing import Optional


class ResourceNotFoundError(Exception):
    def __init__(self, description: str = ""):
        self.description = description
        return super().__init__(description)
