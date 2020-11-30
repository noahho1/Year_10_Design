//big take away
//two ways to run your javascript
//
// 1. For quick testing you can run script right in the browser (in the console)
// 2. Typically link javascript files to web pages. When a script is linked it automatically runs
console.log("Running Script")

var uNames = ["user1@test.com", "user2@test.com", "user3@test.com"]
var pWords = ["pword1", "pword1", "pword2", "pword3"]

function checkCred(u, p){
	
	for (i = 0; i < uNames.length; i = i + 1){
		if (uNames[i] === u){
			if (pWords[i] == p){
				return true
			}
		}
	}

	return false
}

//x = checkCred("user5@test.com", "pword1")
//console.log(x)
//x = checkCred("user1@test.com", "pword1")
//console.log(x)
//x = checkCred("user1@test.com", "pword6")
//console.log(x)