import express from 'express'

import { ping } from './index.js'

export const scannerRouter = express.Router()

scannerRouter.all('/ping/', async (req, res) => {
	const data = {
		'status':	await ping(req.query['host']) ? 'up' : 'down',
	}
	res.send(data)
})

scannerRouter.all('/tcp/', (req, res) => {
	console.log('tcp')
	res.send(req.path)
})
