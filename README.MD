# ColorfulScraper

Simple python web scraper using BeautifulSoup package to pull all the named colors from the [Encycolorpedia](https://encycolorpedia.com). Colors are stored as json object inside the colors.json file. Each json attribute name represents the name of the specific color, while the value of the attributes represents colors hexadecimal value. Colors are sorted in order of their hexadecimal values ascending.

## Motivation

Project was created as a helper to other, more serious, project that required having named colors and their hexadecimal values. As such, it can be used for any other project that requires such thing.

## Prerequisites

This project uses BeautifulSoup module for the purpose of pulling the webpage.

## Improvements

Consider using something like Scrapy for the scraping purpose.
