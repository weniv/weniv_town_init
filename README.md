# weniv_town_init
* 이 레파지토리는 개발용 레파지토리가 아니라 웹 소캣이 사용되는 여러 프로젝트에 이 코드가 사용될 것 같아 기본 형태만 저장해놓은 레포입니다.
* 아래와 같이 실행할 수 있습니다.

## BE
* 가상환경이 올라가 있기 때문에 그대로 실행하면 됩니다.
```
.\venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

* 설치는 안해도 됩니다. 다만 설정했던 명령어를 저장하고자 여기에도 올립니다.
```shell
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows의 경우:
venv\Scripts\activate
# Mac/Linux의 경우:
source venv/bin/activate

# 필요한 패키지 설치
pip install fastapi uvicorn websockets
```

## FE
* 라이브 서버로 실행해주세요.
