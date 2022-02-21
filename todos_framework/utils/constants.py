from typing import Any, Mapping, Union


EXCLUDE_TODO: Mapping[Union[int, str], Any] = {
    "__root__": {
        "__all__": {"user_id", "completed"},
    }
}
