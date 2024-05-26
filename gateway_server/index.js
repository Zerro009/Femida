import dotenv from 'dotenv'
import express from 'express'
import axios from 'axios'

dotenv.config()

const app = express()

const PROD = process.env.PROD
const PORT = PROD ? process.env.PORT : 8000
const registry_server = PROD ?
	`http://${process.env.REGISTRY_SERVER_HOST}:${process.env.REGISTRY_SERVER_PORT}/` :
	`http://localhost:8001/`

app.use(express.json())
app.use(express.urlencoded({
	extended: true,
}))

app.use(async (req, res, next) => {
	const path = req.path

	let service = {}

	try {
		const response = await axios.get(
			`${registry_server}services/detail/`,
			{
				params: 
				{
					path: path
				},
			}
		)

		service = response.data
	} catch (err) {
		res.status(404).send('Not found')
	}
  
	const url = `http://${service.host}:${service.port}${path}`
	try {
		const response = await axios({
			url:		url,
			method:		req.method,
			params:		req.query,
			data:		req.body,
		})
		res.status(response.status).send(response.data)
	} catch (err) {
		res.status(404)
	}
})

app.listen(PORT, () => console.log(`Server is running on port ${PORT}`))
