import click

#
@click.command()
@click.argument('word')
@click.option('--p/--no-p', default=False)
def output(word, p):
    if p:
        click.echo(word.upper())
    else:
        click.echo(word)

if __name__ == '__main__':
    output()