from bs4 import BeautifulSoup

def get_identifiers(file):
    with open(file, "r") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    classes = set([
            class_ 
            for element in soup.find_all(class_=True)
            for class_ in element["class"]
    ])

    ids = set([
            element["id"] 
            for element in soup.find_all(id=True)
    ])

    tags = set([
            element.name 
            for element in soup.find_all()
    ])

    return (["."+class_ for class_ in classes] +
            ["#"+id for id in ids] + 
            list(tags))