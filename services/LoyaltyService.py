"""
    This service class is responsible for calculating customer loyalty points.

    Loyalty points are awarded based on the rental fee. Customers
    receive 1 loyalty point for every $10 spent on a rental.
"""
class LoyaltyService:

    POINTS_PER_DOLLAR = 10

    """
        Method to calculate the number of loyalty points earned from a rental.

        The calculation uses integer division, meaning only complete
        $10 amounts contribute to loyalty points.

        Args:
            rental_fee (float): Total rental fee paid by the customer.

        Returns:
            int: Number of loyalty points earned.
                 Returns 0 when the rental fee is zero or negative.
    """
    def calculate_points(self, rental_fee):
        if rental_fee <= 0:
            return 0

        return int(rental_fee // self.POINTS_PER_DOLLAR)

    """ 
        Method to calculates the monetary value of loyalty points. 
        Each loyalty point is worth $0.10 because customers receive 1 point 
        for every $10 spent. Args: loyalty_points (int): 
        Number of loyalty points available. 
        Returns: float: Monetary value of the loyalty points. 
        Returns 0 when the loyalty points are zero or negative. 
            
    """ 
    def calculate_amount(self, loyalty_points): 
      
        if loyalty_points <= 0: return 0.0 
        return loyalty_points / self.POINTS_PER_DOLLAR 
    
    """
        Method to calculates the  discount value for a given number of loyalty points.
        Each point is worth $0.10 based on the 10 points per dollar earning rule.

        Args:
            loyalty_points (int): Number of loyalty points to redeem.

        Returns:
            float: The  discount value in dollars. 
                   Returns 0.0 when loyalty points are zero or negative.
        """
    def calculate_discount(self, loyalty_points):
        
        if loyalty_points <= 0:
            return 0.0
            
        # Reuses the calculation logic or computes directly
        return loyalty_points / self.POINTS_PER_DOLLAR