const http = require("http"); 
const express = require("express"); 
const fetch = require('node-fetch');
const path = require("path"); 
const app = express();
require('dotenv').config();
app.set('view engine', 'ejs'); 
app.set("views", path.join(__dirname, `/views`)); 
const port =  5000;
const apiUrl1 = "https://cloud.iexapis.com/stable/stock/";
const apiUrl2 = "/stats?token="+process.env.iexapis;
let LastRequest =  new Date(new Date() - 60000);
let companies = [
{stock:'AAPL',marketcap:0},
{stock:'MSFT',marketcap:0},
{stock:'AMZN',marketcap:0},
{stock:'GOOGL',marketcap:0},
{stock:'FB',marketcap:0},
{stock:'BRK.A',marketcap:0},
{stock:'TSLA',marketcap:0},
{stock:'TSLA',marketcap:0},
{stock:'TSM',marketcap:0},
{stock:'TCEHY',marketcap:0},
{stock:'NVDA',marketcap:0},
{stock:'V',marketcap:0},
{stock:'JPM',marketcap:0},
{stock:'JNJ', marketcap:0},
];

app.get("/",(req,res)=> {
    let now = new Date();
    let difference = now.getTime() - LastRequest.getTime(); // This will give difference in milliseconds
    let resultInMinutes = Math.round(difference / 1000);
    if (resultInMinutes > 60) {
        console.log("it's been a minute. call the api")
        LastRequest = new Date();
        let AllQuotes = [];
        companies.map(c=> {
	    console.log(apiUrl1 + c.stock + apiUrl2);
            AllQuotes.push(fetch(apiUrl1 + c.stock + apiUrl2)
            .then(j=> j.json())
            .then(data => {
                return {stock:c.stock,marketcap:data.marketcap};
            })); // end of fetch  
        }); // end of loop

        Promise.all(AllQuotes).then((mc)=> {
            companies = mc.sort((a,b)=> (a.marketcap < b.marketcap)? 1 : -1);
            res.render('./index.ejs', {stocks:companies});
            //mc.map(c=> {res.write(c.stock+"="+Number(c.marketcap).toLocaleString()+"\n")});
            res.end();
        })
        .catch(error => { 
            res.end(error.message)
        });
    } else {
        console.log("it's been less",resultInMinutes)
        res.render('./index.ejs', {stocks:companies});
        res.end();
    }


});


app.use(express.static(__dirname + "/"));
var server = http.createServer(app); 
server.listen(port); // Point it to the port we defined above.
console.log("ready at port "  +port);
