import base64, os, requests

from dotenv import load_dotenv, find_dotenv


async def send_request(name: str, position: str, region: str, phone: str, medical_organization: str) -> int | None:
    load_dotenv(find_dotenv())

    auth_string = f'{os.getenv("EMAIL")}:{os.getenv("API")}'

    encoded_bytes = base64.b64encode(auth_string.encode("utf-8"))
    encoded_string = encoded_bytes.decode("utf-8")

    headers = {
        "Authorization": f"Basic {encoded_string}",
        "Content-Type": "application/json"
    }

    initial_url = f'https://helpdesk.across.ru/api/v2/users/?page=1'

    response = requests.get(initial_url, headers=headers)
    response_json = response.json()
    
    total_pages = response_json['pagination']['total_pages']

    for page in range(1, total_pages + 1):
        url = f'https://helpdesk.across.ru/api/v2/users/?page={page}'

        response = requests.get(url, headers=headers)
        response_json = response.json()

        user_email_data = f'{phone}@auto.bot'

        for user in response_json['data']:
            with open('users.json', 'a') as f:
                f.write(f"{user['id']}, {user['email']}\n")
            if user['email'] == user_email_data:
                return user['id']
    
    return None