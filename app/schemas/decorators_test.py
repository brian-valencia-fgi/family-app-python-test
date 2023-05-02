from dataclasses import dataclass

class DecoratorsTestApiSchemas:
    @dataclass
    class PostRequest:
        a: int
        b: str
        c: float
    
    @dataclass
    class PostResponse:
        message: str
        body: 'DecoratorsTestApiSchemas.PostRequest'
    