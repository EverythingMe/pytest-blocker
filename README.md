pytest-blocker
==============

pytest plugin to mark a test as blocker and skip all tests after it upon failure.

Install with:

    pip install pytest-blocker

Usage:

    import pytest

    @pytest.mark.blocker
    def test_foo():
        assert True==False

    def test_bar():
        assert True

Yields this output:

    $ py.test -sv test_foo.py
    ===================================== test session starts ======================================
    platform darwin -- Python 2.7.10 -- py-1.4.30 -- pytest-2.7.10 -- /usr/bin/python
    plugins: blocker
    collected 2 items

    test_foo.py::test_foo FAILED
    test_foo.py::test_bar SKIPPED

    =========================================== FAILURES ===========================================
    ___________________________________________ test_foo ___________________________________________

        @pytest.mark.blocker
        def test_foo():
    >       assert True==False
    E       assert True == False

    test_foo.py:5: AssertionError
    =================================== short test summary info ====================================
    SKIP [1] test_foo.py:6: Blocker test test_foo failed, skipping remaining tests.
    ============================= 1 failed, 1 skipped in 0.01 seconds ==============================