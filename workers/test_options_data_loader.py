from options_data_loader import OptionsDataLoader


def test_find_available_data_dates():
    loader = OptionsDataLoader()
    data_dates = loader.find_available_data_dates()
    print(f"{len(data_dates)=}")
    # print(data_dates)
    assert len(data_dates) > 0


def test_process_options_data_for_a_given_date():
    loader = OptionsDataLoader()
    data_dates = loader.find_available_data_dates()
    due_date = data_dates[0]
    df = loader.process_options_data_for_a_given_date(due_date)
    print(df.head())
    print(df.columns)
    print(df.info())
    assert len(df) > 0
    assert df.columns.tolist() == ['DateTime', 'Right', 'Open', 'High', 'Low', 'Close', 'Strike', 'Date']
    assert df['DateTime'].dtype == 'datetime64[ns]'
    assert df['Right'].dtype == 'object'
    assert df['Open'].dtype == 'float64'
    assert df['High'].dtype == 'float64'
    assert df['Low'].dtype == 'float64'
    assert df['Close'].dtype == 'float64'
    assert df['Strike'].dtype == 'int64'

