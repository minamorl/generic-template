# generic-template

Generic templating with Jinja2.

## What is this

This project is made for handling process of boilerplate.

## API

### compose(src, dest, values)

`compose()` is a utility function that creates processed files from template files under local directory. `src` and `dest` are must be path str. `values` is a dict object that passed to template files.
```python
import generictemplate

generictemplate.compose("template", "./destination/", {
  "value": "1"
})
```
