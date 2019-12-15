import UIKit

var str1 = "This func "
var str2 = "is not aligned "
var str3 = "properly"

func badAlignFunc(s1: String, s2: String, s3: String) {
    print(s1 + s2 + s3)
}

func returnStrings(str: String, str1: String) -> String {
    print(str + str1)
    return 
}

var p = 0

badAlignFunc(s1: str1,
        s2: str2,
        s3: str3)


//badAlignFunc(s1: str1,
        //s2: returnStrings(str2,
        //str3),
        //s3: ""))
