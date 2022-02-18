const express = require("express")
const app = express()

app.get('/', (req, res) => {
  console.log(req.originalUrl)
  res.send("res")
})
app.listen(8080, () => {
  console.log("Proxy is running at http://localhost:8080")
})
