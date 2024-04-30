import icmp from 'icmp'
import net from 'net'

export async function ping(host) {
	try {
		const res = await icmp.send(host)
		return res.open
	} catch (err) {
		return false
	}
}

export async function tcp_scan(host) {
	try {
		const sock = new Socket()
	} catch (err) {
		
	}
}
