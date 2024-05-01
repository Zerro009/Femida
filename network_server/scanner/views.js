import icmp from 'icmp'
import net from 'net'

export async function ping_view(req, res) {
	const host = req.query['host']
	const data = {}
	try {
		const res = await icmp.send(host)
		data['status'] = res.open ? 'up' : 'down' 
	} catch (err) {
		data['status'] = 'down'
	}
	res.send(data)
}

export async function scan_view(req, res) {
	const host = req.query['host']
	const from = req.query['from']
	const to = req.query['to']
	const data = {}

	for (let port = from; port <= to; port++) {
		const sock = new net.Socket()

		await new Promise((resolve, reject) => {
			sock.connect(port, host, () => {
				data[port] = 'open'
				sock.end()
				resolve()
			})

			sock.on('error', err => {
				sock.end()
				resolve()
			})
		})	
	}
	res.send(data)
}
