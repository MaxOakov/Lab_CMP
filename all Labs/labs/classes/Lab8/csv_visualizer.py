import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

class MockDataVisualizer:
    """
    A class for visualizing and exploring mock data from a CSV file.

    Attributes:
    - df (DataFrame): Pandas DataFrame containing the data.

    Methods:
    - __init__(csv_filepath): Constructor to initialize the object with data from the CSV file.
    - explore_data(): Display minimum and maximum values in the DataFrame.
    - visualize_data(user_choice): Visualize data based on user input.
    - save_plots(fig, filename): Save the given plot as an image.
    - pie_chart(): Generate and display a pie chart of car maker distribution.
    - scatter_plot(): Generate and display a scatter plot of first and last names.
    - bar_chart(): Generate and display a bar chart of the number of occurrences for each car maker.
    - show_all_plots(): Generate and display all three plots (pie chart, scatter plot, bar chart).

    """
    def __init__(self, csv_filepath):
        """
        Constructor to initialize the object with data from the CSV file.

        :param csv_filepath: The path to the CSV file containing mock data.

        """
        self.df = pd.read_csv(csv_filepath)

    def explore_data(self):
        """
        Display minimum and maximum values in the DataFrame.

        """
        min_values = self.df.min()
        max_values = self.df.max()

        print("Min value:")
        print(min_values)

        print("\nMax value:")
        print(max_values)

    def visualize_data(self, user_choice):
        """
        Visualize data based on user input.

        :param user_choice: User's choice for the type of visualization.

        """
        if user_choice == "1":
            self.pie_chart()
        elif user_choice == "2":
            self.scatter_plot()
        elif user_choice == "3":
            self.bar_chart()
        elif user_choice == "4":
            self.show_all_plots()
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

    def save_plots(self, fig, filename):
        """
        Save the given plot as an image.

        :param fig: The Matplotlib or Plotly figure to be saved.
        :param filename: The desired filename for the saved image.

        """
        path = '/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/Lab8'
        full_path = os.path.join(path, filename)
        fig.savefig(full_path)
        print(f"Plot saved at: {full_path}")

    def pie_chart(self):
        """
        Generate and display a pie chart of car maker distribution.

        """
        car_maker_distribution = self.df['car'].value_counts()
        pie_fig, pie_ax = plt.subplots()
        car_maker_distribution.plot(kind='pie', autopct='%1.1f%%', title='Car Maker Distribution', ax=pie_ax)
        self.save_plots(pie_fig, 'pie_chart.png')
        plt.show()

    def scatter_plot(self):
        """
        Generate and display a scatter plot of first and last names.

        """
        scatter_fig, scatter_ax = plt.subplots()
        scatter_ax.scatter(self.df['first_name'], self.df['last_name'], alpha=0.5)
        scatter_ax.set_xlabel('First Name')
        scatter_ax.set_ylabel('Last Name')
        scatter_ax.set_title('Scatter Plot of First and Last Names')
        self.save_plots(scatter_fig, 'scatter_plot.png')
        plt.show()

    def bar_chart(self):
        """
        Generate and display a bar chart of the number of occurrences for each car maker.

        """
        bar_fig, bar_ax = plt.subplots()
        car_maker_counts = self.df['car_maker'].value_counts()
        car_maker_counts.plot(kind='bar', xlabel='Car Maker', ylabel='Count',
                              title='Number of Cars for Each Maker', rot=45, ax=bar_ax)
        self.save_plots(bar_fig, 'bar_chart.png')
        plt.show()

    def show_all_plots(self):
        """
        Generate and display all three plots (pie chart, scatter plot, bar chart).

        """
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))

        # Pie chart
        car_maker_distribution = self.df['car'].value_counts()
        axes[0, 0].pie(car_maker_distribution, autopct='%1.1f%%', labels=car_maker_distribution.index, startangle=90)
        axes[0, 0].set_title('Car Maker Distribution')

        # Scatter plot
        axes[0, 1].scatter(self.df['first_name'], self.df['last_name'], alpha=0.5)
        axes[0, 1].set_xlabel('First Name')
        axes[0, 1].set_ylabel('Last Name')
        axes[0, 1].set_title('Scatter Plot of First and Last Names')

        # Bar chart
        car_maker_counts = self.df['car'].value_counts()
        axes[1, 0].bar(car_maker_counts.index, car_maker_counts)
        axes[1, 0].set_xlabel('Car Maker')
        axes[1, 0].set_ylabel('Count')
        axes[1, 0].set_title('Number of Cars for Each Maker')
        axes[1, 0].tick_params(axis='x', labelrotation=90)

        # Remove empty subplot
        plt.delaxes(axes[1, 1])

        # Adjust spacing between plots
        plt.subplots_adjust(wspace=0.5, hspace=0.5)

        # Save plots as PNG and HTML
        self.save_plots(fig, 'all_plots.png')
        fig = px.scatter(self.df, x='first_name', y='last_name', color='car',
                         title='Scatter Plot of First and Last Names')
        fig.write_html('/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/Lab8/output_plot.html')

        plt.show()
