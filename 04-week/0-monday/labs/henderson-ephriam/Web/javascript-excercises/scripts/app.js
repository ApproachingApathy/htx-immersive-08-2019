function madlibs(name, subject) {
    /**
     * This function accepts name and subject and returns a new string.
     */
    console.log("I ran!")
    var phrase = name.charAt(0).toUpperCase() + name.slice(1) + "'s favorite subject is " + subject + "!"

    document.getElementById("madlibsResults").innerHTML = phrase
}

function tipCalc(bill, service) {
    bill = parseFloat(bill)
    switch (service) {
        case "bad":
            var tipPercent = .1;
            break;
        case "fair":
            var tipPercent = .15;
            break;
        case "good":
            var tipPercent = .2;
            break;
    }
    // return bill + (bill * tipPercent)
    var tip = bill * tipPercent;
    var total = bill + tip
    document.getElementById("tipCalcResults").innerHTML = "$" + bill + "<br/>" + "+ $" + tip + "<br/>" + "= " + total ;
}

function printNumber(start, end) {
    while (start < end) {
        console.log(start);
        start++;
    }

    return start;
}

function printSquare(num) {
    var cellNum = num
    var line = "";
    for (cellNum; cellNum > 0; cellNum--) {
        line = line + "*";
    }

    for (num; num > 0; num--) {
        console.log(line);
    }
    return line
}

function printBox(w, h) {
    var cellNum = w;
    var floorCeilLine = "";
    middleLine = "*" ;

    for (cellNum; cellNum > 0; cellNum--) {
        floorCeilLine = floorCeilLine + "*";
    }

    console.log(floorCeilLine);

    for (w; w > 0; w--) {
        middleLine += " "
    }

    middleLine += "*";

    for (h -= 2; h > 0; h--) {
        console.log(middleLine)
    }

    console.log(floorCeilLine);
}

function printBanner(str) {
    var line = ""
    for (var num = str.length + 4; num > 0; num--) {
        line += "*";
    }

    console.log(line);
    console.log("* " + str + " *");
    console.log(line);
}

function leeter(str) {
    str.toUpperCase();
    str.forEach()
    

}

