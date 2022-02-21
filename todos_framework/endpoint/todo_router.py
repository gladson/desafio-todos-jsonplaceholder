from flask_restx import Namespace, Resource
from flask_restx.reqparse import RequestParser

from todos_framework.model.todo_swagger import todo_model_swagger

from todos_framework.dao.todo_dao import TodoDAO

todo_api_namespace = Namespace("todos", description="TODO operations")
marshal_todo_model_swagger = todo_model_swagger(todo_api_namespace)

pagination_parser: RequestParser = todo_api_namespace.parser()
pagination_parser.add_argument(
    "_start",
    type=int,
    default=0,
    help="Page number",
)
pagination_parser.add_argument(
    "_limit",
    type=int,
    help="Page size",
)


@todo_api_namespace.route("/")
class TodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new todo"""

    @todo_api_namespace.doc("list_todos")
    @todo_api_namespace.marshal_list_with(marshal_todo_model_swagger)
    @todo_api_namespace.expect(pagination_parser, validate=True)
    def get(self):
        """List all todos"""
        todos = TodoDAO().get(
            id=None,
            pagination=pagination_parser,
        )
        return todos

    @todo_api_namespace.doc("create_todo")
    @todo_api_namespace.expect(marshal_todo_model_swagger)
    @todo_api_namespace.marshal_with(marshal_todo_model_swagger, code=201)
    def post(self):
        """Create a new todo"""
        return (
            TodoDAO().create(
                data=todo_api_namespace.payload,
            ),
            201,
        )


@todo_api_namespace.route("/<int:id>")
@todo_api_namespace.response(404, "Todo not found")
@todo_api_namespace.param("id", "The todo identifier")
class Todo(Resource):
    """Show a single todo item and lets you delete them"""

    @todo_api_namespace.doc("get_todo")
    @todo_api_namespace.marshal_with(marshal_todo_model_swagger)
    def get(self, id):
        """Fetch a given resource"""
        return TodoDAO().get(
            id,
            pagination=pagination_parser,
        )

    @todo_api_namespace.doc("delete_todo")
    @todo_api_namespace.response(204, "Todo deleted")
    def delete(self, id):
        """Delete a todo given its identifier"""
        return TodoDAO().delete(id)

    @todo_api_namespace.expect(marshal_todo_model_swagger)
    @todo_api_namespace.marshal_with(marshal_todo_model_swagger)
    def put(self, id):
        """Update a todo given its identifier"""
        return TodoDAO().update(
            id,
            data=todo_api_namespace.payload,
        )
