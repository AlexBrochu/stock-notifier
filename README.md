# stock-notifier

## Info
This simple project takes in input an array of stocks with the price you paid and trigger notification when price limit-buy is hit. It will peridically (each 10 seconds) fetch the current price for a stock and update the output folder with different portfolio stats. 

* Percentage for each sectors 
* Portfolio total value for each sector and overall value

## Setup
1. To install dependencies
`pip install -r requirements.txt`

2. Complete json file with your stocks in the input folder
`
{
    "stocks": [
        {
            "name": "ABT.TO",
            "quantity": 11,
            "avg_price": 15.16, 
            "limit-buy": 13.5,
            "limit-sell": 18
        },
        ...
    ]
}
`

3. Run main.py

## TODO
* Add support for TSX Venture stock
* Add notification when there is a dividend
* Add commandline options