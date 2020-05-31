function next() {
  if (confirm("퀴즈 START!! \n *한 번 선택한 답변은 수정할 수 없으니 신중하게 선택해주세요.* ")) {
    location.href = "amphibiaQuiz2.html";
  } else {
    location.href = "main.html";
  }
}
