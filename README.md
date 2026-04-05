# Summary
This work uses Mandelbrot-inspired volatility and roughness features, paired with Lorentzian-distance similarity and k-nearest neighbors, to make next-minute (up, down or flat) predictions for ATM NIFTY weekly calls and puts. 
Performance of the predictions is also compared to standard benchmark models.

## Motivation
Market participants trade weekly ATM NIFTY options in massive volumes across India, but predicting their next-minute direction remains a tough challenge. When short-term forecasts fail, practitioners face mistimed entries, poor intraday hedging, weak risk management, and unreliable trading signals. Standard models rely on basic distance metrics or smooth assumptions. These conventional methods struggle to process outliers, sudden regime shifts, or clustered volatility.

This project explores whether fractal-based features and Lorentzian similarity can provide an edge in forecasting ultra-short-term option price movement. Comparison with basic benchmarks like persistence, logistic regression, and Euclidean kNN are done for reference/baseline.

## Data
- Instrument universe: NIFTY index, ATM weekly NIFTY calls, and ATM weekly NIFTY puts traded on the National Stock Exchange of India.
- Frequency: 1-minute OHLC data.
- Prediction horizon: Next 1 minute.
