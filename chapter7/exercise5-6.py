letter = """Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your {room}.
Please note that it should never be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.

Thank you for your support.
Sincerely,
{spokesman}
{job_title}
"""

response = {'salutation': 'Mr.', 'name': 'John', 'product': 'TV', 'verbed': 'exploded',
            'room': 'hall', 'animals': 'cats', 'amount': '10 000 RUB',
            'percent': '10', 'spokesman': 'Mr. Jack', 'job_title': 'lord of the company'}

print(letter.format(**response))
