from .queriers import ClusterQuerier
from .queriers import MaxQuerier
from .queriers import MaxRandomQuerier
from .queriers import MaxUncertaintyQuerier
from .queriers import MixedQuerier
from .queriers import RandomQuerier
from .queriers import UncertaintyQuerier
from importlib.metadata import entry_points


def list_queriers():
    my_queriers = {q.name: q for q in [
        ClusterQuerier,
        MaxQuerier,
        MaxRandomQuerier,
        MaxUncertaintyQuerier,
        MixedQuerier,
        RandomQuerier,
        UncertaintyQuerier
    ]}
    try:
        other_queriers = {e.name: e.load() for e in entry_points(group="asreviewlib.queriers")}
    except Exception as e:
        print("Something went wrong loading a module from entrypoint group " +
              f"'asreviewlib.queriers'. The error message was: {e}\nContinuing...")
        other_queriers = {}
    d = dict()
    d.update(my_queriers)
    d.update(other_queriers)
    return dict(sorted(d.items()))
