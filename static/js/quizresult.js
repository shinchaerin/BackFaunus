function next() {
  if (confirm("게시판으로 가려면 확인을 눌러주세요!")) {
    location.href = "/showboard";
  } else {
    location.href = "/main";
  }
}
