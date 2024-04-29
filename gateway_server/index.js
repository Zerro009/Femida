import express from 'express'
import axios from 'axios'

const app = express()

const registry_server = 'http://localhost:8001/'

app.use((req, res, next) => {
	axios({
		url:		`${registry_server}${req.path}`,
		method:		req.method,
		headers:	req.headers,
	}).then((response) => {
		res.send(response.data)
	}).catch(err => {
		res.send(err.message)
	})
})

app.listen(8000)
