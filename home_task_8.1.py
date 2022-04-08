import re


def email_parse(email):
    if '.' in email and '@' in email:
        pattern = re.compile(r'(?P<username>\w+)[@](?P<domain>(\w+)(\.)(\w+))')
        result = pattern.finditer(email)
        for res in result:
            print(res.groupdict())
    else:
        msg = f'wrong email: {email}'
        raise ValueError(msg)


email_parse('pavel999kosarev@gmail.com')
