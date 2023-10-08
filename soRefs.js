// How to write obj to file
var arr = [ {"id":"10", "class": "child-of-9"}, {"id":"11", "class": "child-of-10"}];
    
for (var i = 0; i < arr.length; i++){
  document.write("<br><br>array index: " + i);
  var obj = arr[i];
  for (var key in obj){
    var value = obj[key];
    document.write("<br> - " + key + ": " + value);
  }
}

// JSON IN JS
// https://devqa.io/json-tutorial-how-to-use-json-in-javascript/