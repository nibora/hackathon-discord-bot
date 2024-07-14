from weatherRequest import getWeatherData

def getResponse(input: str, author: str) -> str:
    lowered: str = input.lower()
    titleAuthor: str = author.title()

    if lowered == "hallo":
        return f'Hallo {titleAuthor}'
    elif "bye" in lowered:
        return 'Bis dann, euer Kevin!'   
    elif lowered == '!weather':
        return getWeatherData()


