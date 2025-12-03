import yfinance as yf
import pandas as pd
import math
import matplotlib.pyplot as plt

class AlexAlgoTrader:
    def __init__(self, symbol, start_date, end_date, initial_budget=5000):
        self.symbol = symbol
        self.start = start_date
        self.end = end_date
        self.budget = initial_budget
        self.cash = initial_budget
        self.shares = 0
        self.history = []
        self.data = None

    def fetch_and_clean_data(self):
        print(f"--- Alex is fetching data for {self.symbol} ---")
        df = yf.download(self.symbol, start=self.start, end=self.end, progress=False)
        if df.empty:
            raise ValueError("No data found.")
        df = df.drop_duplicates()
        df = df.ffill()
        self.data = df
        print(f"Data acquired successfully! ({len(df)} rows)")

    def calculate_indicators(self):
        if self.data is None: return
        self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()
        self.data['SMA_200'] = self.data['Close'].rolling(window=200).mean()
        self.data = self.data.dropna()

    def execute_strategy(self):
        print("\n--- Alex is starting the simulation ---")
        in_position = False
        dates = self.data.index
        closes = self.data['Close']
        sma_50 = self.data['SMA_50']
        sma_200 = self.data['SMA_200']

        for i in range(1, len(self.data)):
            current_date = dates[i]
            price = float(closes.iloc[i])
            
            # Check for crossover
            curr_50, curr_200 = sma_50.iloc[i], sma_200.iloc[i]
            prev_50, prev_200 = sma_50.iloc[i-1], sma_200.iloc[i-1]

            # BUY SIGNAL (Golden Cross)
            if not in_position and prev_50 <= prev_200 and curr_50 > curr_200:
                self.buy(current_date, price)
                in_position = True

            # SELL SIGNAL (Death Cross)
            elif in_position and prev_50 >= prev_200 and curr_50 < curr_200:
                self.sell(current_date, price, reason="Death Cross")
                in_position = False

        # Force Close
        if in_position:
            self.sell(dates[-1], float(closes.iloc[-1]), reason="Force Close")

    def buy(self, date, price):
        num_shares = math.floor(self.cash / price)
        if num_shares > 0:
            cost = num_shares * price
            self.cash -= cost
            self.shares = num_shares
            self.history.append({'Type': 'BUY', 'Date': date, 'Price': price})
            print(f"[{date.date()}] BUY  >> {num_shares} shares at ${price:.2f}")

    def sell(self, date, price, reason):
        revenue = self.shares * price
        self.cash += revenue
        self.shares = 0
        self.history.append({'Type': 'SELL', 'Date': date, 'Price': price})
        print(f"[{date.date()}] SELL >> Price: ${price:.2f} ({reason})")

    def evaluate_performance(self):
        total_value = self.cash
        return_pct = ((total_value - self.budget) / self.budget) * 100
        print(f"\nFinal Balance: ${total_value:.2f} (Return: {return_pct:.2f}%)")

    # VISUALIZATION 
    def visualize_trade(self):
        """
        Plots the Price, SMAs, and Buy/Sell markers.
        """
        plt.figure(figsize=(14, 7))
        
        # 1. Plot Price and Averages
        plt.plot(self.data.index, self.data['Close'], label='Price', color='black', alpha=0.3)
        plt.plot(self.data.index, self.data['SMA_50'], label='SMA 50', color='blue', alpha=0.7)
        plt.plot(self.data.index, self.data['SMA_200'], label='SMA 200', color='red', alpha=0.7)

        # 2. Plot Buy/Sell Markers
        # We separate buys and sells to give them different colors/markers
        buy_dates = [x['Date'] for x in self.history if x['Type'] == 'BUY']
        buy_prices = [x['Price'] for x in self.history if x['Type'] == 'BUY']
        
        sell_dates = [x['Date'] for x in self.history if x['Type'] == 'SELL']
        sell_prices = [x['Price'] for x in self.history if x['Type'] == 'SELL']

        # Scatter plot for markers
        plt.scatter(buy_dates, buy_prices, marker='^', color='green', s=100, label='Buy Signal', zorder=5)
        plt.scatter(sell_dates, sell_prices, marker='v', color='red', s=100, label='Sell Signal', zorder=5)

        # 3. Formatting
        plt.title(f"Alex's Trading Adventure: {self.symbol} Golden Cross Strategy")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    alex_bot = AlexAlgoTrader("AAPL", "2018-01-01", "2023-12-31")
    alex_bot.fetch_and_clean_data()
    alex_bot.calculate_indicators()
    alex_bot.execute_strategy()
    alex_bot.evaluate_performance()
    alex_bot.visualize_trade()
