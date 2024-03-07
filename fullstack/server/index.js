require("dotenv").config();
const express = require("express");
const {connectDB} = require("./db/connectDB");
const port = process.env.PORT || 3000;
const { spawn } =require('child_process');

const app = express();

app.get('/', (req,res) =>{
    res.send("Welcome to JackOscope")
})

app.get('/recognize-card', (req,res) => {
    const pythonProcess = spawn('python',['OpenCV/CardDetector.py']);

    pythonProcess.stdout.on('data', (data) =>{
        console.log(` Python script ${data}`);
        res.send(data);
    });
});


connectDB();

app.listen(port, ()=>{
    console.log(`listening on port ${port}`);
})