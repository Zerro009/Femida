import express from 'express'
import axios from 'axios'

const app = express()
const PORT = 8001

const registry_server = 'http://192.168.199.9:8001/'

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
		console.log(req.body)

		const response = await axios({
			url:		url,
			method:		req.method,
			params:		req.params,
			data:		req.body,
		})
		res.status(response.status).send(response.data)
	} catch (err) {
		res.status(404).send('Not found')
	}
})

app.listen(PORT, () => console.log(`Server is running on port ${PORT}`))
