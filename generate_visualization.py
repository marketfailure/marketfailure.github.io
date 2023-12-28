import matplotlib.pyplot as plt
import numpy as np

def generate_beta_distribution(alpha, beta):
    x = np.linspace(0, 1, 1000)
    y = (x**(alpha-1) * (1-x)**(beta-1)) / (np.math.gamma(alpha) * np.math.gamma(beta) / np.math.gamma(alpha+beta))
    plt.plot(x, y)
    plt.xlabel('p')
    plt.ylabel('Density')
    plt.title('Beta Distribution')
    plt.savefig('beta_distribution.png')  # Save the plot as an image

def update_beta(alpha, beta, trials, successes):
    alpha+=alpha + successes
    beta+= trials - successes
    return alpha, beta
