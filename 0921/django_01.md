# django - 01



## django 개발 환경 설정 가이드

### 1. 가상환경 생성 / 실행

> 폴더 생성 및 이동

```bash
$ mkdir foldername
$ cd foldername
```



> 가상환경 생성

```bash
$ python3 -m venv venvname
```



> 가상환경 실행

```zsh
# Windows
venvname\Scripts\activate

# Mac
$ source venvname/bin/activate
```



> 가상환경 종료
```bash
# Windows
deactivate

# Mac
$ cd venvname/bin
$ deactivate
```

<hr>

### 2. django LTS 버전 설치

> 장고 설치

```bash
$ pip install django==3.2.15
```

<hr>

### 3. django 프로젝트 생성 및 실행

> 프로젝트 생성 및 실행

```bash
# 가상환경 진입했다고 가정
$ django-admin startproject pjtname
$ cd pjtname
$ python manage.py runserver
```

<hr>

## 네트워크 퀴즈

### 1. IP 주소와 도메인 무엇인가?

> **IP 주소란?**
>
> 컴퓨터 네트워크에서 장치들이 서로 인식과 통신을 위해 사용하는 특수한 번호이다.



> **도메인이란?**
>
> 넓은 의미로 네트워크 상 컴퓨터를 식별하는 호스트명을 말한다. 좁은 의미로 도메인 레지스트리에게서 등록된 이름을 의미한다. 간단히 말하면 IP 주소를 문자로 알아보기 쉽게 만든 인터넷 상 주소이다. 예시로 example.com 이 있다. 

<hr>

### 2. 클라이언트와 서버는 무엇인가?

> **클라이언트란?**
>
> 서비스를 사용하는 사용자 혹은 사용자의 단말기를 가리키는 말이다.



> **서버란?**
>
> 서비스를 제공하는 컴퓨터이다.

<hr>

### 3. 정적 웹사이트와 동적 웹사이트의 차이점은 무엇인가?

> **정적 웹사이트란?**
>
> 웹 서버에 미리 저장된 파일이 그대로 전달되는 웹사이트이다.



> **동적 웹사이트란?**
>
> url 만으로는 들어갈 수 없는 웹사이트를 의미하며, url 변화가 없이 실시간 내용 갱신이 일어나는 웹사이트이다. 즉 요청에 따라 서버에 있는 데이터들을 스크립트에 의해 가공 처리 한 후에 생성한 HTML 문서를 전달하는 웹사이트이다.

<hr>

### 4. HTTP 정의, request, response 메시지 구성은 무엇인가?

> **HTTP란?**
>
> 웹에서 정보를 주고 받을 수  있는 프로토콜이다. 주로 HTML 문서를 주고받는 용도로 사용되나 최근에는 Plain text, JSON, XML 등 다양한 형태 정보도 전송하는 애플리케이션 레이어 프로토콜이다.



> **request, response 메시지 구성**
>
> startline
>
> headers
>
> 빈 줄
>
> body
> 
>
> ![HTTP_messages](django_01.assets/HTTP_messages.png)



<hr>

### 5. 프레임워크 무엇인가?

> **프레임워크란?**
>
> 설계의 기반이 되는 부분을 기술한  확장 가능한 기반 코드와 사용자가 이 코드를 자기 입맛대로 확장하는 데 필요한 라이브러리 이 두 가지 요소가 통합되어 제공되는 형태를 말하며, 
>사용자가 이를 이용해 일정 수준 이상의 품질을 보장받는 코드를, 비교적 빠른 시간에 완성 및 유지 보수할 수 있는 환경을 제공해주는 솔루션이다.


<hr>

## 참조

[1] [장고 개발 설정](https://wikidocs.net/70588)

[2] [IP 주소란](https://ko.wikipedia.org/wiki/IP_%EC%A3%BC%EC%86%8C)

[3] [도메인 네임 개념1](https://velog.io/@m-vault/%EB%8F%84%EB%A9%94%EC%9D%B8-%EB%84%A4%EC%9E%84%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80%EC%9A%94)

[4] [도메인 네임 정의](https://ko.wikipedia.org/wiki/%EB%8F%84%EB%A9%94%EC%9D%B8_%EB%84%A4%EC%9E%84)

[5] [도메인 네임 개념2](https://ko.wix.com/blog/post/what-is-a-domain)

[5] [클라이언트-서버 구조](https://ko.wikipedia.org/wiki/%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8_%EC%84%9C%EB%B2%84_%EB%AA%A8%EB%8D%B8)

[6] [클라이언트-서버 모델 개념](https://velog.io/@two_jay/%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8-%EC%84%9C%EB%B2%84-%EB%AA%A8%EB%8D%B8-5%EB%B6%84-%EA%B0%9C%EB%85%90%EC%9E%A1%EA%B8%B0)

[7] [정적, 동적 웹페이지 차이](https://velog.io/@ppyooy336/%EC%A0%95%EC%A0%81-%EB%8F%99%EC%A0%81-%EC%9B%B9%ED%8E%98%EC%9D%B4%EC%A7%80-%EC%B0%A8%EC%9D%B4%EB%8A%94)

[8] [HTTP 정의](https://ko.wikipedia.org/wiki/HTTP)

[9] [MDN(request, response message)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages)

[10] [request, response 메시지 구성](https://hanamon.kr/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-http-%EB%A9%94%EC%84%B8%EC%A7%80-message-%EC%9A%94%EC%B2%AD%EA%B3%BC-%EC%9D%91%EB%8B%B5-%EA%B5%AC%EC%A1%B0/)

[11] [HTTP Request / Response 메시지 구조](https://ohcodingdiary.tistory.com/5)

[12] [프레임워크란?](https://jokergt.tistory.com/89)

[13] [레드헷에서 말하는 프레임워크](https://www.redhat.com/ko/topics/cloud-native-apps/what-is-a-Java-framework)
