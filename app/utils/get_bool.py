from typing import Union

def get_bool(value: str) -> Union[bool, None]:

    if value == 'true':
        return True
    elif value == 'false':
        return False
    else:
        return None