function next() {
  if (
    confirm(
      "동물 설명이 전부 끝이 났습니다!! \n퀴즈를 풀려면 확인, 동물 정보를 보려면 취소를 눌러 주세요."
    )
  ) {
    location.href = "/mammaliaQuiz/mammaliaQuiz1";
  } else {
    location.href = "/main";
  }
}
