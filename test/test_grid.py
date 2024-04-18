from ..grid import Grid
import pytest

def test_grid_fill():
    g = Grid(10, 10)
    n_filled = 0

    for w in range(g.width()):

        for h in range(g.height()):
            n_filled += 1
            g.fill(w, h)
            assert g.nFilled() == n_filled
            assert g.cell(w, h).occupied()

            g.fill(w, h)

            assert g.nFilled() == n_filled


def test_grid_empty():
    g = Grid(10, 10)

    for w in range(g.width()):
    
        for h in range(g.height()):
            g.fill(w, h)
            assert g.nFilled() == 1
            assert g.cell(w, h).occupied()

            g.empty(w, h)

            assert g.nFilled() == 0

            assert not g.cell(w, h).occupied()


