import { useState } from 'react'
import { Form } from '../Form/Form'

import { api } from '../../services/auth.jsx'

import style from './signupform.module.css'

export const SignUpForm = () => {
	const data = []

	const setValue = (value) => {
		data['name'] = value
	}

	const inputs = [
		{
			label:	'Имя пользователя',
			name:	'login',
			value:	'',
			getValue: setValue
			
		},
		{
			label:	'Пароль',
			name:	'password',
			value:	'',
			type:	'password',
		},
		{
			label:	'Повторите пароль',
			name:	'passwordConfirm',
			value:	'',
			type:	'password'
		},
	]

	const onSubmit = () => {
		inputs[0].getValue()
		console.log(data)
	}

	return (
		<Form
			className={style.signupform}
			inputs={inputs}
			text='Зарегистрироваться'
			onSubmit={() => onSubmit()}
		/>
	)
}
