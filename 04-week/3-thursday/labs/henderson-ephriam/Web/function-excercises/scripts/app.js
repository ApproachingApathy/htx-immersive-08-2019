function findPositiveNumbers(arrNumbers) {
    let result = arrNumbers.filter(number => number > 0);
    return result;
}

function findEvenNumbers(arrNumbers) {
    let result =  arrNumbers.filter(function(number) {
        let isDivisibleBy2 = (number % 2) == 0;
        if (number != 0 && isDivisibleBy2) {
            return true;
        }
        return false;
    })
    return result;
}

function squareNumbers(arrNumbers) {
    let result = arrNumbers.map(number => number**2)
    return result;
}

function findHotCities(arrCities) {
    let result = arrCities.filter(objCity => objCity.temperature > 70)
    return result;
}

function findCityNames(arrCities) {
    let result = arrCities.map(objCity => objCity.name)
    return result;
}

// function goodJobInator(arrName) {
//     let re
// }

function sortAlpha(arrStr) {
    return arrStr.sort()
}

function sortLength(arrStr) {
    return arrStr.sort(function(a,b) {
        // HTF does this work?
        return b.length - a.length;
    });
};

function sum(total, num) {
    return total + num;
}

function sumArr(arrNum) {
    return arrNum.reduce(sum)
}


function sortSums(matrixNumbers) {
    return matrixNumbers.sort(function(x, y) {
        //WTF is this?
        return x.reduce(sum) - y.reduce(sum);
    })
}

function helloWorld() {
    console.log("Hello World!");
}

function call3Times(fun) {
    fun(); 
    fun(); 
    fun(); 
}

function callNTimes(num, fun) {
    for (num; num > 0; num--) {
        fun();
    };
}

var numbers = [-276, 5, 7,32, -12, 15, 17, 992, 137, 11, 42, 12, 0, -4]
var cities = [
    { name: 'Los Angeles', temperature: 60.0},
    { name: 'Atlanta', temperature: 52.0 },
    { name: 'Detroit', temperature: 48.0 },
    { name: 'New York', temperature: 80.0 } ];

var people = [ 'Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur', 'Jason', 'Che', 'Ben' ];

var nestedNumbers = [
    [1, 3, 4],
    [2, 4, 6, 8],
    [3, 6] ];

var sumNumbers = [1, 2, 3]

console.log(findPositiveNumbers(numbers))
console.log(findEvenNumbers(numbers))
console.log(squareNumbers(numbers))
console.log(findHotCities(cities))
console.log(findCityNames(cities))
console.log(sortAlpha(people))
console.log(sortLength(people))
console.log(sortSums(nestedNumbers))
call3Times(helloWorld)
callNTimes(5, helloWorld)
console.log(sumArr(sumNumbers))




