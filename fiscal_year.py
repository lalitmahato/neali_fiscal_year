import nepali_datetime

class CurrentNeplaiDateTime:
    def __init__(self):
        today = nepali_datetime.datetime.now()
        self.year = today.year
        self.month = today.month
        self.day = today.day
        self.hour = today.hour
        self.minute = today.minute

class FiscalYear(CurrentNeplaiDateTime):
    def __init__(self):
        super().__init__()
        self.fiscal_year = self.get_fiscal_year()
        self.today = self.get_today()
    
    def get_fiscal_year(self) -> str:
        if self.month < 4:
            current_fiscal_year = f"{self.year - 1}/{self.year}"
        else:
            current_fiscal_year = f"{self.year}/{self.year + 1}"
        return current_fiscal_year
    
    def get_today(self) -> str:
        return f"{self.year}/{self.month}/{self.day}"