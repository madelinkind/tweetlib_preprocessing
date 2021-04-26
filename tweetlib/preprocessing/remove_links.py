import re

# text = """https://pepe.pepe.pepe.com probando #PP @Maria quiere comentar # # # :)"""

def RemoveLinks(text: str):
    result = re.sub(r"http\S+", "", text)
    print(result) 

# if __name__ == '__main__':
#     RemoveLinks(text)