from dataclasses import dataclass
from typing import List, Any


@dataclass
class SBDBCloseApproachResponse:
    signature: dict
    count: int
    fields: List[str]
    data: List[Any]
