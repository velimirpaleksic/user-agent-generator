import random

def generate_user_agent(os_type):
    os_type = os_type.lower()
    
    if os_type == 'windows':
        return f'Mozilla/5.0 (Windows NT {random.choice(["5.1", "6.0", "6.1", "6.2", "6.3", "10.0"])}; {random.choice(["Win64; x64", "Win32; x86"])}; rv:{random.randint(50, 85)}.0) Gecko/20100101 Firefox/{random.randint(50, 85)}.0'

    elif os_type == 'mac':
        return f'Mozilla/5.0 (Macintosh; Intel Mac OS X {random.choice(["10_6", "10_7", "10_8", "10_9", "10_10", "10_11", "10_12", "10_13", "10_14", "10_15"])}_{random.randint(0, 9)}_{random.randint(0, 9)}) AppleWebKit/{random.randint(500, 600)}.1.{random.randint(1, 99)} (KHTML, like Gecko) Version/{random.randint(10, 15)}.0 Safari/{random.randint(500, 600)}.1.{random.randint(1, 99)}'

    elif os_type == 'linux':
        return f'Mozilla/5.0 (X11; Linux {random.choice(["i686", "x86_64"])}; rv:{random.randint(50, 85)}.0) Gecko/20100101 Firefox/{random.randint(50, 85)}.0'

    elif os_type == 'android':
        return f'Mozilla/5.0 (Linux; Android {random.choice(["4.0", "4.1", "4.2", "4.3", "4.4", "5.0", "5.1", "6.0", "7.0", "8.0", "9.0"])}; {random.choice(["Mobile", "Tablet"])}; {random.choice(["en-US", "en-GB", "es-ES", "fr-FR", "de-DE", "it-IT", "pt-PT", "ja-JP", "ko-KR"])}; rv:{random.randint(50, 85)}.0) Gecko/20100101 Firefox/{random.randint(50, 85)}.0'

    elif os_type == 'ios':
        return f'Mozilla/5.0 (iPhone; CPU iPhone OS {random.randint(9, 15)}_{random.randint(0, 4)} like Mac OS X) AppleWebKit/{random.randint(500, 600)}.1.{random.randint(1, 99)} (KHTML, like Gecko) CriOS/{random.randint(50, 85)}.0.{random.randint(1, 99)}.{random.randint(1, 99)} Mobile/{random.randint(9, 15)}A{random.randint(100, 999)} Safari/{random.randint(500, 600)}.1.{random.randint(1, 99)}'

    else:
        raise ValueError(f'Unsupported OS type: {os_type}')

def save_user_agents(os_type, num_user_agents):
    user_agents = [generate_user_agent(os_type) for _ in range(num_user_agents)]
    with open(f'{os_type}_user_agents.txt', 'w') as file:
        for i, user_agent in enumerate(user_agents, 1):
            file.write(user_agent + '\n')
            print(f'Generated user agent {i}/{num_user_agents}', end='\r')

if __name__ == "__main__":
    os_type = input("Enter the OS type (windows, mac, linux, android, ios): ").lower()
    num_user_agents = int(input("Enter the number of user agents to generate: "))
    
    save_user_agents(os_type, num_user_agents)
    print(f'\n{num_user_agents} user agents for {os_type} saved to {os_type}_user_agents.txt')