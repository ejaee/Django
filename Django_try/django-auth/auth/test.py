import requests

from views import get_resource_owner_42_id

code = "c257bb22d60f2cc3f06716ee34cc4e9d4d0e9483dc9cc73f0f5fbc3fb3fe222c"
response_json = get_resource_owner_42_id(code)

# response = requests.get(response_json)

print('url request test')
print(response_json)

owner_id = 110667
access_token = 'f0e5bff49ceff6b195b3b4cbfe2c3950440197be0840ebebd826c9ca2a2f8ec9'

response = requests.get('https://api.intra.42.fr/v2/users/110667',
                        headers={'Authorization': f'Bearer {access_token}'}
                        )

# 응답 내용을 출력합니다.
print(response.json())

# # access_token: 3d112176fbffd48de68ab872168a130b7a7fc21b1518c1b55a0029fdb8163d4e
# # 110667 -> db에 저장