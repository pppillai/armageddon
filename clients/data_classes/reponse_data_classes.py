from dataclasses import dataclass
from typing import List, Any


@dataclass
class SBDBCloseApproachResponse:
    """
    Data class for Response.
    Using this we can validate response structure.
    """
    signature: dict
    count: int
    fields: List[str]
    data: List[Any]
