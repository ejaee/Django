import requests
from django.conf import settings


def get_resource_owner_42_id(code):
    try:
        # 토큰 받기 위한 요청
        token_response = requests.post(
            'https://api.intra.42.fr/oauth/token',
            json={
                'grant_type': 'authorization_code',
                'client_id': 'u-s4t2ud-c2faecc8ee78d381c5ec2197e74ed4828773591a23da572205c07745dbca87b7',
                'client_secret': "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",
                'code': code,
                'redirect_uri': "http://127.0.0.1"
            },
            headers={'Content-Type': 'application/json'}
        )

        print(token_response.status_code)
        if token_response.status_code == 200:
            access_token = token_response.json().get('access_token')

            print(f'access_token: {access_token}')

            # 토큰 정보를 사용하여 리소스 소유자 ID 가져오기
            owner_response = requests.get(
                'https://api.intra.42.fr/oauth/token/info',
                headers={'Authorization': f'Bearer {access_token}'}
            )
            print(f'owner_response: {owner_response}')

            if owner_response.status_code == 200:
                return owner_response.json().get('resource_owner_id')
            else:
                return '-1'
        else:
            return '-1'
    except Exception as e:
        return '-1'
