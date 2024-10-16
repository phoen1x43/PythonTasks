def check_password(password):
    if len(password) < 8:
        return False
    if not any(i.isupper() for i in password):
        return False
    if not any(i.islower() for i in password):
        return False
    if not any(i.isdigit() for i in password):
        return False
    return True

check_password("OFghYu87&^ewsiop")
check_password("polkji")
