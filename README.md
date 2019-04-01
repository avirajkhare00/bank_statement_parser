# bank_statement_parser

## Packages used
 - [camelot](https://github.com/socialcopsdev/camelot)

## Setup
 - Install virtualenv
 - install packages from requirements.txt
 - Install following packages: `brew install tcl-tk ghostscript`
 - place pdf file inside files directory
 - edit script.py and give path to filename
 - run script.py
 
 It will generate following output
 
 ```
 [
  {
    "0": "Tran Date\nChq No",
    "1": "",
    "2": "Particulars\nDebit\nCredit",
    "3": "",
    "4": "",
    "5": "Balance",
    "6": "Init.\nBr"
  },
  {
    "0": "",
    "1": "",
    "2": "OPENING BALANCE",
    "3": "",
    "4": "",
    "5": ".00",
    "6": ""
  },
  {
    "0": "28-03-2019",
    "1": "",
    "2": "NEFT/ICMS190328001NKV/LIC OF INDIA\nSATNA MADHYA PR",
    "3": "",
    "4": "60000.00",
    "5": "60000.00",
    "6": "002"
  },
  {
    "0": "29-03-2019",
    "1": "",
    "2": "INB/650297990/PAYTM MOBILE SOLUTIONS\nPVT LTD/",
    "3": "265.00",
    "4": "",
    "5": "59735.00",
    "6": "202"
  },
  {
    "0": "29-03-2019",
    "1": "",
    "2": "INB/650321575/PAYTM MOBILE SOLUTIONS\nPVT LTD/",
    "3": "90.00",
    "4": "",
    "5": "59645.00",
    "6": "202"
  },
  {
    "0": "30-03-2019",
    "1": "",
    "2": "INB/650376300/PAYTM MOBILE SOLUTIONS\nPVT LTD/",
    "3": "285.00",
    "4": "",
    "5": "59360.00",
    "6": "202"
  },
  {
    "0": "30-03-2019",
    "1": "",
    "2": "INB/650478392/PAYTM MOBILE SOLUTIONS\nPVT LTD/",
    "3": "1000.00",
    "4": "",
    "5": "58360.00",
    "6": "202"
  },
  {
    "0": "30-03-2019",
    "1": "",
    "2": "INB/650528746/PAYTM MOBILE SOLUTIONS\nPVT LTD/",
    "3": "253.00",
    "4": "",
    "5": "58107.00",
    "6": "202"
  },
  {
    "0": "30-03-2019",
    "1": "",
    "2": "INB/650596626/PAYTM MOBILE SOLUTIONS\nPVT LTD/",
    "3": "386.00",
    "4": "",
    "5": "57721.00",
    "6": "202"
  },
  {
    "0": "30-03-2019",
    "1": "",
    "2": "INB/650635986/PAYTM MOBILE SOLUTIONS\nPVT LTD/",
    "3": "183.00",
    "4": "",
    "5": "57538.00",
    "6": "202"
  },
  {
    "0": "30-03-2019",
    "1": "",
    "2": "INB/650664469/PAYTM MOBILE SOLUTIONS\nPVT LTD/",
    "3": "100.00",
    "4": "",
    "5": "57438.00",
    "6": "202"
  },
  {
    "0": "30-03-2019",
    "1": "",
    "2": "INB/650677169/RELIANCE JIO\nINFOCOM(BILLDESK)/NA",
    "3": "51.00",
    "4": "",
    "5": "57387.00",
    "6": "202"
  },
  {
    "0": "31-03-2019",
    "1": "",
    "2": "INB/650682826/PAYTM MOBILE SOLUTIONS\nPVT LTD/",
    "3": "275.00",
    "4": "",
    "5": "57112.00",
    "6": "202"
  },
  {
    "0": "31-03-2019",
    "1": "",
    "2": "INB/650803656/RAZORPAY SOFTWARE PVT\nLIMITED/",
    "3": "426.00",
    "4": "",
    "5": "56686.00",
    "6": "202"
  },
  {
    "0": "31-03-2019",
    "1": "",
    "2": "INB/650910542/SWIGGY(RAZORPAY)/",
    "3": "405.00",
    "4": "",
    "5": "56281.00",
    "6": "202"
  },
  {
    "0": "31-03-2019",
    "1": "",
    "2": "912010020834990:Int.Pd:01-01-2019 to 31-03-\n2019",
    "3": "",
    "4": "38.00",
    "5": "56319.00",
    "6": "202"
  },
  {
    "0": "31-03-2019",
    "1": "",
    "2": "INB/650923591/PAYTM MOBILE SOLUTIONS\nPVT LTD/",
    "3": "225.00",
    "4": "",
    "5": "56094.00",
    "6": "202"
  },
  {
    "0": "",
    "1": "",
    "2": "TRANSACTION TOTAL",
    "3": "3944.00",
    "4": "60038.00",
    "5": "",
    "6": ""
  },
  {
    "0": "",
    "1": "",
    "2": "CLOSING BALANCE",
    "3": "",
    "4": "",
    "5": "56094.00",
    "6": ""
  }
]
 ```
 
 ## TODO
  - Create django server
  - implement redis queue
  - post json data to requested webhook.
