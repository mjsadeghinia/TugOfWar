import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

from activation_model import compute_delayed_activations
from heart_model import HeartModelPulse


delay = 0.0
geo_params = {
    "r_short_endo": 3,
    "r_short_epi": 3.75,
    "r_long_endo": 5,
    "r_long_epi": 5.75,
    "mesh_size": 1,
}
fe_model = HeartModelPulse(geo_params=geo_params)
delayed_activations = compute_delayed_activations(
    fe_model.geometry.cfun, num_time_step=500, std=delay
)
data = delayed_activations[0][0, :]
if delay == 0:
    offsets = np.zeros(len(data))
else:
    offsets = stats.norm.ppf(np.linspace(0.01, 0.99, len(data)), loc=0, scale=delay)
plt.hist(offsets * 1000, align="left")
plt.ylabel("No. of elements")
plt.xlabel("delays [ms]")
plt.xlim([-150, 150])
# %%
plt.plot(delayed_activations[0][:, :], "k-", linewidth=0.05)
plt.ylabel("Activation (kPa)")
plt.xlabel("Time (ms)")
# %%
