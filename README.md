<div align="center">

# Lab-Cycle_2
### Python Data Analysis and Visualization Programs

</div>

A collection of nine Python practical programs covering string processing, numerical computation, Pandas data handling, CSV file operations, and data visualization with Matplotlib.

## Contents

1. [Find a Substring in a Word List](#1-find-a-substring-in-a-word-list)
2. [Automobile Data Analysis](#2-automobile-data-analysis)
3. [Fair Attendance Using Linear Equations](#3-fair-attendance-using-linear-equations)
4. [CSV File Creation and Company Sales Visualization](#4-csv-file-creation-and-company-sales-visualization)
5. [Word Frequency and Sentence Positions](#5-word-frequency-and-sentence-positions)
6. [Student Records Analysis](#6-student-records-analysis)
7. [Technology Innovators CSV Analysis](#7-technology-innovators-csv-analysis)
8. [Sales Data Visualization](#8-sales-data-visualization)
9. [Iris Dataset Analysis](#9-iris-dataset-analysis)

## Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- scikit-learn (for the Iris dataset train/test split)
- Jupyter Notebook (optional)

## Suggested Repository Structure

```text
python-data-analysis-practicals/
├── README.md
├── requirements.txt
├── 01_word_substring/
│   ├── 1.py
│   └── wordlist.txt
├── 02_automobile_analysis/
│   ├── 2.py
│   └── auto-mpg.csv
├── 03_fair_attendance/
│   └── 3.py
├── 04_company_sales/
│   ├── 4.py
│   ├── company.csv
|   └── contributors_table.csv
├── 05_word_frequency/
│   ├── 5.py
│   └── 5.txt
├── 06_student_records/
│   ├── 6.py
│   └── students.csv
├── 07_tech_innovators/
│   ├── 7.py
|   └── tech_innovators.csv
├── 08_sales_visualization/
│   ├── 8.py
│   └── sales_data.csv
├── 09_iris_analysis/
|   ├── 9.py
|   └── iris.csv
```

This is a suggested structure; adjust file and folder names to match your actual repository.

## Installation

Install Python 3 from [python.org](https://www.python.org/downloads/).

Clone your repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Create `requirements.txt` with:

```text
pandas
numpy
matplotlib
scikit-learn
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Programs

### 1. Find a Substring in a Word List

**Goal:** Accept a word list and a search string, then return a tuple containing (1) the number of words containing the string and (2) a list of its position in each word, using `0` when it is absent.

**Input file:** `wordlist.txt`

**Concepts:** Functions, loops, strings, lists, and tuples.

**Note:** The supplied code uses `str.find()` and adds `1` to found positions, making those positions 1-based. If the assignment expects standard Python string indices, return `indx` rather than `indx + 1`.

### 2. Automobile Data Analysis

**Goal:** Use Pandas to read automobile data, update model years, separate company names from car names, list cars by company, and calculate average mileage by company.

**Input file:** `auto.csv` (the supplied code uses `auto-mpg.csv`).

**Expected columns depend on the downloaded dataset.** The supplied code expects columns such as `model year`, `car name`, and `mileage`; a common Auto MPG dataset may instead use names such as `model_year`, `name`, and `mpg`. Adjust the column names to match your file.

**Concepts:** DataFrames, string splitting, grouping, and aggregation.

### 3. Fair Attendance Using Linear Equations

**Goal:** Calculate the numbers of children and adults from the total attendance and ticket revenue.

- Child ticket: ₹1.50
- Adult ticket: ₹4.00
- Total attendees: 2,200
- Total collection: ₹5,050

Equations:

```text
children + adults = 2200
1.50 × children + 4.00 × adults = 5050
```

**Expected result:** 1,500 children and 700 adults.

**Concepts:** Linear equations and NumPy numerical computation.

### 4. CSV File Creation and Company Sales Visualization

**Goal:** Write contributor information to a CSV file and visualize monthly company sales.

Tasks:
- Save Linus Torvalds, Tim Berners-Lee, and Guido van Rossum's details to `contributors_table.csv`.
- Plot monthly toothpaste sales with a scatter plot.
- Compare face cream and face wash sales with a grouped bar chart.
- Show annual sales totals by product in a pie chart.

**Input file:** `company.csv`

**Expected sales columns:** `month_number`, `facecream`, `facewash`, `toothpaste`, `bathingsoap`, `shampoo`, and `moisturizer`.

**Important:** The supplied code uses the same DataFrame for contributor records and company sales. These are separate datasets. Load `company.csv` into a separate DataFrame (for example, `sales_df`) before making the sales charts.

**Concepts:** CSV export, Pandas, and Matplotlib charts.

### 5. Word Frequency and Sentence Positions

**Goal:** Read sentences from `5.txt` and count occurrences of a selected word, create a dictionary of sentence indices and word positions (or `-1` when absent), and list repeated words.

**Input file:** `5.txt`

**Concepts:** File handling, string cleanup, lists, dictionaries, and word counting.

The supplied dictionary function uses 0-based sentence indices and 0-based word positions. It records only the first occurrence of the word in each sentence.

### 6. Student Records Analysis

**Goal:** Use Pandas to remove duplicate records, handle missing or placeholder values, find the highest mark and student for each subject, and calculate average marks grouped by grade.

**Input file:** `students.csv` (the supplied code uses `student_records.csv`).

**Concepts:** Data cleaning, duplicate removal, `idxmax()`, and `groupby()`.

**Important:** Make the CSV filename and column names consistent with the code. Confirm which columns represent subjects before using positional selection such as `df.iloc[:, 5:10]`. Replace missing values based on the dataset's needs; replacing all Boolean values with zero is not a general missing-value strategy.

### 7. Technology Innovators CSV Analysis

**Goal:** Store the innovators dataset in `tech_innovators.csv`, then display innovators whose contribution year is earlier than a user-provided year.

**Fields:** `SN`, `Name`, `Country`, `Innovation`, `Year`

**Concepts:** Pandas, CSV export, Boolean filtering, and user input.

To list innovators before 2000, enter `2000` when prompted.

### 8. Sales Data Visualization

**Goal:** Read `sales_data.csv` and create:
- A line chart of monthly profit.
- A grouped bar chart comparing electronics and clothing sales.
- A pie chart showing yearly totals for electronics, clothing, groceries, and furniture.

**Input file:** `sales_data.csv`

**Concepts:** Pandas, NumPy, and Matplotlib line, bar, and pie charts.

### 9. Iris Dataset Analysis

**Goal:** Load and clean the Iris dataset, split it into training and testing sets using an 80–20 split, display species counts, plot histograms of sepal length and petal length, and show species distribution in a bar chart.

**Expected fields:** `sepal_length`, `sepal_width`, `petal_length`, `petal_width`, and `species`. Column names can differ by source.

**Dataset source:** [UCI Machine Learning Repository – Iris](https://archive.ics.uci.edu/dataset/53/iris). If downloading the CSV manually, place it in the expected folder and update the filename in the code.

**Concepts:** Data cleaning, train/test splitting, class counts, histograms, and bar charts.

## Dataset Notes

- Include the CSV and text files required by your scripts, or provide clear download instructions and source links.
- Keep filenames consistent: the assignment says `auto.csv`, while the supplied code uses `auto-mpg.csv`; the assignment says `students.csv`, while the supplied code uses `student_records.csv`.
- Commit `company.csv`, `sales_data.csv`, `wordlist.txt`, and `5.txt` if they contain no restricted or personal data.
- The contributor and tech-innovator CSV files can be generated by their respective scripts.
- Check dataset licenses and terms before redistributing downloaded datasets.

## Running the Programs

Open a terminal in the folder containing the program and run:

```bash
python main.py
```

Follow the menu prompts where applicable. Matplotlib may open a chart window; close it to return to the program.

If using Jupyter Notebook, open the notebook and run its cells in order.

## Learning Outcomes

These practicals provide experience with:

- Python functions, loops, strings, lists, tuples, and dictionaries.
- Reading and writing text and CSV files.
- Solving linear equations with NumPy.
- Cleaning, grouping, and analyzing data with Pandas.
- Exporting DataFrames to CSV.
- Creating scatter plots, line charts, grouped bar charts, histograms, and pie charts.
- Splitting a dataset for a basic machine-learning workflow.

