from flask import Flask
from flask_restx import Api
from werkzeug.exceptions import HTTPException

from todos_framework.endpoint.todo_router import todo_api_namespace
from todos_framework.utils.common_errors import common_error_httpx

app = Flask(__name__)
app.config["RESTX_MASK_SWAGGER"] = False
app.config["ERROR_INCLUDE_MESSAGE"] = False

api = Api(
    app,
    version="0.1.0",
    title="Todo Framework",
    description="Desafio Tecnico - Todo Framework",
)

api.add_namespace(todo_api_namespace)


@api.errorhandler(HTTPException)
def handle_exception(e):
    common_error_httpx(
        messageError=None,
        responseErrorMessage=e.get_response(),
    )


# if __name__ == "__main__":
#     app.run(
#         host="0.0.0.0",
#         port=int(os.environ.get("PORT", 5000)),
#         debug=bool(os.environ.get("DEBUG", True)),
#     )
