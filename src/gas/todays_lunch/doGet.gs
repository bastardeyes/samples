
function doGet() {
  var html = HtmlService.createTemplateFromFile("index");
  
  html.data = JSON.stringify({fortunelist:["大吉","中吉","小吉","末吉","吉"],
                              menulist:["肉","魚","定食","丼","米","中華","和食","洋食","イタリアン","エスニック","麺類","カレー味","ビル出て右","ビル出て左","赤いもの","白いもの","茶色いもの","黄色いもの","温かいもの","女子力高いもの","おっさん飯","居酒屋めし","からいもの","とろみがある","ビル1F","2F以上","ビル地下","ファミレス","スプーンで食う","おばちゃん店員","900円以内"]
                             });  
  return html.evaluate().setSandboxMode(HtmlService.SandboxMode.IFRAME);    
    
}

function GetCSS(filename) {
    return HtmlService.createHtmlOutputFromFile(filename).getContent();
}
