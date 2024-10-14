<<<<<<< HEAD
function checkLeapYear() {
    var year = document.getElementById("year").value;
=======
function checkLeapYear(){
    var year = document.getElementById("year").value;
>>>>>>> bd6bdb02c5a2de226107d7ae980d23a198363a47

    if (year % 4 == 0) {
        if (year % 100 != 0 || year % 400 == 0) {
            document.getElementById("result").innerHTML = year + " is a leap year.";
        } else {
            document.getElementById("result").innerHTML = year + " is not a leap year.";
        }
    } else {
        document.getElementById("result").innerHTML = year + " is not a leap year.";
    }
}
