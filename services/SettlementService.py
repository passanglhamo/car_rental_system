from datetime import datetime
"""
    This service is responsible for calculating late-return days and
    settlement fees for rented vehicles.
"""
class SettlementService:

    LATE_FEE_PER_DAY = 20

    """
        Method to calculate the number of days a car was returned late.

        Args:
            end_date: The agreed rental end date.
            return_date: The actual car return date. 

        Returns:
            int: Number of late days. Returns 0 if the vehicle was
                 returned on or before the agreed end date.
    """
    def calculate_late_days(self, end_date, return_date):
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        if isinstance(return_date, str):
            return_date = datetime.strptime(return_date, "%Y-%m-%d").date()

        if return_date <= end_date:
            return 0

        return (return_date - end_date).days

    """
        Method to calculate the total settlement fee for a late vehicle return.

        The settlement fee is calculated by multiplying the number
        of late days by the fixed daily late fee.

        Args:
            end_date: The agreed rental end date.
            return_date: The actual vehicle return date.

        Returns:
            int: Total late settlement fee.
    """
    def calculate_settlement_fee(self, end_date, return_date):
        late_days = self.calculate_late_days(
        end_date,
        return_date
        )

        return late_days * self.LATE_FEE_PER_DAY