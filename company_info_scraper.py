import os
import yfinance as yf
import pandas as pd
import json

from mappings import countries


class CompanyInfo:
    def __init__(self) -> None:
        self.data_export_path = self._get_data_export_path()
        os.makedirs(self.data_export_path, exist_ok=True)
        self.company_info_file = f"{self.data_export_path}\\company_info.csv"

    """-----------------------------------"""

    def _get_data_export_path(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        return data["data_export_path"]

    """-----------------------------------"""

    def _get_chrome_driver_path(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        return data["chrome_driver_path"]

    """-----------------------------------"""

    def get_company_info(self, ticker: str):
        """
        Gets the company info by searching via Ticker symbol.

        Parameters
        ----------
        ticker : str
            Ticker symbol of the company

        returns: pd.Series
            Series with the companies information.
        """

        # Ensure that ticker is uppercase.
        ticker = ticker.upper()
        try:
            df = pd.read_csv(self.company_info_file)
            df.set_index("ticker", inplace=True)
            try:
                data = df.loc[ticker]
                return data
            except KeyError:
                df = self._fill_df(ticker, df)
                df.to_csv(self.company_info_file)
                data = df.loc[ticker]
                return data

        except FileNotFoundError:
            df = self._create_and_fill(ticker)
            df.to_csv(self.company_info_file)
            data = df.loc[ticker]
            return data

    def get_company_name(self, ticker: str):
        """
        Gets the name by searching via Ticker symbol.

        Parameters
        ----------
        ticker : str
            Ticker symbol of the company

        returns: str
            Name of the company.
        """

        # Ensure that ticker is uppercase.
        ticker = ticker.upper()
        try:
            df = pd.read_csv(self.company_info_file)
            df.set_index("ticker", inplace=True)
            try:
                data = df.loc[ticker, "name"]
                return data
            except KeyError:
                df = self._fill_df(ticker, df)
                df.to_csv(self.company_info_file)
                data = df.loc[ticker, "name"]
                return data
        except FileNotFoundError:
            df = self._create_and_fill(ticker)
            df.to_csv(self.company_info_file)
            data = df.loc[ticker, "name"]
            return data

    def get_company_sector(self, ticker: str):
        """
        Gets the company sector by searching via Ticker symbol.

        Parameters
        ----------
        ticker : str
            Ticker symbol of the company

        returns: str
            String of the sector.
        """

        # Ensure that ticker is uppercase.
        ticker = ticker.upper()
        try:
            df = pd.read_csv(self.company_info_file)
            df.set_index("ticker", inplace=True)
            try:
                data = df.loc[ticker, "sector"]
                return data
            except KeyError:
                df = self._fill_df(ticker, df)
                df.to_csv(self.company_info_file)
                data = df.loc[ticker, "sector"]
                return data
        except FileNotFoundError:
            df = self._create_and_fill(ticker)
            df.to_csv(self.company_info_file)
            data = df.loc[ticker, "sector"]
            return data

    def get_company_industry(self, ticker: str):
        """
        Gets the company industry by searching via Ticker symbol.

        Parameters
        ----------
        ticker : str
            Ticker symbol of the company

        returns: str
            String of the industry.
        """

        # Ensure that ticker is uppercase.
        ticker = ticker.upper()
        try:
            df = pd.read_csv(self.company_info_file)
            df.set_index("ticker", inplace=True)
            try:
                data = df.loc[ticker, "industry"]
                return data
            except KeyError:
                df = self._fill_df(ticker, df)
                df.to_csv(self.company_info_file)
                data = df.loc[ticker, "industry"]
                return data
        except FileNotFoundError:
            df = self._create_and_fill(ticker)
            df.to_csv(self.company_info_file)
            data = df.loc[ticker, "industry"]
            return data

    def get_company_country(self, ticker: str):
        """
        Gets the company country by searching via Ticker symbol.

        Parameters
        ----------
        ticker : str
            Ticker symbol of the company

        returns: str
            String of the country.
        """

        # Ensure that ticker is uppercase.
        ticker = ticker.upper()
        try:
            df = pd.read_csv(self.company_info_file)
            df.set_index("ticker", inplace=True)
            try:
                data = df.loc[ticker, "country"]
                return data
            except KeyError:
                df = self._fill_df(ticker, df)
                df.to_csv(self.company_info_file)
                data = df.loc[ticker, "country"]
                return data
        except FileNotFoundError:
            df = self._create_and_fill(ticker)
            df.to_csv(self.company_info_file)
            data = df.loc[ticker, "sector"]
            return data

    """-----------------------------------"""

    def _create_and_fill(self, ticker: str):
        """
        Create an empty dataframe and fill the first row with information.

        Parameters
        ----------
        ticker : str
            Ticker symbol of the company

        returns: pandas.DataFrame
            Dataframe with relevant information.
        """

        cols = ["ticker", "name", "sector", "industry", "country"]
        df = pd.DataFrame(columns=cols)
        df.set_index("ticker", inplace=True)
        df = self._fill_df(ticker, df)
        return df

    """-----------------------------------"""

    def _fill_df(self, ticker: str, df: pd.DataFrame):
        """
        Insert data into dataframe passed in the function parameter.

        Parameters
        ----------
        ticker : str
            Ticker symbol of the company

        df : pandas.DataFrame
            Dataframe to be filled with relevant information.
        returns: pandas.DataFrame
            Dataframe with relevant information.
        """
        data = self._fetch_external_data(ticker)
        df.loc[ticker, "name"] = data["name"]
        df.loc[ticker, "sector"] = data["sector"]
        df.loc[ticker, "industry"] = data["industry"]
        df.loc[ticker, "country"] = data["country"]
        return df

    """-----------------------------------"""

    def _fetch_external_data(self, ticker: str):
        """
        Query company info from yahoo finance

        Parameters
        ----------
        ticker : str
            Ticker of the company to search.

        returns: dict
            Dictionary with data related to the company.
        """
        yf_data = yf.Ticker(ticker).info
        # Company Name
        name = yf_data["longName"]
        # Sector
        sector = yf_data["sector"]
        # Industry
        industry = yf_data["industry"]
        # Country
        country = yf_data["country"]
        if country in countries:
            country = countries[country]
        return {
            "ticker": ticker,
            "name": name,
            "sector": sector,
            "industry": industry,
            "country": country,
        }

    def view(self):
        print(f"Path: {self.company_info_file}")
        df = pd.read_csv(self.company_info_file)
        df.set_index("ticker", inplace=True)
        print(f"DF: {df}")


if __name__ == "__main__":

    ci = CompanyInfo()
    ci.get_company_info("AAPL")
