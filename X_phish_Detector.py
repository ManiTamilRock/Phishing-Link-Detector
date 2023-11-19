import re

def is_phishing_link(url):
    # Check for suspicious keywords in the URL
    suspicious_keywords = ['login', 'password', 'bank', 'paypal', 'secure', 'account']
    for keyword in suspicious_keywords:
        if keyword in url:
            return True

    # Check for the presence of '@' symbol, which is unusual in the domain part of a URL
    if '@' in url:
        return True

    # Check for the use of IP address instead of a domain name
    ip_address_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    if ip_address_pattern.search(url):
        return True

    # Check for the use of 'https' in the URL (phishing sites may use 'http')
    if 'https' not in url:
        return True

    # Check for URL shorteners
    if 'bit.ly' in url or 'goo.gl' in url or 'tinyurl' in url:
        return True

    return False

# Example usage
url_to_check = input("Enter the URL to check: ")
if is_phishing_link(url_to_check):
    print("Warning: This is a phishing link.")
else:
    print("The link appears to be safe.")
