# Letterboxd Viewing Habits Analysis

This project explores film-watching habits using data exported from [Letterboxd](https://letterboxd.com/). The analysis includes:

- **Monthly viewing trends** across multiple years  
- **Heatmap of average ratings and viewing frequency**  
- **Temporal trend of rating behavior over time**

The data was extracted and saved as csv using a custom scraper:  
[`letterboxd_diary.py`](https://github.com/Carbonard/python-exercises-collection/blob/main/scraping-projects/letterboxd/letterboxd_diary.py)  
and analyzed using:  
[`films_analysis.py`](https://github.com/Carbonard/python-exercises-collection/blob/main/data-analysis/letterboxd-analysis-pandas/films_analysis.py)

📄 **Full PDF report:** [`letterboxd-analysis-report.pdf`](https://github.com/Carbonard/python-exercises-collection/blob/main/data-analysis/letterboxd-analysis-pandas/letterboxd-analysis-report.pdf)

## 🛠️ Tech Stack

| Component           | Technologies Used                         |
|---------------------|-------------------------------------------|
| **Data Extraction** | Python, Requests, BeautifulSoup           |
| **Data Analysis**   | Pandas, NumPy                             |
| **Visualization**   | Matplotlib, Seaborn                       |
| **Reporting**       | LaTeX                                     |

## 📁 Project Structure

```
python-exercises-collection/
├── data-analysis/
│   └── letterboxd-analysis/
│       ├── data/
│       │   └── sample_diary.csv
│       ├── outputs/
│       │   ├── sample_diary_heatmap.png
│       │   ├── sample_diary_plotline.png
│       │   └── sample_diary_plotlines.png
│       ├── films-analysis-report.pdf
│       ├── films_analysis.py
│       └── README.md
├── scraping-projects/
│   └── Letterboxd/
│       └── letterboxd_diary.py
```
