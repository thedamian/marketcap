const http = require("http"); 
const express = require("express"); 
const fetch = require('node-fetch');
const app = express();
app.set('view engine', 'ejs'); 
const port =  5000; ;
const apiUrl1 = "https://cloud.iexapis.com/stable/stock/";
const apiUrl2 = "/stats?token=sk_df682fa87ed248bf9179a225c11c5ffc";
const companies = ['AAPL',
'MSFT',
'AMZN',
'GOOGL',
'FB',
'BRK.A',
'BABA',
//'SEHK: 700',
'JPM',
'JNJ'
]

app.get("/",(req,res)=> {
    let AllQuotes = [];
    companies.map(c=> {
       AllQuotes.push(fetch(apiUrl1 + c + apiUrl2)
        .then(j=> j.json())
        .then(data => {
            return {stock:c,marketcap: data.marketcap};
        })); // end of fetch  
    }); // end of loop

    Promise.all(AllQuotes).then((mc)=> {
        mc = mc.sort((a,b)=> (a.marketcap < b.marketcap)? 1 : -1);
        res.render('./index.ejs', {stocks:mc});
        //mc.map(c=> {res.write(c.stock+"="+Number(c.marketcap).toLocaleString()+"\n")});
        res.end();
    })
    .catch(error => { 
        res.end(error.message)
      });

});


app.use(express.static(__dirname + "/"));
var server = http.createServer(app); 
server.listen(port); // Point it to the port we defined above.
console.log("ready at port "  +port);