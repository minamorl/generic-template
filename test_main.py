import generictemplate
import shutil


def test_main():
    src = "./examples/simple-template"
    dest = "./sample"
    shutil.rmtree(dest, ignore_errors=True) 
    
    generictemplate.compose(src, dest, {
        "example": "value"
    })
    
