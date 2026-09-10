from datetime import datetime
class SettlementService:

    LATE_FEE_PER_DAY = 20

    def calculate_late_days(self, end_date, return_date):
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        if isinstance(return_date, str):
            return_date = datetime.strptime(return_date, "%Y-%m-%d").date()

        if return_date <= end_date:
            return 0

        return (return_date - end_date).days


    def calculate_settlement_fee(self, end_date, return_date):
        late_days = self.calculate_late_days(
        end_date,
        return_date
        )

        return late_days * self.LATE_FEE_PER_DAY