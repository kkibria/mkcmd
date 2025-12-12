# Mkcmd

`mkcmd` creates python command file.

This tool is built with [`chef`](https://github.com/kkibria/chef) which uses
[`prj-gen`](https://github.com/kkibria/prj-gen) library to perform generation.

## Install
Recommended way is to install `mkcmd` globally and you will
have to install in administrative mode.

### Using uv
```
uv tool -n install git+https://github.com/kkibria/mkcmd.git
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