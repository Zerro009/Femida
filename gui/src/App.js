import { Header } from './components/Header/Header'

import style from './app.module.css'

export const App = () => {
	return (
		<div
			className={style.app}
		>
		<Header />
		</div>
	)
}

export default App;
