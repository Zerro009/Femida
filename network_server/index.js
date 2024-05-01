import os from 'os'
import express from 'express'

import { scannerRouter } from './scanner/routers.js'

const app = express()
const PORT = 8004

const router = express.Router()

app.use('/scanner/', scannerRouter);

app.listen(PORT, () => {
	if (os.userInfo().uid !== 0) {
		console.log('This server requires root privileges to run!')
		process.exit(1)
	}
	console.log(`Network server started at ${PORT} port!`)
})
