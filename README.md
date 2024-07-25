![App Screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCf0eXZ8ieW20or45rwqnhKafHLa9bkTT0Cfh5CDI0-f57u9V04VUcOTLxCCvzMBRjeXOvoNw-qoPdPQI6SNZ0rCA4YimLQqsMWrfT2gzcg8k91_K8NLxXTr2MzCJT47eD6Jniy7K8RvHAb_ThfLFVPl0dqwcLTzak2EOYX4WZ89Ymwzc12aY6msogOhpn/s1239/Screenshot%202024-07-25%20213909.png)

<div align="center">
https://indonbs-football-sty.streamlit.app
</div>

<br>
This Streamlit app analyzes public sentiment on comments about the Indonesian national football team during Shin Tae-yong’s tenure, using a Naive Bayes algorithm. It aims to evaluate how people feel about the team's performance and give insights into their perception of the coach.

## Features

- Sentiment analysis of comments using the Naive Bayes algorithm.
- Visualization of the analysis results.

## Local Installation

Clone this repository:

```bash
  git clone https://github.com/fmjawahir/indonbs-football-sty.git
```

Navigate to the project directory:

```bash
  cd indonbs-football-sty
```

Create and activate a virtual environment (optional but recommended):

```bash
  python -m venv venv
  source venv/Scripts\activate
```

Install the required dependencies:

```bash
  pip install -r requirements.txt
```

Run streamlit app:

```bash
  streamlit run app.py
```

## Datasets

The dataset for this project contains comments from Indonesian fans about the national football team during Shin Tae-yong's time as coach. It’s pulled from [Kaggle](https://www.kaggle.com/datasets/pajarbebek/analisis-sentimen-timnas-sepakbola-di-era-sty) and features comments labeled as either positive or negative. This work is by Fajar Ramadhan.

## License

Proyek ini dilisensikan di bawah [MIT](https://choosealicense.com/licenses/mit/) License.
