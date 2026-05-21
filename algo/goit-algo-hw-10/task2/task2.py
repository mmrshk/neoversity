import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x):
    return x**2


a = 0  # нижня межа
b = 2  # верхня межа


def monte_carlo_integral(func, lower, upper, n=100_000, seed=42):
    """Інтеграл ∫_a^b f(x)dx ≈ (b-a) * середнє(f(x_i)), x_i ~ Uniform[a,b]."""
    rng = np.random.default_rng(seed)
    x_random = rng.uniform(lower, upper, n)

    return (upper - lower) * np.mean(func(x_random))


def analytical_integral():
    """∫₀² x² dx = x³/3 |₀² = 8/3"""
    return 8 / 3


def plot_integration(func, lower, upper):
    x = np.linspace(-0.5, 2.5, 400)
    y = func(x)

    _fig, ax = plt.subplots()
    ax.plot(x, y, "r", linewidth=2)

    ix = np.linspace(lower, upper)
    iy = func(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.axvline(x=lower, color="gray", linestyle="--")
    ax.axvline(x=upper, color="gray", linestyle="--")
    ax.set_title(f"Інтегрування f(x) = x² від {lower} до {upper}")
    ax.grid()
    plt.tight_layout()
    plt.show()


def compare_methods(n_samples=100_000):
    mc = monte_carlo_integral(f, a, b, n=n_samples)
    exact = analytical_integral()
    quad_val, quad_err = spi.quad(f, a, b)

    print("--- Порівняння методів ---")
    print(f"Monte Carlo (N={n_samples:,}): {mc:.8f}")
    print(f"Аналітично (8/3):           {exact:.8f}")
    print(f"scipy.quad:                 {quad_val:.8f} (оцінка похибки ≈ {quad_err:.2e})")
    print(f"|MC - аналітично|:          {abs(mc - exact):.8f}")
    print(f"|MC - quad|:                {abs(mc - quad_val):.8f}")
    print(f"|quad - аналітично|:        {abs(quad_val - exact):.8f}")

    print("\n--- Висновки ---")
    print(
        "Метод Монте-Карло наближає площу під кривою; при збільшенні N "
        "похибка зазвичай зменшується."
    )
    print(
        "quad та аналітична формула збігаються з високою точністю — "
        "вони підтверджують коректність MC."
    )


def benchmark_sample_sizes():
    print("\n--- Залежність від кількості випадкових точок ---")
    exact = analytical_integral()
    for n in (1_000, 10_000, 100_000, 1_000_000):
        mc = monte_carlo_integral(f, a, b, n=n)
        print(f"N={n:>9,}: MC={mc:.6f}, |MC - 8/3|={abs(mc - exact):.6f}")


if __name__ == "__main__":
    compare_methods()
    benchmark_sample_sizes()
    plot_integration(f, a, b)
