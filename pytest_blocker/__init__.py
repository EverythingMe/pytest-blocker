from .__version__ import __version__

import pytest


def pytest_configure(config):
    """Register the "run" marker."""

    config_line = (
        'blocker: specify a blocker test. '
        'See also: http://pytest-blocker.readthedocs.org/'
    )
    config.addinivalue_line('markers', config_line)


def pytest_runtest_makereport(item, call, __multicall__):
    # get current report status from _pytest.runner.pytest_runtest_makereport
    report = __multicall__.execute()
    if report.failed and item.get_marker('blocker'):
        skip_reason = "Blocker test {0} failed, skipping remaining tests.".format(item.name)
        for test in item.session.items:
            if test.name != item.name and test._request:
                test._request.applymarker(pytest.mark.skipif(True, reason=skip_reason))
    return report
