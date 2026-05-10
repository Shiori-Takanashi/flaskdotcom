from flask import Flask

from flaskdotcom.app import create_app


def test_create_app() -> None:
    obj = create_app()
    assert isinstance(obj, Flask)
