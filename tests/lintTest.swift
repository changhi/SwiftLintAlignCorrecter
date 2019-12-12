import UIKit

var str = "Hello, playground"

func badAlignmentFunc(s1: String, s2: String, s3: String) {
    print(s1 + s2 + s3)
}

var p = 0

badAlignmentFunc(s1: "This func ",
            s2: "is not aligned ",
            s3: "properly")
