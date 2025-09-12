from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass(frozen=True)
class Branding:
    name: str
    colors: Dict[str, str]
    fonts: Dict[str, str]
    logo_path: Optional[str] = None


@dataclass
class Document:
    markdown: str
    meta: Dict[str, Any] = field(default_factory=dict)