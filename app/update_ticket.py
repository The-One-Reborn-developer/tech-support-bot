import base64, os, requests

from dotenv import load_dotenv, find_dotenv


async def update_ticket(ticket_id: int,
                        text: str,
                        user_id: int,
                        has_photo: bool,
                        telegram_id: int) -> int | None:
    load_dotenv(find_dotenv())
    
    url = f'https://helpdesk.across.ru/api/v2/tickets/{ticket_id}/posts'

    auth_string = f'{os.getenv("EMAIL")}:{os.getenv("API")}'

    encoded_bytes = base64.b64encode(auth_string.encode("utf-8"))
    encoded_string = encoded_bytes.decode("utf-8")

    headers = {
        "Authorization": f"Basic {encoded_string}"
    }

    if has_photo:
        file_path = f'app/photos/{telegram_id}.jpg'

        payload = {
            "text": text,
            "user_id": user_id
        }

        files = [
            ('files[]',
            (f'{telegram_id}.jpg',
            open(file_path, 'rb'),
            'image/jpeg'))
        ]

        response = requests.post(url, headers=headers, data=payload, files=files)
    else:
        payload = {
            "text": text,
            "user_id": user_id
        }

        response = requests.post(url, headers=headers, json=payload)

    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

    return response.status_code