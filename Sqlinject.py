import requests

def teste_sql_injection():
    url_alvo = input("Send URL: ")
#TO ADD "HTTP://" IF YOU DO NOT HAVE
    if not url_alvo.startswith(("http://", "https://")):
        url_alvo = f"https://{url_alvo}"

    payloads = [" ' OR '1'='1'", '" OR "1"="1"', "') OR ('1'='1--"]

    for payload in payloads:
        full_url + f"{url_alvo}?parameter={payload}"
        try:
            response = requests.get(full_url)
            if "error" in responde.text.lower():
                print(f"VUNERABILITY FOUND IN: {full_url}")
        except requests.exceptions.RequestException as e:
            print(f"ERROR IN {full_url}: {e}")

def main():
    print_banner()
    test_sql_injection()

if __name__ == __main__:
    main()