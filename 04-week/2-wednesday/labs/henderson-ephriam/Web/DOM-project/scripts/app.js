function createHeading(heading, size) {
    var newHeading = document.createElement("h" + size);
    newHeading.textContent = heading;
    return newHeading;
}

function createParagraph(str) {
    var newParagraph = document.createElement("p")
    newParagraph.textContent = str;

    return newParagraph;
}

function createTitleBox(title, subTitle) {
    var newBox = document.createElement("div");
    var newParagraph = createParagraph(subTitle);

    newBox.setAttribute("class", "title-box");

    newBox.appendChild(createHeading(title, 1));
    newBox.appendChild(newParagraph);

    return newBox;
}

function createArticleBox(articleTitle, shortText, numComments = 0, numLikes = 0) {
    var newBox = document.createElement("div")
    var articleHeading = createHeading(articleTitle, 2);
    var newParagraph = createParagraph(shortText);

    newBox.setAttribute("class", "article-box");
    newBox.appendChild(articleHeading);
    newBox.appendChild(newParagraph);
    newBox.appendChild(createSocialBar(numComments, numLikes))

    return newBox;
}

function createSocialBar(numComments, numLikes) {
    var newBar = document.createElement("div");
    var arrCommentLike = [numComments + " Comments", numLikes + " Likes"];
    newBar.setAttribute("class", "social-bar text-white");

    newBar.appendChild(createUnorderedList("", arrCommentLike));

    return newBar;
}

function createHeader(title, ...headerLinks) {
    var headerDiv = document.createElement("div");
    headerDiv.setAttribute("class", "header text-white");
    
    headerDiv.appendChild(createHeading(title, 1))
    headerDiv.appendChild(createUnorderedList("", headerLinks))
    return headerDiv;
}

function createUnorderedList(classStr, arrListElements) {
    var unorderedList = document.createElement("ul");
    unorderedList.setAttribute("class", classStr);
    arrListElements.forEach((item)=> {
        var newListItem = document.createElement("li");
        newListItem.textContent = item;
        unorderedList.appendChild(newListItem);
    });

    return unorderedList;
}

function drwPage() {
    var subTitle = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Repellendus aut dolor nesciunt id, minima, unde delectus minus veniam quas ducimus error voluptas dignissimos. Minima vel nobis sapiente blanditiis culpa dolorem sed labore est repellat omnis, in, deserunt dolorum qui itaque vero numquam facere assumenda voluptatum architecto consequatur quas fugit. Repellat explicabo aspernatur ut deleniti expedita modi, fugiat esse reiciendis nobis."

    var article1ShortText = "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Laboriosam dolorem ipsam, inventore eligendi assumenda aperiam hic! Sunt eveniet similique porro unde voluptate inventore, qui ab doloribus facilis aliquam, dicta aspernatur."

    var article2ShortText = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque hic dolore, in quam provident explicabo eligendi ipsam itaque, fugit obcaecati vel ipsum odit cum voluptate aliquid iusto ipsa repudiandae quaerat fuga nesciunt, similique ratione vitae beatae eveniet? Sequi non eveniet voluptatum nemo, nesciunt ad delectus!"

    var container = document.getElementById("container");
    container.appendChild(createHeader("My Blog", "Home", "Categories"))
    container.appendChild(createTitleBox("Title", subTitle))

    container.appendChild(createArticleBox("Article 1", article1ShortText, 10, 32))
    
    container.appendChild(createArticleBox("Article 2", article2ShortText, 0,7))
}


drwPage()