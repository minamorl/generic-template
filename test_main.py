import generictemplate


def test_main():
    generictemplate.compose("./examples/simple-template", {
        "example": "value"
    })
    
