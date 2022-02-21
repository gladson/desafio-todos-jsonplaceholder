from __future__ import annotations

from pydantic import BaseModel


class Error(BaseModel):
    reason: str


class MessagesErrorSchema(BaseModel):
    """
    ### Base de exemplo com modelo:
    {
        "error": {
            "reason": "error description",
        }
    }
    """

    error: Error
