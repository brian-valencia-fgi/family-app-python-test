from app.schemas.decorators_test import DecoratorsTestApiSchemas

def do_stuff(a: int, b: str, c: float):
    return {
        "message": "Body received",
        "body": {
            "a": a,
            "b": b,
            "c": c
        }
    }

def do_stuff_with_models(payload: DecoratorsTestApiSchemas.PostRequest):
    return DecoratorsTestApiSchemas.PostResponse(
        message="Body received",
        body=payload
    )