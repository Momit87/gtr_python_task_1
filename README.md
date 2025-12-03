
# 📈 Alex's Trading Adventure – Golden Cross Strategy

An algorithmic trading simulation built with **Python**, where Alex—an aspiring programmer and finance enthusiast—uses technical indicators to make data-driven trading decisions in the stock market.

This project demonstrates how **Simple Moving Averages (SMA)** can be used to identify **Golden Cross** and **Death Cross** signals to automate buy and sell decisions while managing capital responsibly.

---

## 🧠 Strategy Overview

- **Golden Cross (BUY):**
  - 50-day SMA crosses **above** the 200-day SMA
- **Death Cross (SELL):**
  - 50-day SMA crosses **below** the 200-day SMA
- Only **one open position** is allowed at a time
- Capital constrained by an **initial budget of $5000**
- Any open position is **forcefully closed on the last trading day**

---

## 🛠️ Technologies Used

- **Python 3**
- **yfinance** – for historical stock market data
- **pandas** – data manipulation & cleaning
- **matplotlib** – data visualization
- **math** – position sizing logic

---

## 📂 Project Structure

```

.
├── alex_algo_trader.py   # Main strategy implementation
├── README.md             # Project documentation
└── requirements.txt      # Required Python libraries

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Momit87/gtr_python_task_1.git
cd gtr_python_task_1
````

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install yfinance pandas matplotlib
```

---

## 🚀 How to Run

```bash
python alex_algo_trader.py
```

---

## 🧩 Class Initialization Example

```python
alex_bot = AlexAlgoTrader(
    symbol="AAPL",
    start_date="2018-01-01",
    end_date="2023-12-31"
)
```

---

## 📊 Features Implemented

✅ Download historical stock data
✅ Clean missing & duplicate values
✅ Calculate 50 & 200 day moving averages
✅ Detect Golden Cross & Death Cross
✅ Budget-aware position sizing
✅ Single-position trading logic
✅ Forced position closure at end date
✅ Performance evaluation
✅ Trade visualization with buy/sell markers

---

## 📈 Sample Output

```text
[2019-05-06] BUY  >> 100 shares at $49.77
[2022-06-03] SELL >> Price: $142.78 (Death Cross)
[2023-12-29] SELL >> Price: $190.73 (Force Close)

Final Balance: $16268.62
Return: 225.37%
```

---

## 📉 Visualization

The graph includes:

* **Price** (gray line)
* **50-Day SMA** (blue)
* **200-Day SMA** (red)
* **BUY signal** (green ▲)
* **SELL signal** (red ▼)

This makes trend reversals and trading decisions easy to understand visually.

---

## 🎯 Learning Outcomes

* Practical understanding of technical indicators
* Hands-on experience with financial time-series data
* Class-based approach for flexible strategy design
* Risk-aware capital management
* End-to-end algorithmic trading simulation

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
It does **not** constitute financial or investment advice.

---

## 👤 Author

**Momitul Hoque**
Aspiring Software Engineer | Competitive Programmer | Python Enthusiast


