# urlparser

This is a simple command line tool for extracting pieces (such as the scheme, port, or hostname) of a standard URL.

## Usage

```bash
$ urlparser hostname http://google.com
> google.com
$ urlparser port http://google.com
> 80
$ urlparser port https://google.com
> 443
$ urlparser scheme https://google.com
> https
```

## Help

```
Usage: urlparser [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  fragment  Get fragment from URL
  hostname  Get hostname from URL
  netloc    Get netloc from URL
  params    Get params from URL
  password  Get password from URL
  path      Get path from URL
  port      Get port from URL
  query     Get query from URL
  scheme    Get scheme from URL
  username  Get username from URL
```
