from typing import Any, Dict, Optional
from flask import jsonify, make_response

from todos_framework.model.todos_schema import TodoSchema
from todos_framework.utils import x_requests
from todos_framework.utils.constants import EXCLUDE_TODO
from todos_framework.utils.common_errors import common_error_httpx


class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(
        self,
        id: Optional[int],
        pagination: Any,
    ):
        self.todos = x_requests.get(
            url="https://jsonplaceholder.typicode.com/todos",
            params=pagination.parse_args()
            if hasattr(pagination, "parse_args")
            else None,
        )
        if self.todos.is_error:
            common_error_httpx(
                messageError=None, responseErrorMessage=self.todos
            )

        if not str(id) or id is None:
            todos = TodoSchema.parse_obj(self.todos.json()).dict(
                exclude=EXCLUDE_TODO
            )
            return make_response(jsonify(todos["__root__"])).json
        else:
            if any(todo["id"] == id for todo in self.todos.json()):
                for todo in self.todos.json():
                    if todo["id"] == id:
                        todo_schema = TodoSchema.parse_obj(
                            [todo],
                        ).dict(exclude=EXCLUDE_TODO)
                        return make_response(
                            jsonify(todo_schema["__root__"][0])
                        ).json
            else:
                common_error_httpx(
                    messageError={
                        "reason_phrase": "Not Found",
                        "status_code": 404,
                    },
                    responseErrorMessage=None,
                )

    def create(self, data: Dict):
        todo = data
        self.todos = x_requests.post(
            url="https://jsonplaceholder.typicode.com/todos", data=todo
        )
        if self.todos.is_error:
            common_error_httpx(
                messageError=None, responseErrorMessage=self.todos
            )
        return self.todos.json()

    def update(self, id, data: Dict):
        todo = self.get(id, pagination=None)
        self.todos = x_requests.put(
            url=(
                "https://jsonplaceholder.typicode.com/todos/" + str(todo["id"])
            ),
            data=data,
        )
        if self.todos.is_error:
            common_error_httpx(
                messageError=None, responseErrorMessage=self.todos
            )
        return self.todos.json()

    def delete(self, id):
        todo = self.get(id, pagination=None)
        self.todos = x_requests.delete(
            url=(
                "https://jsonplaceholder.typicode.com/todos/" + str(todo["id"])
            ),
        )
        if self.todos.is_error:
            common_error_httpx(
                messageError=None, responseErrorMessage=self.todos
            )
        return make_response(
            jsonify(self.todos.json()),
            204,
        )
