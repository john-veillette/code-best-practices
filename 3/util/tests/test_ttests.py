from util.ttests import compute_p_ttest, ttest_1samp, ttest_paired
import numpy as np

def test_compute_p_ttest(n_simulations = 100):
    '''
    checks that p-values are always in range [0, 1].

    This doesn't mean that the function is giving the right answer,
    but a mediocre unit test is better than no unit test! It can still
    help you spot bugs.
    '''
    rng = np.random.default_rng(seed = 0)
    for i in range(n_simulations):
        # generate random t-val and sample size
        n = rng.integers(10, 100)
        t = rng.normal(loc = 1, scale = 5, size = 1)[0]
        for tail in [-1, 0, 1]:
            p = compute_p_ttest(t, n, tail)
            # assert statements that should be true 100% of the time
            assert(p >= 0.)
            assert(p <= 1.)
    return None

def test_ttest_paired(alpha = .05, n_simulations = 1000, wiggle_room = .01):
    '''
    verifies false positive rate is close to signifiance level by simulation.
    '''
    rng = np.random.default_rng(seed = 1)
    count_rejections = 0
    for i in range(n_simulations):
        # generate random null data
        x0 = rng.normal(loc = 0, size = 30)
        x1 = rng.normal(loc = 0, size = 30)
        t, p = ttest_paired(x0, x1)
        if p <= alpha:
            count_rejections += 1
    fpr = count_rejections / n_simulations
    assert(np.isclose(fpr, alpha, atol = wiggle_room))
    return None

def test_ttest_1samp(n_simulations = 10):
    '''
    compares to a reference implementation.

    A reference implementation isn't always available (otherwise, you'd probably
    just be using that instead of coding your own version.) But when it is,
    this is super handy. I've found a bug in my code just because another
    implementation fixed a bug in theirs, and then my unit tests notified me
    that our versions now differed.
    '''
    from scipy.stats import ttest_1samp as ttest_scipy
    rng = np.random.default_rng(seed = 3)
    for i in range(n_simulations):
        # generate random data with a random sample size
        n = rng.integers(10, 100)
        true_mean = rng.normal(loc = 1, scale = 5, size = 1)[0]
        x = rng.normal(loc = true_mean, size = n)
        # compare it to a random null mean with both implementations
        null_mean = rng.normal(loc = 1, scale = 5, size = 1)[0]
        t, p = ttest_1samp(x, null_mean)
        res = ttest_scipy(x, null_mean)
        # check that the output is the same
        assert(np.isclose(t, res.statistic))
        assert(np.isclose(p, res.pvalue))
    return None
