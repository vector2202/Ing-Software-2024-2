import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';

import CRUDPeliculas from './components/Peliculas/CRUDPeliculas';
import CRUDClientes from './components/Clientes/CRUDClientes';
import CRURentas from './components/Rentas/CRURentas';

function App() {
    return (
	<Router>
	    <div className="app-container">
		<header className="app-header">
		    <h1>Dead-Blockbuster</h1>
		    <nav>
			<ul className="nav-links">
			    <li>
				<Link to="/clientes" className="nav-link">Clientes</Link>
			    </li>
			    <li>
				<Link to="/peliculas" className="nav-link">Películas</Link>
			    </li>
			    <li>
				<Link to="/rentas" className="nav-link">Rentas</Link>
			    </li>
			</ul>
		    </nav>
		</header>
		<Routes>
		    <Route path="/clientes" element={<CRUDClientes />} />
		    <Route path="/peliculas" element={<CRUDPeliculas />} />
		    <Route path="/rentas" element={<CRURentas />} />
		</Routes>
	    </div>
	</Router>
    );
}

export default App;
