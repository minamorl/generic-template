import shutil
import os
import generictemplate
import jinja2
import shutil


def compose(src, dest, values):
    """ Compose template files and copy all files from src to dest. """
    env = jinja2.Environment(loader=jinja2.loaders.FileSystemLoader(src))

    if os.path.exists(dest):
        return False

    shutil.copytree(src, dest)

    for root, dirs, files in os.walk(src):
        for fname in files:
            if fname.endswith(".template"):
                template = env.get_template(fname)
                content = template.render(values=values)
                with open(os.path.join(dest, fname.replace(".template", "")), "w") as f:
                    f.write(content)
                os.remove(os.path.join(dest, fname))
    if os.path.exists(os.path.join(dest, "_scheme.json")):
        os.remove(os.path.join(dest, "_scheme.json"))
