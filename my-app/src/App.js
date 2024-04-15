import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom'; // Cambiado el import para adaptarse a la versión 6
import "./App.css";

import Alumnos from "./components/Alumnos/Alumnos";
import NuevoAlumno from "./components/NuevoAlumno/NuevoAlumno";
import CRUDPeliculas from './components/Peliculas/CRUDPeliculas';
import CRUDClientes from './components/Clientes/CRUDClientes';
import CRUDRentas from './components/Rentas/CRUDRentas';


function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/clientes">Clientes</Link>
            </li>
            <li>
              <Link to="/peliculas">Películas</Link>
            </li>
            <li>
              <Link to="/rentas">Rentas</Link>
            </li>
          </ul>
        </nav>

        <Routes> {/* Cambiado de Route a Routes */}
          <Route path="/clientes" element={<CRUDClientes />} /> {/* Cambiado de component a element */}
          <Route path="/peliculas" element={<CRUDPeliculas />} /> {/* Cambiado de component a element */}
          <Route path="/rentas" element={<CRUDRentas />} /> {/* Cambiado de component a element */}
        </Routes> {/* Cambiado de Route a Routes */}
      </div>
    </Router>
  );
}

export default App;

//function App() {
    // const [peliculas, setPeliculas] = useState([
// 	{ id: 1, title: "Spiderman", director: "Sam R." },
// 	{ id: 2, title: "Batman", director: "Tim Burton" },
// 	{ id: 3, title: "Inception", director: "Christopher Nolan", inventario: 4 },
//     ]);
//     const [clientes, setClientes] = useState([]);
//     const [peliculas, setPeliculas] = useState([]);
//     const [rentas, setRentas] = useState([]);
//     const [alumnos, setAlumnos] = useState([
// 	{
// 	    nombre: "Fernando",
// 	    apellido: "Fong",
// 	    numCta: 313320679,
// 	},
// 	{
// 	    nombre: "Valeria",
// 	    apellido: "Garcia",
// 	    numCta: 314006088,
// 	},
// 	{
// 	    nombre: "Erick",
// 	    apellido: "Martinez",
// 	    numCta: 414890123,
// 	},
//     ]);

//     const agregarAlumno = (alumno) => {
// 	const nuevoAlumno = [alumno, ...alumnos];
// 	setAlumnos(nuevoAlumno);
// 	console.log(nuevoAlumno);
//     };

//     return (
// 	<div className="App">
// 	    <NuevoAlumno onAgregarAlumno={agregarAlumno} />
// 	    <Alumnos alumnos={alumnos} />
// 	</div>
//     );
// }


