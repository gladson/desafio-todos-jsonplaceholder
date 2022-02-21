from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ModelItem(BaseModel):
    user_id: Optional[int] = Field(None, alias="userId")
    id: Optional[int] = None
    title: Optional[str] = None
    completed: Optional[bool] = None


class TodoSchema(BaseModel):
    """
    ### Base de exemplo com modelo:
    [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": false
        }
    ]
    """

    __root__: List[ModelItem]
