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
    def __init__(self, S:float, K:float, T:float, r:float, sigma:float,option_type):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

        self.d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
        self.d2 = self.d1 - self.sigma * np.sqrt(self.T)

        self.sign = 1 if option_type == "call" else -1

    def price(self):
        return self.sign * (self.S * norm.cdf(self.sign * self.d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(self.sign * self.d2))

    def delta(self):
        return self.sign * (norm.cdf(self.sign * self.d1))

    def gamma(self):
        return norm.pdf(self.d1) / (self.S * self.sigma * np.sqrt(self.T))

    def vega(self):
        return self.S * norm.pdf(self.d1) * np.sqrt(self.T)

    def theta(self):
        theta1 = -(self.S * norm.pdf(self.d1) * self.sigma) / (2 * np.sqrt(self.T))
        theta2 = self.sign * self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(self.sign * self.d2)
        return theta1 - theta2

    def rho(self):
        return self.sign * self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(self.sign * self.d2)