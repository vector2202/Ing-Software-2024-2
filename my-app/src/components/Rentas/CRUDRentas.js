import React, { useState } from 'react';
import './CRUDRentas.css'; // Importar archivo de estilos CSS

function CRUDRentas() {
  const [rentas, setRentas] = useState([]);
  const [nuevaRenta, setNuevaRenta] = useState({
    idCliente: '',
    idPelicula: '',
    fecha: '',
    duracion: '',
    estatus: false
  });
  const [rentaEditada, setRentaEditada] = useState(null);

  const agregarRenta = () => {
    if (nuevaRenta.idCliente && nuevaRenta.idPelicula && nuevaRenta.fecha && nuevaRenta.duracion !== '') {
      setRentas([...rentas, nuevaRenta]);
      setNuevaRenta({
        idCliente: '',
        idPelicula: '',
        fecha: '',
        duracion: '',
        estatus: false
      });
    } else {
      alert('Por favor, complete todos los campos.');
    }
  };

  const editarRenta = (id) => {
    const nuevasRentas = [...rentas];
    nuevasRentas[id].estatus = !nuevasRentas[id].estatus;
    setRentas(nuevasRentas);
  };

  return (
    <div className="crud-rentas-container"> {/* Utilizar la clase CSS correspondiente */}
      <h2 className="crud-rentas-header">Rentas</h2> {/* Utilizar la clase CSS correspondiente */}
      <ul className="crud-rentas-list"> {/* Utilizar la clase CSS correspondiente */}
        {rentas.map((renta, index) => (
          <li key={index} className="crud-rentas-item"> {/* Utilizar la clase CSS correspondiente */}
            <div>
              <strong>ID Cliente:</strong> {renta.idCliente}
            </div>
            <div>
              <strong>ID Película:</strong> {renta.idPelicula}
            </div>
            <div>
              <strong>Fecha:</strong> {renta.fecha}
            </div>
            <div>
              <strong>Duración:</strong> {renta.duracion}
            </div>
            <div>
              <strong>Estatus:</strong> {renta.estatus ? 'Activo' : 'No activo'}
            </div>
            <button onClick={() => editarRenta(index)} className="crud-rentas-button">Cambiar Estatus</button> {/* Utilizar la clase CSS correspondiente */}
          </li>
        ))}
      </ul>

      <h2>Agregar Renta</h2>
      <div>
        <label>ID Cliente:</label>
        <input type="number" value={nuevaRenta.idCliente} onChange={(e) => setNuevaRenta({ ...nuevaRenta, idCliente: parseInt(e.target.value) })} className="crud-rentas-input" /> {/* Utilizar la clase CSS correspondiente */}
      </div>
      <div>
        <label>ID Película:</label>
        <input type="number" value={nuevaRenta.idPelicula} onChange={(e) => setNuevaRenta({ ...nuevaRenta, idPelicula: parseInt(e.target.value) })} className="crud-rentas-input" /> {/* Utilizar la clase CSS correspondiente */}
      </div>
      <div>
        <label>Fecha:</label>
        <input type="date" value={nuevaRenta.fecha} onChange={(e) => setNuevaRenta({ ...nuevaRenta, fecha: e.target.value })} className="crud-rentas-input" /> {/* Utilizar la clase CSS correspondiente */}
      </div>
      <div>
        <label>Duración:</label>
        <input type="text" value={nuevaRenta.duracion} onChange={(e) => setNuevaRenta({ ...nuevaRenta, duracion: e.target.value })} className="crud-rentas-input" /> {/* Utilizar la clase CSS correspondiente */}
      </div>
      <button onClick={agregarRenta} className="crud-rentas-button">Agregar</button> {/* Utilizar la clase CSS correspondiente */}
    </div>
  );
}

export default CRUDRentas;
