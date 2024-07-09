import os, pathlib
from dotenv import load_dotenv

_path = pathlib.Path(".").resolve()
load_dotenv(_path / "secrets.env")

google_password = os.getenv("password")