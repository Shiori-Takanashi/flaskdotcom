from flask import Flask

from flaskdotcom.routes.company_routes import bp_company
from flaskdotcom.routes.home_routes import bp_home


def create_app() -> Flask:
    """
    1. Flaskオブジェクトを作成
    2. アプリにBlueprintを登録。
    3. Flaskオブジェクトを返す。
    """
    app = Flask(__name__)

    app.register_blueprint(bp_home)
    app.register_blueprint(bp_company)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
