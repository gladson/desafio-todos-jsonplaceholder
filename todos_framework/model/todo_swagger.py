from flask_restx import fields


def todo_model_swagger(todo_api_namespace):
    return todo_api_namespace.model(
        "Todo",
        {
            "id": fields.Integer(
                readonly=True,
                description="<id do registro>",
            ),
            "title": fields.String(
                required=True,
                description="<nome do registro>",
            ),
        },
    )
