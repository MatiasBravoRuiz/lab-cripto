const express = require('express')
const app = express()
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const { rejects } = require('assert')

//Connect to db:
mongoose.connect('mongodb+srv://test:test@cluster0.yhpvb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', () => console.log('conected to db'))

app.use(bodyParser.json())

var Schema = mongoose.Schema

var infoPDF = new Schema({
    ip: String,
    operatingSystem: String
})

var infoPDFModel = mongoose.model('infoPDF', infoPDF)

//Routes:
app.get('/', (req, res) => {
    try{
        const posts = infoPDF.find()
        res.json(posts)
    }catch(err){
        res.json({message:err})
    }
})

app.post('/', (req, res) => {
    var infoPDF = new infoPDFModel({
        ip: req.body.ip,
        operatingSystem: req.body.operatingSystem
    })
    infoPDF.save()
        .then(data => {
            res.json(data)
        })
})

//Open server:
app.listen(3000)