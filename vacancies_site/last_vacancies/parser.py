import re
import requests
from datetime import timedelta, datetime


class HHParser():

    def __init__(self):
        pass

    def get_last_workday(self):
        today = datetime.now()
        offset = max(1, (today.weekday() + 6) % 7 - 3)
        delta = timedelta(offset)
        most_recent = today - delta
        return str(most_recent).split(' ')[0]

    def clean_html_tags(self, string: str):
        template = re.compile('<.*?>')
        cleantext = re.sub(template, '', string)
        return cleantext

    def get_vacancies(self):
        date = self.get_last_workday()
        params = {
            'text': 'python',
            'date_from': date,
            'date_to': date,
        }
        resp = requests.get('https://api.hh.ru/vacancies', params=params)
        return resp.json()

    def parse_vacancies(self):
        vacancies = self.get_vacancies()
        vacancyList = []
        for vacancy in vacancies['items']:
            vacancyList.append(
                {
                    'name': vacancy['name'],
                    'area': vacancy['area']['name'],
                    'skills': self.clean_html_tags(vacancy['snippet']['requirement']).split('. '),
                    'company': vacancy['employer']['name'],
                    'logo': vacancy['employer']['logo_urls'],
                    'salary': vacancy['salary'],
                    'date_published': vacancy['published_at'].split('T')[0],
                    'url': vacancy['alternate_url']
                }
            )
        return vacancyList


if __name__ == '__main__':
    hh = HHParser()
