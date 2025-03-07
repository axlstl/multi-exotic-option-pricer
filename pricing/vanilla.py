import numpy as np
from scipy import norm

class VanillaOptions:
    """
    S : spot price at time t = 0
    K : strike price
    T : time to maturity (in years)
    r : risk-free interest rate
    sigma : implied volatility

    """
    def __init__(self, S:float, K:float, T:float, r:float, sigma:float):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

        self.d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
        self.d2 = self.d1 - self.sigma * np.sqrt(self.T)

    def price(self, option_type="call"):
        """
        Returns the price of a vanilla call or put option
        """
        if option_type.lower() == "call":
            return self.S * norm.cdf(self.d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2)
        elif option_type.lower() == "put":
            return self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2) - self.S * norm.cdf(-self.d1)
        else:
            raise ValueError("Invalid option type.")
