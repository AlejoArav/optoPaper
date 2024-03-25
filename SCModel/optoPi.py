from numpy import exp


def areaFunction(t, A_max, mu_max, t_0):
    """
    This function returns the area of a sigmoidal function at time t.

    Parameters
    ----------
    t : float
        Time at which to evaluate the function
    A_max : float
        Maximum area of the sigmoidal function
    mu_max : float
        Maximum growth rate of the sigmoidal function
    t_0 : float
        Time at which the growth rate is maximized

    Returns
    -------
    float
        Area of the sigmoidal function at time t
    """

    return A_max / (1 + exp(-mu_max * (t - t_0)))


def muFunction(t, mu_max, t_0):
    """
    This function returns the growth rate of a sigmoidal function at time t.

    Parameters
    ----------
    t : float
        Time at which to evaluate the function
    mu_max : float
        Maximum growth rate of the sigmoidal function
    t_0 : float
        Time at which the growth rate is maximized

    Returns
    -------
    float
        Growth rate of the sigmoidal function at time t
    """

    return mu_max / (1 + exp(mu_max * (t - t_0)))
