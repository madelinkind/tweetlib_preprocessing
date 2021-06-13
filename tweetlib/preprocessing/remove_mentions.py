text = ["@made", "probando", "#vic", "#h", "#d", "s@", "df#"]

def RemoveMentios(text):
    MENT = 0
    for t in text:
        if '@' in t[0]:
            MENT = MENT + 1
    print(MENT)

if __name__ == '__main__':
    RemoveMentios(text)