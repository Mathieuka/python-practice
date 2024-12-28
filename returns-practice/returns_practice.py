from typing import Optional
from returns.maybe import Maybe, maybe


@maybe  # decorator to convert existing Optional[int] to Maybe[int]
def bad_function() -> Optional[int]: ...


maybe_number: Maybe[float] = bad_function().bind_optional(
    lambda number: number / 2,
)
# => Maybe will return Some[float] only if there's a non-None value
#    Otherwise, will return Nothing
