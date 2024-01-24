import numpy.testing


def assert_allclose(actual, desired, msg=None):
    """
    Raises an AssertionError if two objects are not equal up to a default tolerance.

    Parameters
    ----------
    actual :
        Object to test.
    desired :
        Reference object to compare against.
    """
    try:
        numpy.testing.assert_allclose(actual=actual, desired=desired, err_msg=msg)
    except TypeError:
        assert actual == desired, msg
