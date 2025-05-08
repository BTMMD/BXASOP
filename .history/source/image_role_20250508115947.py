from docutils.parsers.rst import roles
from docutils import nodes


def new_window_img_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    parts = text.split(',')
    href = parts[0].strip()
    img_src = parts[1].strip()
    alt_text = parts[2].strip()
    html = f'<a href="{href}" target="_blank" rel="noopener noreferrer"><img src="{img_src}" alt="{alt_text}"></a>'
    node = nodes.raw(text=html, format='html')
    return [node], []


def setup(app):
    roles.register_local_role('new_window_img', new_window_img_role)
    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
