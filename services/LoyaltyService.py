class LoyaltyService:

    POINTS_PER_DOLLAR = 10

    def calculate_points(self, rental_fee):
        if rental_fee <= 0:
            return 0

        return int(rental_fee // self.POINTS_PER_DOLLAR)