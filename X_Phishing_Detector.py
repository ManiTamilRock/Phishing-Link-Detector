import re

def print_banner():
    banner = """
  _____ _                 _    ____  _              _____      _             
 / ____| |               | |  |  _ \| |            / ____|    | |            
| |    | | __ _ _ __ __ _| |  | |_) | |_   _  ___| |     __ _| | ___  _ __  
| |    | |/ _` | '__/ _` | |  |  _ <| | | | |/ __| |    / _` | |/ _ \| '_ \ 
| |____| | (_| | | | (_| | |  | |_) | | |_| | (__| |___| (_| | | (_) | | | |
 \_____|_|\__, |_|  \__,_|_|  |____/|_|\__,_|\___|\_____\__, |_|\___/|_| |_|
           __/ |                                          __/ |            
          |___/                                          |___/             
    """
    print(banner)
    print("Created by: A S MANIKANDAN")
    print("Project: X_Phishing_Detector\n")

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
    if 'bit.ly' in url or 'goo.gl' in url or 'tinyurl' in url or 'shorturl' in url:
        return True

    return False

if __name__ == "__main__":
    print_banner()

    # Example usage
    url_to_check = input("Enter the URL to check: ")
    if is_phishing_link(url_to_check):
        print("Warning: This is a phishing link.")
    else:
        print("The link appears to be safe.")
