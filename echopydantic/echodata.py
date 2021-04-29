from pydantic import BaseModel, Field
from .toplevel import Toplevel

class EchoData(BaseModel):
    toplevel: Toplevel = Field(...)