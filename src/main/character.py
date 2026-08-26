from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Character:
    """
    This class defines a Character object. Objects of this class represent one row of a database table. The
    table should be defined as follows to be compatible with these objects:

    CREATE TABLE character (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         first_name VARCHAR(255),
         last_name VARCHAR(255)
    );
    """
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
