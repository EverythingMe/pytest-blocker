pytest-blocker
==============

pytest plugin to mark a test as blocker and skip all tests after it

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

    $ py.test test_foo.py -vv
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2 -- env/bin/python
    plugins: blocker
    collected 2 items

    test_foo.py:3: test_foo FAILED
    test_foo.py:7: test_bar SKIPPED

    ====================== 1 failed, 1 skipped in 0.01 seconds =====================
