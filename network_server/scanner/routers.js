import express from 'express'

import { ping_view, scan_view } from './views.js'

export const scannerRouter = express.Router()

scannerRouter.get('/ping/', async (req, res) => ping_view(req, res))

scannerRouter.all('/tcp/', async (req, res) => scan_view(req, res))
