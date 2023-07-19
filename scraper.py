import requests
from bs4 import BeautifulSoup
from lxml import etree

def clean_text(text):
    text = text[4:]
    text = text.split("</td>", 1)[0]
    return text

def fetch_cpi(faculty_no, enrolment_no):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://ctengg.amu.ac.in',
        'Connection': 'keep-alive',
        'Referer': 'https://ctengg.amu.ac.in/web/st_result001.php?prog=btech',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }

    data = {
        'fac': faculty_no,
        'en': enrolment_no,
        'prog': 'btech',
    }

    try:
        response = requests.post('https://ctengg.amu.ac.in/web/table_result010.php',headers=headers, data=data)

        soup = BeautifulSoup(response.content, "html.parser")
        dom = etree.HTML(str(soup))

        table_elements = soup.find_all('td')
        spi_second_sem = float(clean_text(str(table_elements[len(table_elements)-3])))
        cpi_first_year = float(clean_text(str(table_elements[len(table_elements)-2])))
        spi_first_sem = 2 * cpi_first_year - spi_second_sem

        # print(spi_first_sem)
        # print(spi_second_sem)
        # print(cpi_first_year)

        return [spi_first_sem, spi_second_sem, cpi_first_year]

    except:
        return [0, 0, 0]


