from .log_level import LogLevel
from .log_type import LogType

from dataclasses import dataclass
from typing import Dict


@dataclass
class LogEntry:
    log_level: LogLevel
    log_type: LogType
    payload: Dict[str, str]
