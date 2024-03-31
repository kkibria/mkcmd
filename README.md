# Mkcmd

`mkcmd` creates python command file.

It is a python CLI tool that does the followings,
- Creates a poetry project.
- Runs git init.
- Creates a license file.

This tool is built with [`chef`](https://github.com/kkibria/chef) which uses
[`prj-gen`](https://github.com/kkibria/prj-gen) library to perform generation.

## Install
`mkcmd` requires `poetry` and `git` installed in your system and added to
`path` already. Recommended way is to install `mkcmd` globally and you will
have to install in administrative mode.

### Using poetry
```
poetry add git+https://github.com/kkibria/mkcmd.git
```

### Using pip
```
pip install mkcmd@git+https://github.com/kkibria/mkcmd.git
```

Without the administrative privilege, you can install it in a virtual
environment as well.

## Running
It can be executed directly from command line,
```
mkcmd <path>
```

You can also run this as a python module,
```
python -m mkcmd <path>
```