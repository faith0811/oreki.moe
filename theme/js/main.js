
var character_list = [{
  "name": "折木奉太郎",
  "img_url": "/images/oreki.jpeg",
  "tagline": "不做也行的事情就不做，非做不可的事情一切从简",
}, {
  "name": "千反田える",
  "img_url": "/images/chitanda.jpeg",
  "tagline": "我很好奇",
}];

var random_value = parseInt(Math.random() * 2);
var character = character_list[random_value];
document.getElementById("author_logo").src = character["img_url"];
document.getElementById("author_name").innerHTML = character["name"];
document.getElementById("author_tagline").innerHTML = character["tagline"];
