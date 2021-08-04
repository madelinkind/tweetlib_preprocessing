# text = ["@made", "probando", "#vic", "@#h", "#d", "s@", "df#"]

def rm_mentions(text: list):
    # MENT = 0
    if type(text) == str:
        text = text.split(" ")
    within_ment = [word for word in text if not '@' in word[0]]
        # if '@' in t[0]:
            # MENT = MENT + 1
    # print(within_ment)
    return within_ment

def count_mentions(text: list):
    # tx = text.split()
    if type(text) == str:
        text = text.split(" ")
    list_mentions = [word for word in text if '@' in word[0]]
    return len(list_mentions)
# if __name__ == '__main__':
#     rm_mentions(text)