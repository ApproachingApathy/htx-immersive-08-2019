function createHeading(heading, size) {
    var newHeading = document.createElement("h" + size);
    newHeading.textContent = heading;
    return newHeading;
}

function drwTitleBox(title, subTitle) {

}

function drwHeader(title, ...headerLinks) {
    var headerDiv = document.createElement("div");
    headerDiv.setAttribute("class", "header text-white");
    
    headerDiv.appendChild(createHeading(title, 1))
    headerDiv.appendChild(createUnorderedList("", headerLinks))
    return headerDiv;
}

function createUnorderedList(classStr,...listElements) {
    var unorderedList = document.createElement("ul");
    unorderedList.setAttribute("class", classStr);
    listElements.forEach((item)=> {
        var newListItem = document.createElement("li");
        newListItem.textContent = item;
        unorderedList.appendChild(newListItem);
    });

    return unorderedList;
}






function drwPage() {
    var container = document.getElementById("container");
    container.appendChild(drwHeader("My Blog", "Home", "Categories"))
}

drwPage()