import yfinance as yf

class Portfolio:
    def __init__(self, default_exchange_suffix=".NS"):
        # Dictionary to store stocks with ticker as key and number of shares as value
        self.stocks = {}
        # Default suffix to append if the ticker symbol does not include an exchange suffix.
        self.default_exchange_suffix = default_exchange_suffix

    def format_ticker(self, ticker):
        """
        Formats the ticker to include the exchange suffix if it's not already present.
        For Indian stocks, the default suffix is .NS (for NSE).
        """
        ticker = ticker.strip().upper()
        # If ticker already ends with a recognized suffix, leave it unchanged.
        if ticker.endswith(".NS") or ticker.endswith(".BO"):
            return ticker
        # Otherwise, append the default suffix.
        return ticker + self.default_exchange_suffix

    def add_stock(self, ticker, shares):
        formatted_ticker = self.format_ticker(ticker)
        if formatted_ticker in self.stocks:
            self.stocks[formatted_ticker] += shares
        else:
            self.stocks[formatted_ticker] = shares
        print(f"Added {shares} shares of {formatted_ticker} to your portfolio.")

    def remove_stock(self, ticker, shares):
        formatted_ticker = self.format_ticker(ticker)
        if formatted_ticker in self.stocks:
            if self.stocks[formatted_ticker] >= shares:
                self.stocks[formatted_ticker] -= shares
                print(f"Removed {shares} shares of {formatted_ticker} from your portfolio.")
                # Remove ticker if no shares remain
                if self.stocks[formatted_ticker] == 0:
                    del self.stocks[formatted_ticker]
            else:
                print("You do not have enough shares to remove.")
        else:
            print("Stock not found in your portfolio.")

    def get_stock_price(self, ticker):
        """
        Retrieve the current stock price using yfinance.
        """
        formatted_ticker = self.format_ticker(ticker)
        try:
            stock = yf.Ticker(formatted_ticker)
            # Retrieve today's market data
            data = stock.history(period="1d")
            if data.empty:
                print(f"Could not retrieve data for {formatted_ticker}.")
                return None
            # Use the 'Close' price as the current price
            current_price = data['Close'][0]
            return current_price
        except Exception as e:
            print("Error retrieving stock data:", e)
            return None

    def track_portfolio(self):
        print("\n=== Portfolio Performance ===")
        total_value = 0.0
        if not self.stocks:
            print("Your portfolio is currently empty.")
        else:
            for ticker, shares in self.stocks.items():
                price = self.get_stock_price(ticker)
                if price is not None:
                    stock_value = price * shares
                    total_value += stock_value
                    print(f"{ticker}: {shares} shares @ ₹{price:.2f} each = ₹{stock_value:.2f}")
                else:
                    print(f"Skipping {ticker} due to data retrieval issues.")
            print(f"Total Portfolio Value: ₹{total_value:.2f}")
        print("=============================\n")

def main():
    print("Welcome to the Indian Stock Portfolio Tracking Tool!")
    print("By default, tickers will be treated as NSE stocks (suffix '.NS').")
    portfolio = Portfolio()

    while True:
        print("\n=== Portfolio Menu ===")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio Performance")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            ticker = input("Enter stock ticker (e.g., RELIANCE.NS for NSE or RELIANCE.BO for BSE): ").strip()
            try:
                shares = float(input("Enter number of shares to add: "))
                portfolio.add_stock(ticker, shares)
            except ValueError:
                print("Invalid number of shares. Please enter a numeric value.")
        elif choice == '2':
            ticker = input("Enter stock ticker (e.g., RELIANCE for NSE or RELIANCE.BO for BSE): ").strip()
            try:
                shares = float(input("Enter number of shares to remove: "))
                portfolio.remove_stock(ticker, shares)
            except ValueError:
                print("Invalid number of shares. Please enter a numeric value.")
        elif choice == '3':
            portfolio.track_portfolio()
        elif choice == '4':
            print("Exiting the Portfolio Tracking Tool. Goodbye!")
            break
        else:
            print("Invalid choice, please select an option between 1 and 4.")

if __name__ == '__main__':
    main()
