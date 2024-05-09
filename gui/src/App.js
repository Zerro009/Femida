import { Dropdown } from './components/Dropdown/Dropdown'
import { Form } from './components/Form/Form'

import style from './app.module.css'

export const App = () => {
	const inputs = [
		{
			label:	'Username',
			name:	'',
			value:	'',
		},
		{
			label:	'Password',
			name:	'',
			type:	'password',
			value:	'',
		}
	]

	return (
		<div
			className={style.app}
		>
			<Dropdown 
				children='HIDDEN'
			/>
			<Form
				inputs={inputs}
			/>
		</div>
	)
}

export default App;
