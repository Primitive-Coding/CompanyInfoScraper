# CompanyInfo Scraper

- Get info related to a company including it's full name, sector, industry, and country of origin.

---

### Setup

1. Clone git repository: `https://github.com/Primitive-Coding/CompanyInfoScraper.git`
2. Configure the "config.json" file. All the necessary folders will be created within the `data_export_path`.

```
    {
        "data_export_path": "D:\\PATH TO EXPORT DATA\\CompanyInfo"
    }

```

3. Install the projects requirements with `pip install -r requirements.txt`

---

### Instructions

- Create a class instance. If debug is set to true, various pieces of information will be logged to confirm steps of scraping were completed.

```
    ci = CompanyInfo()
```

---

### Overview

- Using the `yfinance` package this program will get relevant company information and store the information in a csv file locally based on the `data_export_path`.

- Once the data is saved, it will read from the local data going forward.

- In this example we will be using `AMZN`.

###### General Info

```
    f = ci.get_company_info("AMZN")

    # Output
    name         Amazon.com, Inc.
    sector      Consumer Cyclical
    industry      Internet Retail
    country                   USA
```

###### Sector

```
    f = ci.get_company_sector("AMZN")

    # Output
    "Consumer Cyclical"
```

###### Industry

```
    f = ci.get_company_industry("AMZN")

    # Output
    "Internet Retail"
```

---

### Local Data

- All locall data is stored in this file: `D:\YOUR PATH HERE\CompanyInfo\company_info.csv`.

- The folder `CompanyInfo` and file `company_info.csv` will be created automatically, if they do not already exist.

- Point `data_export_path = D:\YOUR PATH HERE` in `config.json`.

- If information for the company does not exist locally, calling any of the "get" functions such as `get_company_sector()`, will automatically add the data locally for future use.

##### For Example

```
# We start out with our information for AMZN.

            name             sector              industry      country
ticker
AMZN    Amazon.com, Inc.  Consumer Cyclical  Internet Retail     USA


# Now we try and get information related to AAPL

f = ci.get_company_sector("AAPL")


# Now our local data looks like this. AAPL was succesfully added locally.

            name             sector              industry      country
ticker
AMZN    Amazon.com, Inc.  Consumer Cyclical       Internet Retail     USA
AAPL          Apple Inc.         Technology  Consumer Electronics     USA
```
