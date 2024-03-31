import argparse
import re
from pathlib import Path
from warnings import warn

from . import get_template_path, set_warnigs_hook
from prj_gen.template import process_folder

def mk_py_var_name(s):
    pat = r'[^0-9a-zA-Z_]+'
    pat1 = r'^[0-9]'
    ret = re.sub(pat, "_", s)
    if re.match(pat1, ret):
        ret = "_n" + ret
    return ret

def build(params, path, force, no_ext, **kwargs):
    dst = Path(path)
    if dst.suffix == "" and not no_ext:
        dst = dst.with_suffix(".py")

    if not force:
        if dst.exists():
            warn(f'"{dst.name}" already exists, use --force, exiting!')
            return

    obj = lambda: None
    obj.exclude = '__pycache__'.split()
    prj = Path(get_template_path()).joinpath("prj")
    process_folder(obj, prj, dst.parent, {
        "__target__": dst.name,
        "__app__":dst.stem,
        "__appfn__":"do_"+mk_py_var_name(dst.stem)
        })

def main():
    params = {"app": "mkcmd"}

    parser = argparse.ArgumentParser(
        prog=params["app"],
        description='Creates python command file',
        epilog=f'python -m {params["app"]}')

    parser.add_argument('path')
    parser.add_argument('-f', '--force', default=False,
                    action='store_true')

    parser.add_argument('-n', '--no-ext', default=False,
                    action='store_true')

    args = parser.parse_args()
    params = params | vars(args)

    set_warnigs_hook()
    try:
        build(params, **params)
    except Exception as e:
        print(f'{e.__class__.__name__}:', *e.args)
        return 1
    
    return 0