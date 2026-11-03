import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def create_visualizations():

    # Load dataset
    data = pd.read_csv("dataset.csv")

    # Create charts folder if it doesn't exist
    os.makedirs("charts", exist_ok=True)

    # -----------------------------
    # Bar Chart
    # -----------------------------

    plt.figure(figsize=(8, 5))

    data["Disease"].value_counts().plot(
        kind="bar",
        color="skyblue"
    )

    plt.title("Disease Count")
    plt.xlabel("Disease")
    plt.ylabel("Count")
    plt.tight_layout()

    plt.savefig(
        "charts/bar_chart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    # -----------------------------
    # Pie Chart
    # -----------------------------

    plt.figure(figsize=(7, 7))

    data["Disease"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Disease Distribution")
    plt.ylabel("")
    plt.tight_layout()

    plt.savefig(
        "charts/pie_chart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    # -----------------------------
    # Heatmap
    # -----------------------------

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        data.iloc[:, 0:6].corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Symptom Correlation HeatMap")
    plt.tight_layout()

    plt.savefig(
        "charts/heatmap.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


if __name__ == "__main__":
    create_visualizations()