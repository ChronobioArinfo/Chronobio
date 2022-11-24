from pydantic import BaseModel


class LoanJSON(BaseModel):
    amount: int
    start_day: int
