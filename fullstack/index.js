require("dotenv").config();

const express = require("express");
const {connectDB} = require("./db/connectDB");
const port = process.env.PORT || 8080;

const app = express();



connectDB();

app.listen(port, ()=>{
    console.log(`listening on port ${port}`);
})