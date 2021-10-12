# Docker 기반이 될 이미지(python 3.7-apline -> lightweight version)
FROM python:3.7-alpine

# 도커 컨테이너 안에서 python을 실행할 때 unbuffered mode를 추천
# python이 실행될 때 도커이미지와 관련된 것들의 일부 충돌을 막아준다.
ENV PythonUNBUFFERED 1

# dependanse install
# 앞에있는 친구 = 복사할 파일 경로, 뒤에있는 친구 = docker 이미지 만들어질 파일명
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# 유저 생성 -D : 프로젝트 안에서 프로세스 실행 시 유저
RUN adduser -D user
# 유저 설정 
  # 이것은 보안을 목적으로 설정
  # root 계정으로 도커 이미지를 실행하는 것을 추천하지 않는다.
  # 만약 root 계정으로 실행 시 누군가 application을 손상시키면 
  # 전체 이미지에 대한 root access 권한을 가질 수 있고
  # 악의 적인 행위 외의 작업을 수행 할 수 있다.
USER user