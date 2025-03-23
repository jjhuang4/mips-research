This is a summary of our current matching methods for creating a weight-based matching algorithm for factorial designs. 

### First step:

Originally we'd be estimating optimal weights $w_i$ for each observation $i$. These weights encode balance of both treatment assignment and covariate values, but are continuous. We want to create a subsample of these weights for matching, so we instead solve a different optimization problem with the same balancing constraints but this time changing the objective function to a maximization of the sample size:

Obj:  $\max \sum w_i$

as opposed to

Obj: $\min \sum w_i^2$


However, it may be infeasible to exactly solve the original optimization problem's balancing constraints if $w_i \in{0,1}$. It cannot pick a strict subset that exactly reproduces the entire sample’s sums.

Therefore, we allow a tolerance on the SMD of the lhs and rhs for every balancing constraints. We calculate the SMD of the lhs and rhs of every balancing constraints and let them smaller than this tolerance value. 

### Second step:

We propose some methods for conducting matching after getting the initial subsample of 'weighted' observations.

Approach 1. We perform cluster based matching

The objective function for this is:

$$
\text{minimize} \quad \sum_{(i,j)} d_{(i,j)} \cdot x_{(i,j)} - \gamma \sum_i y_i + \sum_{(i,k)} \omega_k \cdot z_{(i,k)}
$$

Summing the Mahalanobis distance measure between covariates, $d_{(i,j)}$, over all pairs of observations $(i,j)$, with the penalty term $\gamma \sum_i y_i + \sum_{(i,k)} \omega_k \cdot z_{(i,k)}$ creating and maximizing the number of matched sets. The optimization problem maximizes the number of clusters / matched samples while minimizing the distance in covariate space within each matched set.

Some notes about the variables used:
- $\gamma$ hyperparameter (higher = less matched sets, lower = more matched sets)
	- The idea being, that more matched sets = higher precision/closer distance within that matched set, so we have better guarantees on the actual covariate balance within each matched set, as opposed to one single matched set where covariate balance can vary
	- However, tradeoff is that we will have smaller samples within each matched set, and we may also not have observations within a matched set that are representative of the whole treatment combination space (i.e, you will have multiple observations with 1-1-0 treatment and only one of 0-0-1, which isn't reliable for making a causal estimate).
- Imbalance penalty term $\omega_k$
	- (In Zubizarreta, uses higher moments such as variance, skew, etc, to additionally balance based on distribution and other statistical properties)


Approach 2: 