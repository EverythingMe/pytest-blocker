from .__version__ import __version__

import pytest


def pytest_configure(config):
    """Register the "run" marker."""

    config_line = (
        'blocker: specify a blocker test. '
        'See also: http://pytest-blocker.readthedocs.org/'
    )
    config.addinivalue_line('markers', config_line)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # get current report status from _pytest.runner.pytest_runtest_makereport
    outcome = yield
    report = outcome.get_result()
    if report.failed and item.get_marker('blocker'):
        skip_reason = "Blocker test {0} failed, skipping remaining tests.".format(item.name)
        for test in item.session.items:
            if test.name != item.name:
                test.add_marker(pytest.mark.skipif(True, reason=skip_reason))
    return report
