from pathlib import Path

import pandas as pd


class DataWrangler:
    def __init__(self):
        self.atm_options_data_folder = Path(__file__).parent / "data" / "raw" / "atm_options"
        self.index_data_path = Path(__file__).parent / "data" / "raw" / "series" / "NIFTY 50_minute.csv"
        self.processed_data_folder = Path(__file__).parent / "data" / "processed"

    def preprocess(self) -> pd.DataFrame:
        # load & pre-process data
        atm_options = self._load_atm_options()
        s = self._load_index_data()
        # TODO: combine series price with atm options data; align on timestamp

        holidays = pd.read_csv(self.processed_data_folder / "holidays.csv")
        # TODO: add boolean 'is_expiry' using holidays
        # TODO: add column for 'days_to_expiry' for the weekly ATM options

        return df

    def _load_atm_options(self) -> pd.DataFrame:
        pass

    def _load_index_data(self) -> pd.Series:
        pass


if "__main__" == __name__:
    worker = DataWrangler()
    df = worker.preprocess()
    print(df)