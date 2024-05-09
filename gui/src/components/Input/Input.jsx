import { useState } from 'react'

import style from './input.module.css'

export interface iInput {
	label:		String,
	name:		String,
	type:		String,
	value:		String,
}

export const Input = (i: iInput) => {
	const [value, setValue] = useState(i.value)

	const onChange = (e) => {
		e.preventDefault()
		setValue(e.target.value)
	}

	return (
		<div className={style.input}>
			<label>
				{i.label}
			</label>
			<input
				name={i.name}
				type={i.type}
				value={value}
				onChange={onChange}
			/>
		</div>
	)
}
