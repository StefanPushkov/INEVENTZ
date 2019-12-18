from igramscraper.instagram import Instagram

proxies = {
    'http': 'http://123.45.67.8:1087',
    'https': 'http://123.45.67.8:1087',
}

instagram = Instagram()
instagram.set_proxies(proxies)

account = instagram.get_account('shtephqn')
print(account.identifier)