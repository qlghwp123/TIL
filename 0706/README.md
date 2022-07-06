# 오늘은 무엇을 배웠을까?

아라보자



## Git

* Git 은 분산버전관리 도구이다.
* Git 은 프로젝트의 **파일**이 아닌 **커밋**을 관리한다.



## Git 동작흐름

![Workflow](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F994E924C5E29280735)



* Untracked : 깃이 추적하고 있지 않은 상태를 말한다.
* Unmodified : Commit을 모두 마친 상태, Commit은 깃에 내가 만든 코드를 저장을 완료한 상태이다.
* Modified : Git으로 **관리되고 있던** 코드를 수정하여 변경이 일어난 상태를 말한다.
* Staged : Untracked/Modified 상태인 파일을 add 하면 `Staged`상태가 된다.



## 기본 명령어

1. ```git log```

   * 현재 기록된 **커밋**을 조회한다.
   * git log -2 --oneline : 최근 2개의 커밋을 한 줄로 보여준다.

2. ```git status```

   * 파일의 상태를 알 수 있다.
     * Untracked files : 명령어의 결과에서 **Untracked files** 명단에 있는 파일들이 해당된다.
     * Modified : 명령어의 결과에서 **Changes not staged for commit** 명단에 해당된다.
     * Staged : 명령어의 결과에서 **Changes to be committed** 명단에 해당된다.

3. ```git add```

   * 특정 파일/폴더를 추적하겠다는 의미.

   * 또는 추적하고 있는 파일을 staged 상태로 만든다는 의미로 쓸 수 있다.

4. ```git remove -v```

   * 현재 등록된 원격 저장소의 정보를 확인할 수 있다

5. ```git push <원격 저장소 이름> <브랜치이름>```

   * 현재 로컬 저장소의 변경사항을 원격 저장소 내 해당 브랜치에 반영한다.
   * 다시 말하자면 git 은 커밋을 관리하므로 폴더/파일이 아닌 "커밋" 이 올라감.

6. ```git pull <원격 저장소 이름> <브랜치이름>```

   * 원격 저장소로 부터 변경된 이력을 받아와서 병합한다.



## .gitignore

1. 버전 관리를 하다보면 관리 받을 필요가 없는 파일이 반드시 존재하게 된다.
2. 그런 파일들을 관리하기 위한 설정 파일이라고 보면 된다.
3. 해당 파일에 원격 저장소에 commit 을 하고 싶지 않은 내용을 작성해두면 git 이 알아서 적힌 파일을 무시한다.
4. 이 파일은 항상 .git 폴더가 위치한 루트 폴더에 존재 해야한다.
5. 사용법은 [링크](https://kyu9341.github.io/Git/2020/08/23/git_gitignore/) 참조 



## 그 외 해본 것들

[파이썬 소개 Markdown](https://github.com/qlghwp123/TIL/blob/main/0706/Python.md)

[나만의 마크다운 요약본](https://github.com/qlghwp123/markdown)



## push 관련 에러

깃은 프로젝트의 **"파일"**이 아닌 **"커밋"**들을 관리한다.

remote repository 를 github 에서 생성 후 push 를 하니 에러가 뜬다.

```
 ! [rejected]        master -> master (non-fast-forward)
 error: failed to push some refs to 'https://github.com/qlghwp123/TIL.git'
```

**master -> master** : 로컬 저장소의 master 브랜치의 변경 사항을 원격 저장소의 master 브랜치에 반영하려 했는데 거부되었다.

**non-fast-forward** : 원격 저장소의 master 브랜치가 로컬 저장소의 버전보다 이전 버전이 아니다. 라는 의미이다.



즉, 오류가 발생한 원인은 github에서 새로운 프로젝트를 생성하면서 만들어진 원격 저장소의 readme.md

파일 때문일 것이다. 



더 정확히 말하면 readme.md 파일의 존재가 문제가 되는 것이 아니고, 원격 저장소에서 이루어진 readme.md를 

추가하는 커밋이 로컬 저장소의 커밋 로그에는 없기 때문이다.



push 명령은 로컬 저장소의 commit 목록과 원격 저장소의 commit 목록을 비교한다.

그런 다음 원격 저장소의 마지막 commit id와 동일한 commit id를 가진 로컬 저장소의 commit 시점을

찾아낸 뒤, 원격 저장소의 마지막 커밋과 연결한다.

원격 저장소의 첫번째 commit이자 마지막 commit인 readme를 추가하는 commit이 원격 저장소에는

존재하지 않고, 따라서 **현 상태에서는 둘을 연결할 수 없다.**



이 상황을 해결하는 방법에는

1. 원격 저장소를 삭제하고 다시 만든다. (readme.md 파일을 없애고 다시 저장소를 만든다.)
2. fetch나 pull 명령어로 원격 저장소의 마지막 commit을 로컬 저장소의 commit로그의 맨 앞으로 받아온다.



1번은 아닌거 같아서 pull을 해보면

```
>> git pull TIL main
-- fatal: refusing to merge unrelated histories
```

 이렇게 된다.



에러 내용은 원격 저장소의 master 브랜치에서 로컬 저장소의 FETCH_HEAD를 merge하는 것이 거부되었다.

commit 히스토리가 서로 관련이 없다는 뜻이다. 즉, 서로 관련성이 없기 때문에 merge할 수 없다는 것이다.



pull 명령어는 fetch + merge 작업을 한번에 처리하는 명령어이다. 현 상황은 fetch는 되었지만, merge가

되지 않은 상태이다.

기본적으로 merge는 원격 저장소와 로컬 저장소가 공통으로 가지고 있는 commit지점이 존재해야 한다.

그 지점부터 병합을 시도하기 때문이다. 애초에 공통되는 commit이 없기때문에 pull 명령어를 사용할 수

없는 것이다.



즉, 연결되는 **공통된 커밋 포인트가 없다**는 것이다.



따라서 ```git pull test main --allow-unrelated-histories``` 을 하니 해결됐다.



## 참조링크 

1. [깃 Workflow](https://kin3303.tistory.com/285)
2. [git push, pull (fatal: refusing to merge unrelated histories) 에러](https://jobc.tistory.com/177)
3. [깃 파일 상태](https://godtaehee.tistory.com/16)
4. [push 에러 해결](https://jobc.tistory.com/177)
