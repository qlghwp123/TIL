# 후기

## 소감

1. 페어 프로그래밍을 한번 경험해보니 대화를 이끌어가려고 노력하고 최대한 속도를 내려고 노력했다.
2. 팀원 중 한 명이 나보다 못하는 것을 알고 이끌어 가려고 했지만 나의 독단적으로 진행한 부분이 많았다.
3. 하지만 팀원분께서 모르는 부분은 최대한 상세하게 설명하고 모르는 부분은 모른다고 말씀드렸다.
4. 서로 몰랐던 부분도 있었고 팀원분이 지속적으로 다른 방법 시도를 계속하시는  것이 너무 좋았다.



## TIL

1. 프로젝트 하면서 배웠던 부분(부트스트랩 기준)

   * button 태그가 아닌 a 태그에서 data-bs-toggle, data-bs-target 속성을 적용해도 modal 을 사용할 수 있었다.

   * d-{breakpoint}-{value} 형식을 지키면 해당 breakpoint 에 따라 display 속성에 값을 줄 수 있었다.

     즉, 특정 width 범위에 따라서 보이게 할 수도 있고 flex 나 table 과 같은 값을 줄 수 있다.

     width 992px 이상일 때, 주어진 width 에서 테이블의 각 column 이 동일한 영역을 가지게 만들고 싶었는데 d-lg-table을 주니까 각 영역을 동일하게 가지는 테이블이 표시가 되었다.

     해당 링크를 보니까 추가적 속성을 더 해줘야 한다고 하지만 이번 프로젝트에서는 문제가 없었다.[1]

   * 보이게 하고 싶지 않으면 d-none 을 주면 된다.

     * ex) pagination component 에 width 가 992px 이상일 때만 보여지고 flex 주기 나머지는 hidden

       ```html
       <nav aria-label="Page navigation example">
           <ul class="pagination justify-content-center d-none d-lg-flex">
       ```

       

## 모르는거 

1. 이번에는 딱히 없었다.



## 참고자료

[1] [display 속성에 table 값](https://www.biew.co.kr/entry/%EC%9B%B9%ED%8D%BC%EB%B8%94%EB%A6%AC%EC%85%94%EA%B0%80-%EC%95%8C%EA%B3%A0%EC%9E%88%EC%96%B4%EC%95%BC-%ED%95%A0-display-table-%EC%86%8D%EC%84%B1)