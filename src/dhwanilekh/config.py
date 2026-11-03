"""
Configuration management for DhwaniLekh.
"""

from dataclasses import asdict, dataclass
import json
from pathlib import Path
from typing import Any, Dict, Optional


@dataclass
class Config:
    hotkey: str = "ctrl+space"
    model_size: str = "base"
    compute_type: str = "int8"
    sample_rate: int = 16000
    language: Optional[str] = "en"
    paste_mode: str = "clipboard"  # "clipboard" or "typing"
    speak_status: bool = True

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Config":
        valid_fields = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
        return cls(**valid_fields)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def load(cls, path: Optional[Path] = None) -> "Config":
        if path is None:
            path = Path("settings.json")
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                return cls.from_dict(data)
            except Exception:
                return cls()
        config = cls()
        config.save(path)
        return config

    def save(self, path: Optional[Path] = None) -> None:
        if path is None:
            path = Path("settings.json")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")
