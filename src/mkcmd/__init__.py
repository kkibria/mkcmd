def set_warnigs_hook():
    import sys
    import warnings
    def on_warn(message, category, filename, lineno, file=None, line=None):
        print(f'Warning: {message}', file=sys.stderr)
    warnings.showwarning = on_warn

def get_template_path():
    from importlib.resources import files
    return files(__package__).joinpath(f"template")