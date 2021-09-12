"""
Functions with MATLAB-compatible signatures.
"""
from matlab2py.handles import FigureHandlesArray, FigureHandle

# All of the figure handles.
HANDLES = FigureHandlesArray()
groot = HANDLES[0]


def axes(fig):
    """Add an axes to fig."""
    fig.add_axes()


def figure(*args):
    """
    Create a new figure or make an existing one current.

    Mirrors: matlab.ui.figure

    Signatures:
    figure()
    figure(handle)
    figure(number)
    figure(name, value, ...)
    f = figure(___)
    """
    if not args:
        return HANDLES.make_new_figure()

    elif len(args) == 1:
        if isinstance(args[0], int):
            # Find figure with number int or make a new one.
            try:
                HANDLES.current_fig = args[0]
                return HANDLES[args[0]]
            except (KeyError, AssertionError):
                return HANDLES.make_new_figure(number=args[0])

        elif isinstance(args[0], FigureHandle):
            # Make that figure the current figure and bring to front.
            HANDLES.current_fig = args[0].Number
            return args[0]

    elif len(args) % 2 == 0:
        # We've got name-value pairs.
        assert(all(isinstance(x, str) for x in args[::2]))
        return HANDLES.make_new_figure(
            properties={
                name: value for name, value in zip(args[0::2], args[1::2])
            },
        )

    else:
        # Error?
        ValueError("Invalid number of arguments.")


def gca():
    """Return the current axes."""
    return gcf().current_child


def gcf():
    """Return the current figure."""
    return HANDLES.current_fig


def plot(ax, x, y):
    """Plot """
    return ax._plot(x, y)
