const express = require('express')
const app = express()
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const { rejects } = require('assert')

//Connect to db:
mongoose.connect('mongodb+srv://test:test@lab.ttvkd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', () => console.log('conected to db'))

app.use(bodyParser.json())

var Schema = mongoose.Schema

var infoPDF = new Schema({
    ip: String,
    operatingSystem: String,
    version: String,
    password: String
})

var infoPDFModel = mongoose.model('infoPDF', infoPDF)

//Routes:
app.get('/', (req, res) => {
    infoPDFModel.find({}, (err, data) => {
        res.json(data)
    })
})

app.post('/', (req, res) => {
    var infoPDF = new infoPDFModel({
        ip: req.body.ip,
        operatingSystem: req.body.operatingSystem,
        version: req.body.version,
        password: req.body.password
    })
    infoPDF.save()
        .then(data => {
            res.json(data)
        })
})

//Open server:
app.listen(3000)