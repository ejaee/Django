from django.shortcuts import render, HttpResponse
from .models import UserProfile
import requests
import secrets
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return HttpResponse('index!')

def get_resource_owner_42_id(request, code):
    try:
        # 토큰 받기 위한 요청
        token_response = requests.post(
            'https://api.intra.42.fr/oauth/token',
            json={
                'grant_type': 'authorization_code',
                'client_id': 'u-s4t2ud-b677e803809d207e81ae3a321bdf542af8d318ca330d81824e4b972bca224918',
                'client_secret': "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",
                'code': code,
                'redirect_uri': "http://127.0.0.1"
            },
            headers={'Content-Type': 'application/json'}
        )

        if token_response.status_code == 200:
            access_token = token_response.json().get('access_token')

            created, user_profile = save_user_data(access_token)

            otp = generate_otp()
            send_email_with_otp(otp, user_profile)

            if created:
                return HttpResponse('Created new user profile')
            else:
                return HttpResponse('User profile already exists')

        else:
            return '-1'
    except Exception as e:
        return HttpResponse('Error: ' + str(e))

def send_email_with_otp(otp, user_profile):
    # otp 토큰 발급
    print(f'이메일로 보낼 otp: {otp}')
    user_email = user_profile.external_name + "@student.42seoul.kr"
    print(f'이메일 : {user_email}')
    send_otp_email(user_email, otp)  # 이메일을 UserProfile 모델에 저장했다고 가정
    print('이메일을 발송하였습니다.')

def save_user_data(access_token):
    # 토큰 정보를 사용하여 리소스 소유자 정보 가져오기
    owner_response = requests.get(
        'https://api.intra.42.fr/oauth/token/info',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    # 소유자 고유 번호 정보 가져오기
    # print(owner_response.json().get('resource_owner_id'))
    owner_id = owner_response.json().get('resource_owner_id')
    if not UserProfile.objects.filter(external_id=owner_id).exists():

        # 소유자 고유 정보를 통해 원하는 정보 42 사이트에서 가져오기
        owner_data = requests.get(f'https://api.intra.42.fr/v2/users/{owner_id}',
                                  headers={'Authorization': f'Bearer {access_token}'}
                                  )
        owner_name = owner_data.json().get('login')
        # 소유자 'image' 데이터에서 'link' 값 추출
        owner_image_link = owner_data.json().get('image', {}).get('link')
        print('Image Link:', owner_image_link)
            # 프로필 사진 URL도 받아와야 한다면 여기에 추가
        user_profile, created = UserProfile.objects.update_or_create(
            external_id=owner_id,
            external_name=owner_name,
            defaults={'profile_picture': owner_image_link}
        )
        return created, user_profile
    else:
        # 이미 존재하는 owner_id의 경우
        return False, UserProfile.objects.get(external_id=owner_id)

def generate_otp(length=6):
    return ''.join([secrets.choice('0123456789') for _ in range(length)])

def send_otp_email(email, otp):
    subject = 'Pikapong login OTP'
    message = f'Your OTP is: {otp}'
    send_mail(subject, message, 'admin@pikapong.com', [email])

    # for test
    # email = 'ejae6467@gmail.com'
    # send_mail(subject, message, 'admin@pikapong.com', [email])