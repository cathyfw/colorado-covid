import pandas
import csv
import datetime


class DataSource:
    __instance = None

    @staticmethod
    def get_instance(*args, **kwargs):
        """ Use this method to get the singleton, then use DataSource.get_dataframe to get the df """
        if DataSource.__instance is None:
            DataSource(*args, **kwargs)
        return DataSource.__instance

    def __init__(self):
        """ This is a private constructor, do not call it """
        self.download_new_csv()
        self.df = self.make_dataframe()
        pass

    def get_dataframe(self) -> pandas.DataFrame:
        """ return dataframe if it exists and is valid, otherwise make a new one and return it. """
        if self.df and self.check_date():
            return self.df
        else:
            self.download_new_csv()
            self.df = self.make_dataframe()
            return self.df

    def make_dataframe(self) -> pandas.DataFrame:
        """ Make a dataframe from the csv and return it. """
        pass

    def check_date(self) -> bool:
        """ make sure the last date in the dataframe is within the last 2 days, return true if so """
        pass

    def download_new_csv(self):
        """ download the csv, check that the schema is valid """
        pass
