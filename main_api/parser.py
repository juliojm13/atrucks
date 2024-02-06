import os

import io

from bs4 import BeautifulSoup

import pandas as pd

import requests

from main_api.models import OpenData


def find_links(html_content: str) -> list:
    """
    Find all links in the given HTML content that start with the specified prefix.

    Args:
        html_content (str): The HTML content to search for links.

    Returns:
        list: A list of links that start with the specified prefix.
    """

    # Define the desired prefix for links
    prefix = 'https://opendata.digital.gov.ru/'

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all anchor elements with href attributes
    links = soup.find_all('a', href=True)

    # Filter links that start with the desired prefix
    desired_links = [link['href'] for link in links if link['href'].startswith(prefix)]

    return desired_links


def load_html(page_url: str) -> str:
    """
    Load the HTML content from the specified file path.

    Args:
        page_url (str): The url of the page to load.

    Returns:
        str: The HTML content.
    """

    # Fetch the page content
    response = requests.get(page_url, verify=False)
    html_content = response.text

    return html_content


def get_csv_as_dataframe(csv_urls: list):
    """
    Load the CSV files from the specified URL and return a Pandas DataFrame.

    Args:
        csv_urls (list): The list with the URLs of the CSV files.

    Returns:
        pd.DataFrame: The DataFrame containing the CSVs data.
    """
    final_df = pd.DataFrame()

    column_names = {
        'АВС/ DEF': 'code',
        'От': 'from_limit',
        'До': 'to_limit',
        'Емкость': 'capacity',
        'Оператор': 'operator',
        'Регион': 'region',
        'ИНН': 'inn',
    }
    for csv_url in csv_urls:
        # Load the CSV file
        response = requests.get(csv_url, verify=False)
        response.raise_for_status()
        df = pd.read_csv(io.StringIO(response.text), delimiter=';')

        # Rename the columns using the provided mapping
        df = df.rename(columns=column_names)

        # Append the DataFrame to the final DataFrame
        final_df = pd.concat([final_df, df], ignore_index=True)

    return final_df


def save_dataframe_to_database(df: pd.DataFrame, replace=True):
    """
    Save the given Pandas DataFrame to the database.

    Args:
        df (pd.DataFrame): The Pandas DataFrame to save.
        replace (bool): If True, delete all existing data before saving.
    """
    if replace:
        OpenData.objects.all().delete()

    objects = [OpenData(**row.to_dict()) for index, row in df.iterrows()]
    OpenData.objects.bulk_create(objects)


def save_external_data():
    """
    Save the external data to the database.
    """
    html_data = load_html(os.getenv("PARSER_LINK"))
    links_data = find_links(html_data)
    df = get_csv_as_dataframe(links_data)
    save_dataframe_to_database(df)
    print("Data saved to the database.")
