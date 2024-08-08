

# $c_{n}^{I}$:

To compute $c_{n}^{I}$, you require the computation of:

$$c_{n}^{I} = C_{++}(n) \text{Re} \left[ \mathcal{C}_{++}^{I} (n | \mathcal{F})\right] + C_{0+}(n) \text{Re} \left[ \mathcal{C}_{0+}^{I} (n | \mathcal{F}_{eff})\right] + C_{-+}(n) \text{Re} \left[ \mathcal{C}_{-+}^{I} (n | \mathcal{F}_{T})\right].$$

We handle the computation of the $c_{n}^{I}$ with a fixed $n$ with the function `calculate_c_interference_coefficient`. This function calls the associated function for a given $n$: If $n = 2$, then we call the functions corresponding to $C_{++}(2)$, $C_{0+}(2)$ and $C_{-+}(2)$. 

# $s_{n}^{I}$:

To compute $s_{n}^{I}$, you actually need a hell of a lot of other ingredients. First of all, you need the standard $S_{++}(n)$, $S_{0+}(n)$, and $S_{-+}(n)$ contrubutions depending on $n$. 

$$s_{n}^{I} = S_{++}(n) \text{Im} \left[ \mathcal{S}_{++}^{I} (n | \mathcal{F})\right] + S_{0+}(n) \text{Im} \left[ \mathcal{S}_{0+}^{I} (n | \mathcal{F}_{eff})\right] + S_{-+}(n) \text{Im} \left[ \mathcal{S}_{-+}^{I} (n | \mathcal{F}_{T})\right].$$

# $\text{Im} \left[ \mathcal{S}_{++}^{I} (n | \mathcal{F})\right]$

To compute $\text{Im} \left[ \mathcal{S}_{++}^{I} (n | \mathcal{F})\right]$, you require computation of $\mathcal{C}^{I}(\mathcal{F})$, 

So, the chronology is the following:

1. Calculate $\mathcal{C}^{I}(\mathcal{F})$
2. Calculate $\mathcal{C}^{I. V}(\mathcal{F})$, 
3. Calculate $\mathcal{C}^{I, A}(\mathcal{F})$, 

Then, based on the integer $n$, we compute

1. 