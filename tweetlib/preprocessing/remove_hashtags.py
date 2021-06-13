text = ["@made", "probando", "#vic", "#h", "#d", "s@", "df#"]

def RemoveHashtags(text):
    HASH = 0
    for t in text:
        elif '#' in t[0]:
            HASH = HASH + 1
    print(HASH)

if __name__ == '__main__':
    RemoveHashtags(text)