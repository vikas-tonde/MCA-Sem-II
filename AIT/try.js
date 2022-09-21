var fs = require("fs");
var data = "Vikas Tonde";
fs.writeFile("demo.txt", data, (err) => {
 if (err) console.log(err);
 console.log("Successfully Written to File.");
});
