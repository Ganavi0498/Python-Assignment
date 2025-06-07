# src/visualizer.py

from bokeh.plotting import figure, output_file, save

class Visualizer:
    """
    Uses Bokeh to plot:
    - Training vs. chosen ideal functions
    - Test points mapped onto these functions
    """
    def __init__(self, train_df, ideal_df, selections):
        self.train_df = train_df
        self.ideal_df = ideal_df
        self.selections = selections

    def plot_training(self, out_html="train_vs_ideal.html"):
        p = figure(
            title="Training vs. Ideal Functions",
            x_axis_label="x",
            y_axis_label="y"
        )
        # plot each train curve and its chosen ideal
        for train_col, ideal_col in self.selections.items():
            p.line(
                self.train_df["x"],
                self.train_df[train_col],
                legend_label=f"Train {train_col}",
                line_width=2
            )
            p.line(
                self.ideal_df["x"],
                self.ideal_df[ideal_col],
                legend_label=f"Ideal {ideal_col}",
                line_dash="dashed"
            )
        output_file(out_html)
        save(p)

    def plot_test_mapping(self, test_map_df, out_html="test_mapping.html"):
        p = figure(
            title="Test Points Mapped to Ideal Functions",
            x_axis_label="x",
            y_axis_label="y"
        )
        # use scatter() instead of circle() with size to avoid deprecation warning
        p.scatter(
            "x",
            "y",
            source=test_map_df,
            marker="circle",
            size=6,
            color="red"
        )
        output_file(out_html)
        save(p)
