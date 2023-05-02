def do_stuff(a: int, b: str, c: float):
    return {
        "message": "Body received",
        "body": {
            "a": a,
            "b": b,
            "c": c
        }
    }