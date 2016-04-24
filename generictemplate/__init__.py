import shutil
import os
import generictemplate
import jinja2


def compose(path, values):
    env = jinja2.Environment(loader=jinja2.loaders.FileSystemLoader(path))
    for root, _, files in os.walk(path):
        for fname in files:
            if fname.endswith(".template"):
                template = env.get_template(fname)
                print(template.render(values=values))
        

    #  if not os.path.exists(path):
        #  module_path = os.path.dirname(minamonious.__file__)
        #  shutil.copytree(os.path.abspath(os.path.join(module_path, "./templates")), path)
