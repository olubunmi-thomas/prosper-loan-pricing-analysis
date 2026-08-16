import matplotlib.pyplot as plt


def style_plot(
    ax,
    title=None,
    xlabel=None,
    ylabel=None,
    grid=True,
    remove_spines=True,
    title_size=14,
    label_size=11,
    tick_size=9,
    title_weight="bold",
):
    """Apply a consistent presentation style to Matplotlib axes."""
    if title:
        ax.set_title(title, fontsize=title_size, fontweight=title_weight)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=label_size)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=label_size)

    ax.tick_params(axis="both", labelsize=tick_size)

    if grid:
        ax.grid(alpha=0.25, linestyle="--")

    if remove_spines:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    return ax
