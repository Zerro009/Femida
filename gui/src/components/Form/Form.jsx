import { Input } from '../Input/Input'

import style from './form.module.css'

export interface iForm {
	inputs:	Array,
}

export const Form = (i: iForm) => {
	const inputs = []
	for (let input of i.inputs) {
		inputs.push(<Input {...input} />)
	}
	
	return (
		<div className={style.form}>
			{inputs}
		</div>
	)
}
