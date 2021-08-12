import demo
import click

@click.group()
#función que agrupa
def main():
    pass

#Download all tweets from all DB users
@main.command()
#esta funcion se convierte en un comando
def download_tweets_users():
    download_tweets = demo.download_all_tweets_users()

#Download all tweets of a user 
@main.command()
@click.option('--username', '-u', help='Entre un usuario, para proceder a descargar los tweets de dicho usuario')
@click.option('--typeuser', '-tu', help='Especifique el tipo de usuario. Ej: artista, politico, youtuber, deportista...', default="")
# 'Entre el tipo de usuario (opcional)'
# @click.argument('username')
# @click.argument('typeuser', default=None)

def download_tweets_user(username, typeuser):
    download_all_tweets_user = demo.download_all_tweets_user(username, typeuser)

#Delete user
@main.command()
@click.option('--deleteuser', '-du', prompt='Entre el usuario a eliminar', help='Entre el usuario que desee eliminar de la DB')
def delete_user(deleteuser):
    delete_u = demo.delete_user(deleteuser)

#Add new text
@main.command()
@click.option('--username', '-u', prompt='Entre un usuario', help='Entre el usuario del que desea guardar un tweet')
@click.option('--text', '-t', prompt='Entre el texto que desea guardar', help='Entre el texto del usuario que desea guardar en BD')
def add_text_user(username, text):
    add_text = demo.add_text_user(username, text)

if __name__ == '__main__':
    main()