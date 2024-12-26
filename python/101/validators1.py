#pip install validators
import validators

print(validators.url("http://www.google.com")) #True
flag = validators.url("www.google.com")
print(flag) #ValidationError(func=url, args={'value': 'www.google.com'})
print(validators.email('someone@example.com')) #True