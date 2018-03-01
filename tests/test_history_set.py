import pytest

from history_set import HistorySet


@pytest.fixture(scope="function")
def history_set():
    yield HistorySet([1, 2, 3])


def test_add(history_set):
    history_set.add(4)
    assert (history_set.added() == {4})
    assert (history_set == {1, 2, 3, 4})


def test_remove(history_set):
    history_set.remove(3)
    assert (history_set.removed() == {3})
    assert (history_set == {1, 2})

def test_remove_not_exist(history_set):
    with pytest.raises(KeyError):
        history_set.remove(5)

def test_reset(history_set):
    history_set.add(4)
    assert (history_set.added() == {4})

    history_set.remove(2)
    assert (history_set.removed() == {2})

    history_set.reset()
    assert (history_set.added() == set())
    assert (history_set.removed() == set())
    assert (history_set == {1, 3, 4})

def test_added_reset(history_set):
    history_set.add(4)
    assert (history_set.added() == {4})

    history_set.remove(2)
    assert (history_set.removed() == {2})

    history_set.reset(added=True)
    assert (history_set.added() == set())
    assert (history_set.removed() == {2})

def test_removed_reset(history_set):
    history_set.add(4)
    assert (history_set.added() == {4})

    history_set.remove(2)
    assert (history_set.removed() == {2})

    history_set.reset(removed=True)
    assert (history_set.added() == {4})
    assert (history_set.removed() == set())

def test_non_eidetic():
    history_set = HistorySet([1, 2, 3], eidetic=True)
    history_set.add(4)
    history_set.remove(4)
    assert (history_set.added() == {4})
    assert (history_set.removed() == {4})

def test_atomic(history_set):
    history_set.add(4)
    assert (history_set.added() == {4})
    assert (history_set.removed() == set())
    history_set.remove(4)
    assert (history_set.added() == set())
    assert (history_set.removed() == set())
