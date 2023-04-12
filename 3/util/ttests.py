from scipy.special import stdtr as t_cdf
import numpy as np

def compute_t_1samp(x, null_mean = 0):
    '''
    Computes the t-stat for a one-sample t-test.

    Arguments
    ---------
    x : array of shape (n_observations,)
        The data,
    null_mean : float
        Distribution mean under the null hypothesis.

    Returns
    --------
    t : float
        The t-statistic
    '''
    delta = x - null_mean
    n_obs = delta.shape[0]
    var = ((delta - delta.mean())**2).sum() / (n_obs - 1)
    se = np.sqrt(var / n_obs)
    t = delta.mean() / se
    return t

def compute_p_ttest(t, n_obs, tail = 0):
    '''
    Computes the p-value for a t-test.

    Arguments
    ---------
    t : float
        The t-statistic.
    n_obs : int
        The number of observations (i.e. sample size).
    tail : -1 or 0 or 1 (default = 0)
        If tail is 1, the alternative hypothesis is that the
        mean of the data is greater than 0 (upper tailed test).  If tail is 0,
        the alternative hypothesis is that the mean of the data is different
        than 0 (two tailed test).  If tail is -1, the alternative hypothesis
        is that the mean of the data is less than 0 (lower tailed test).

    Returns
    ---------
    p : float
        The p-value.
    '''
    df = n_obs - 1
    if tail == 0:
        p = 2 * t_cdf(df, -np.abs(t))
    elif tail == 1:
        p = t_cdf(df, -t)
    elif tail == -1:
        p = t_cdf(df, t)
    else:
        raise Exception('tail argument must be -1, 0, or 1!')
    return p

def ttest_1samp(x, null_mean = 0, tail = 0):
    '''
    A one-sample t-test.

    Arguments
    ---------
    x : array of shape (n_observations,)
        Your data.
    null_mean : float
        The distribution mean under the null hypothesis.
    tail : -1 or 0 or 1 (default = 0)
        If tail is 1, the alternative hypothesis is that the
        mean of the data is greater than 0 (upper tailed test).  If tail is 0,
        the alternative hypothesis is that the mean of the data is different
        than 0 (two tailed test).  If tail is -1, the alternative hypothesis
        is that the mean of the data is less than 0 (lower tailed test).

    Returns
    ---------
    t : float
        The t-statistic.
    p : float
        The p-value.
    '''
    n_obs = x.shape[0]
    t = compute_t_1samp(x, null_mean)
    p = compute_p_ttest(t, n_obs, tail)
    return t, p

def ttest_paired(x0, x1, tail = 0):
    '''
    A paired-sample t-test.

    Arguments
    ---------
    x0 : array of shape (n_observations,)
    x1 : array of shape (n_observations,)
    tail : -1 or 0 or 1 (default = 0)
        If tail is 1, the alternative hypothesis is that the
        mean of x0 is greater than that of x1. If tail is -1,
        the alternative is that the mean of x1 is greater than
        that of x0. If tail is 0, then the alternative is that
        the means are different from one another.

    Returns
    ---------
    t : float
        The t-statistic.
    p : float
        The p-value.
    '''
    t, p = ttest_1samp(x0 - x1, 0, tail)
    return t, p
