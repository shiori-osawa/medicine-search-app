//idが「search-button」の検索ボタンを取得する
//const = 変わらない値を入れる箱を作る
//searchButton = 変数名
//document = 今開いているHTML全体
//getElementById = get取ってくる　Element部品　ById idを使って
const searchButton = document.getElementById("search-button");//ここではボタンを見つけるだけ
//検索中メッセージを表示する場所を取得する
const loadingMessage = document.getElementById("loading-message"); 


//点の数を入れる(点が1つ、2つと変化する) let=中身が変わるときに使う
let dots = "";
const form = document.querySelector("form");
//検索ボタンがクリックされたとき
//ここでボタンが押されたら◯◯してねという約束をしてる
form.addEventListener("submit", function () {
    loadingMessage.style.display = "block";
    setInterval(function (){
        dots += ".";

        loadingMessage.innerHTML =
            '<span class="spinner"></span>検索中' + dots;

        if (dots.length == 3){
            dots = "";
        }
    }, 1000);
   
});
