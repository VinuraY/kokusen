# Whois infogather.
import requests
from bs4 import BeautifulSoup
import termcolor


def main(site):

    try:

        url = f'https://www.whois.com/whois/{site}'

        web_page = requests.get(url)

        result = BeautifulSoup(web_page.content, 'html.parser')

        data = result.find(id='registrarData')

        print(termcolor.colored(f'\n{data.text.strip()}', 'blue'))

    except:

        print(termcolor.colored(
            '\nAn error occured. Check your domain name again!', 'red'))
