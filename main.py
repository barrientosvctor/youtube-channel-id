from bs4 import BeautifulSoup
from requests.api import get

def main():
    example_url = 'https://www.youtube.com/@SomeChannel'
    print(f'''
YouTube Channel ID Scraper
Example: {example_url}
    ''')

    inputUser = str(input('Type the URL of some YouTube channel to know its channel ID: '))
    try:
        result = get(inputUser)
        soup = BeautifulSoup(result.text, 'html.parser')

        # Channel information
        fetch_name = soup.findAll(attrs={'itemprop': 'name'})
        fetch_channel_id = soup.findAll(attrs={'itemprop': 'url'})

        channel_name = str(fetch_name[0]).strip().split()[1].replace('content=', '').replace('"', '')
        channel_url = str(fetch_channel_id[0]).strip().split()[1].replace('href=', '').replace('"', '')
        channel_id = channel_url.split('/').pop()

        print(f'''
Name: {channel_name}
Channel URL: {channel_url}
Channel ID: {channel_id}
        ''')
    except ValueError:
        print(f'Error: Must provide an URL from youtube.com to get YouTube Channel ID.\nExample: {example_url}');
    except IndexError:
        print(f'Error: YouTube Channel ID not found. Make sure that URL is from youtube.com\nExample: {example_url}')

if __name__ == '__main__':
    main()
