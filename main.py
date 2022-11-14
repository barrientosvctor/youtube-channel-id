from bs4 import BeautifulSoup
import requests

def main():
    print('''
YouTube Channel ID Scraper
Example: https://www.youtube.com/c/SomeChannel
    ''')

    inputUser = str(input('Type the URL of some YouTube channel to know its channel ID: '))
    try:
        result = requests.get(inputUser)
        soup = BeautifulSoup(result.text, 'lxml')

        # Channel information
        title = soup.findAll(property='og:title')
        channelId = soup.findAll(property='og:url')

        print(f'''
    Name: {' '.join(str(e) for e in title).split('content=')[1].replace(' property="og:title"/>', '')}
    Channel ID: {' '.join(str(e) for e in channelId).split('content=')[1].replace(' property="og:url"/>', '')}
        ''')
    except ValueError:
        print('Error: Must provide an URL from youtube.com to get YouTube Channel ID.\nExample: https://www.youtube.com/c/SomeChannel');
    except IndexError:
        print('Error: YouTube Channel ID not found. Make sure that URL is from youtube.com\nExample: https://www.youtube.com/c/SomeChannel')

if __name__ == '__main__':
    main()
