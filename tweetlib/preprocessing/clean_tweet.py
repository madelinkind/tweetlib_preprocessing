# import re

#-------------------------------------------------------------------------------------------------
#SECCIÓN DATASET UTILIZADO
#-------------------------------------------------------------------------------------------------

# text = ["@Made", "#PP", "https://pp.com", "@Madelin", "#pepe", "Mucha", "mano", ",", "técnica", "en", "productos", "http://pp.com,"]
# text = '@Made #9l #ñ https://pp.com #yty#$@%'

# Remove hashtag
# def CleanTweets(text: list):
#     corpus = " ".join(text)
#     result = (' '.join(re.sub("(#[A-Za-z0-9-ñ]+)"," ",corpus).split()))
#     return result.split(',')

#https://stackoverflow.com/questions/24399820/expression-to-remove-url-links-from-twitter-tweet

#Eliminar links
#result = re.sub(r"http\S+", "", tweet)


#https://stackoverflow.com/questions/8376691/how-to-remove-hashtag-user-link-of-a-tweet-using-regular-expression
#Eliminar links, hashtag y caracteres especiales. Implementar este
#' '.join(re.sub("(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x).split())

#Lo mismo que el de arriba pero le hice un pequeo cambio para que me tomara en cuenta la ñ
#' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z-ñ \t])|(\w+:\/\/\S+)"," ",x).split())

# if __name__ == '__main__':
#     CleanTweets(text)