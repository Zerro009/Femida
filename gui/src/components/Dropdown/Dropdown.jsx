import { useState } from 'react'

import style from './dropdown.module.css'

export interface iDropdown {
	children: any,
}

export const Dropdown = (i: iDropdown) => {
	const [active, setActive] = useState(false)

	return (
		<div
			onMouseEnter={() => setActive(true)}
			onMouseLeave={() => setActive(false)}
		>
			{(active) && (
			<div
				className={style.dropdown}
			>
				{i.children}
			</div>
			)}
			<div
				className={style.sensor}
			>
				...
			</div>
		</div>
		
	)
}
