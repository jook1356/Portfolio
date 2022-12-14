# PJT_08



## 배운점

- JSON을 이용한 데이터 송수신에 대해서 자세히 배울 수 있었습니다.
  - 댓글 및 대댓글을 JSON으로 송수신하고 이를 템플릿에 표현할 수 있었습니다.

- 대댓글의 Model을 별도로 추가하지 않고 기존의 Comment 모델에서 null=True 속성을 이용하여 댓글과 대댓글을 구분하는 방법을 배웠습니다.

- JavaScript를 활용하여 html 요소들을 생성하고 속성을 부여하는 방법들을 배우고, 이를 addEventListener를 사용하여 요소들을 Django와 통신하는데에 사용하게끔 하는 법을 배웠습니다.

- 추천 페이지를 만들 때 어떤 추천 로직을 사용할지에 대해서 고민을 하고 이를 적용할 수 있었습니다.




## 어려웠던 점

- 대댓글을 작성하는 로직을 작성할 때, 모델을 어떻게 적용할 지에 대해서 약간의 어려움이 있었던 것 같습니다.
- 대댓글을 작성할 때 로직이 axios를 이용한 것이었는데 이때 대댓글의 내용을 어떻게 JSON으로 전달할 수 있는지, 그리고 이것을 유효성 검사에서 통과할 수 있게끔 하는 과정에서 약간의 고비가 있었습니다.
  - Comment 모델에서 parent_comment를 exclude에 추가하지 않아서 일어난 일이었습니다.
- 댓글 및 대댓글 관련 기능을 자바스크립트를 구현할 때, 똑같은 기능을 상황에 따라 여러번 반복하여 구현해야하는 어려움이 있었습니다.
  - 예를 들어 새로 만들어진 댓글의 수정과 기존의 댓글의 수정은 다른 코드로 동작합니다.
- 추천 페이지를 만들때 장르를 기준으로 적용을 했는데 장르중에 거의 모든 영화들에 들어가있는 장르가 있어서 무조건 이 장르를 기준으로 추천을 하게 되었는데 이를 해결하기가 조금 힘든 면이 있었습니다.