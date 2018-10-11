#!/usr/bin/env python

import click
from urllib.parse import urlparse

import socket

@click.group()
@click.pass_context
def cli(ctx):
    if ctx.parent:
        print(ctx.parent.get_help())


@cli.command(short_help="Get scheme from URL")
@click.argument('url')
@click.option('-f', '--allowfail', is_flag=True)
def scheme(url, allowfail):
    o = urlparse(url)
    if o.scheme:
        click.echo(o.scheme)
        exit(0)
    if allowfail:
        exit(0)
    exit(1)


@cli.command(short_help="Get netloc from URL")
@click.argument('url')
@click.option('-f', '--allowfail', is_flag=True)
def netloc(url, allowfail):
    o = urlparse(url)
    if o.netloc:
        click.echo(o.netloc)
        exit(0)
    if allowfail:
        exit(0)
    exit(1)


@cli.command(short_help="Get path from URL")
@click.argument('url')
@click.option('-f', '--allowfail', is_flag=True)
def path(url, allowfail):
    o = urlparse(url)
    if o.path:
        click.echo(o.path)
        exit(0)
    if allowfail:
        exit(0)
    exit(1)


@cli.command(short_help="Get params from URL")
@click.argument('url')
@click.option('-f', '--allowfail', is_flag=True)
def params(url, allowfail):
    o = urlparse(url)
    if o.params:
        click.echo(o.params)
        exit(0)
    if allowfail:
        exit(0)
    exit(1)


@cli.command(short_help="Get query from URL")
@click.argument('url')
@click.option('-f', '--allowfail', is_flag=True)
def query(url, allowfail):
    o = urlparse(url)
    if o.query:
        click.echo(o.query)
        exit(0)
    if allowfail:
        exit(0)
    exit(1)


@cli.command(short_help="Get fragment from URL")
@click.argument('url')
@click.option('-f', '--allowfail', is_flag=True)
def fragment(url, allowfail):
    o = urlparse(url)
    if o.fragment:
        click.echo(o.fragment)
        exit(0)
    if allowfail:
        exit(0)
    exit(1)


@cli.command(short_help="Get username from URL")
@click.argument('url')
@click.option('-f', '--allowfail', is_flag=True)
def username(url, allowfail):
    o = urlparse(url)
    if o.username:
        click.echo(o.username)
        exit(0)
    if allowfail:
        exit(0)
    exit(1)


@cli.command(short_help="Get password from URL")
@click.argument('url')
@click.option('-f', '--allowfail', is_flag=True)
def password(url, allowfail):
    o = urlparse(url)
    if o.password:
        click.echo(o.password)
        exit(0)
    if allowfail:
        exit(0)
    exit(1)


@cli.command(short_help="Get hostname from URL")
@click.argument('url')
@click.option('-f', '--allowfail', is_flag=True)
def hostname(url, allowfail):
    o = urlparse(url)
    if o.hostname:
        click.echo(o.hostname)
        exit(0)
    if allowfail:
        exit(0)
    exit(1)


@cli.command(short_help="Get port from URL")
@click.argument('url')
@click.option('-f', '--allowfail', is_flag=True)
def port(url, allowfail):
    o = urlparse(url)
    if o.port:
        click.echo(o.port)
        exit(0)
    if o.scheme:
        click.echo(socket.getservbyname(o.scheme))
        exit(0)
    if allowfail:
        exit(0)
    exit(1)


if __name__ == '__main__':
    cli()
