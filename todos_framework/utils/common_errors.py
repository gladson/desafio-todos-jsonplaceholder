import datetime
from typing import Any, Optional

from flask import abort, jsonify, make_response

from todos_framework.model.messages_error_schema import (
    Error,
    MessagesErrorSchema,
)
from todos_framework.utils.logger import Logger


def common_error_httpx(
    *,
    messageError: Optional[dict],
    responseErrorMessage: Any,
):
    if not messageError:
        message_error_log = {
            "status_code": str(responseErrorMessage.status_code),
            "description": str(responseErrorMessage.reason_phrase)
            if hasattr(responseErrorMessage, "is_error")
            and responseErrorMessage.is_error
            else str(responseErrorMessage.status),
            "timestamp": str(
                datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            ),
        }
        Logger(msg=message_error_log).error()
        message_error_client = MessagesErrorSchema(
            error=Error(
                reason=str(responseErrorMessage.reason_phrase)
                if hasattr(responseErrorMessage, "is_error")
                and responseErrorMessage.is_error
                else str(responseErrorMessage.status),
            ),
        )
        abort(
            make_response(
                jsonify(message_error_client.json()),
                responseErrorMessage.status_code,
            )
        )
    else:
        message_error_client = MessagesErrorSchema(
            error=Error(
                reason=str(messageError["reason_phrase"]),
            ),
        )
        abort(
            make_response(
                jsonify(message_error_client.json()),
                messageError["status_code"],
            )
        )
