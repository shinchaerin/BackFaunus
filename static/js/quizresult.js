function next() {
  if (confirm("게시판으로 갈려면 확인을 눌러주세요!")) {
    location.href = "showboard.html";
  } else {
    location.href = "main.html";
  }
}
