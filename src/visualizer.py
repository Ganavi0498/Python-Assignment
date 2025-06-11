from bokeh.plotting import figure, output_file, save
from bokeh.palettes import Category10

class Visualizer:
    """
    Uses Bokeh to plot:
    - Training functions alone
    - Ideal functions alone
    - Test points mapped onto the model
    """
    def __init__(self, train_df, ideal_df, selections):
        self.train_df  = train_df
        self.ideal_df  = ideal_df
        self.selections = selections

    def plot_train_curves(self, out_html="train_curves.html"):
        palette = Category10[len(self.selections)]
        p = figure(
            title="Training Functions",
            x_axis_label="x",
            y_axis_label="y",
            width=800, height=400
        )

        for idx, train_col in enumerate(self.selections):
            color = palette[idx % len(palette)]
            p.line(
                self.train_df["x"],
                self.train_df[train_col],
                legend_label=f"Train {train_col}",
                line_width=2,
                color=color
            )

        p.legend.location     = "top_left"
        p.legend.click_policy = "hide"

        output_file(out_html)
        save(p)

    def plot_ideal_curves(self, out_html="ideal_curves.html"):
        palette = Category10[len(self.selections)]
        p = figure(
            title="Ideal Functions",
            x_axis_label="x",
            y_axis_label="y",
            width=800, height=400
        )

        for idx, ideal_col in enumerate(self.selections.values()):
            color = palette[idx % len(palette)]
            p.line(
                self.ideal_df["x"],
                self.ideal_df[ideal_col],
                legend_label=f"Ideal {ideal_col}",
                line_dash="dashed",
                line_width=2,
                color=color
            )

        p.legend.location     = "top_left"
        p.legend.click_policy = "hide"

        output_file(out_html)
        save(p)

    def plot_test_mapping(self, test_map_df, out_html="test_mapping.html"):
        p = figure(
            title="Test Points Mapped to Ideal Functions",
            x_axis_label="x",
            y_axis_label="y",
            width=800, height=400
        )
        p.scatter(
            "x",
            "y",
            source=test_map_df,
            marker="circle",
            size=6,
            color="red",
            legend_label="Test points"
        )
        p.legend.location     = "top_left"
        p.legend.click_policy = "hide"

        output_file(out_html)
        save(p)
