import axios from 'axios'

export const api = axios.create({
	baseURL:	'http://192.168.199.9:8001'
})
