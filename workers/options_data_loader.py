import glob
import pprint as pp

import pandas as pd


class OptionsDataLoader:
    def __init__(self):
        self.atm_options_data_path = 'data/raw/atm_options'
        self.series_data_path = 'data/raw/series'
        self.available_data_dates = self.find_available_data_dates()

    def process_options_data(self):
        df = pd.DataFrame()
        # for date in self.available_data_dates[:408]:  # data with basic columns
        # for date in self.available_data_dates[409:]:  # data with basic & processed/additional columns
        for date in self.available_data_dates:
            df_ = self.process_options_data_for_a_given_date(date)
            df = pd.concat([df, df_])
        print(df.head())
        print(df.info())
        print(df.describe())
        return df

    def process_options_data_for_a_given_date(self, date: str):
        if date not in self.available_data_dates:
            print(f"Data on {date=} is not available")
            return None
        folder_path = f"{self.atm_options_data_path}/{date}"

        call_data_file = f"{folder_path}/ATM_CALL.csv"
        call_data = pd.read_csv(call_data_file, parse_dates=['DateTime'])
        call_data['Right'] = 'CALL'
        # print(call_data.head())

        put_data_file = f"{folder_path}/ATM_PUT.csv"
        put_data = pd.read_csv(put_data_file, parse_dates=['DateTime'])
        put_data['Right'] = 'PUT'
        # print(put_data.head())

        df_ = pd.concat([call_data, put_data])
        keep_cols = ['DateTime', 'Right', 'Open', 'High', 'Low', 'Close', 'Strike']
        df_ = df_[keep_cols]
        # df_['Date'] = pd.to_datetime(date)
        df_['Date'] = date
        # print(df_.head())
        # print(df_.info())
        # print(df_.describe())
        return df_

    def find_available_data_dates(self) -> list[str]:
        folders = glob.glob(f'{self.atm_options_data_path}/*')
        available_dates = [f.split('/')[-1] for f in folders]
        available_dates.sort()
        return available_dates


if __name__ == "__main__":
    print(f"\n\n{'=' * 20} RUNNING DATA PROCESSOR {'=' * 20}")
    worker = OptionsDataLoader()

    dates = worker.find_available_data_dates()
    pp.pprint(dates)
    print(f"{len(dates)=}")

    # processor.process_options_data_for_a_given_date('2024-03-26')
    worker.process_options_data()
