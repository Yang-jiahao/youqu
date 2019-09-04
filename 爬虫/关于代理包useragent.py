from fake_useragent import UserAgent

u=UserAgent()

headers={'user-agent':u.random}
print(headers)