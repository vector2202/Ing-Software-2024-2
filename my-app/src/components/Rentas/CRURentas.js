import React, { useState } from 'react';
import './CRURentas.css';

function CRURentas() {
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
    <div className="crud-rentas-container"> {}
      <h2 className="crud-rentas-header">Rentas</h2> {}
      <ul className="crud-rentas-list"> {}
        {rentas.map((renta, index) => (
          <li key={index} className="crud-rentas-item"> {}
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
            <button onClick={() => editarRenta(index)} className="crud-rentas-button">Cambiar Estatus</button> {}
          </li>
        ))}
      </ul>

      <h2>Agregar Renta</h2>
      <div>
        <label>ID Cliente:</label>
        <input type="number" value={nuevaRenta.idCliente} onChange={(e) => setNuevaRenta({ ...nuevaRenta, idCliente: parseInt(e.target.value) })} className="crud-rentas-input" /> {}
      </div>
      <div>
        <label>ID Película:</label>
        <input type="number" value={nuevaRenta.idPelicula} onChange={(e) => setNuevaRenta({ ...nuevaRenta, idPelicula: parseInt(e.target.value) })} className="crud-rentas-input" /> {}
      </div>
      <div>
        <label>Fecha:</label>
        <input type="date" value={nuevaRenta.fecha} onChange={(e) => setNuevaRenta({ ...nuevaRenta, fecha: e.target.value })} className="crud-rentas-input" /> {}
      </div>
      <div>
        <label>Duración:</label>
        <input type="number" value={nuevaRenta.duracion} onChange={(e) => setNuevaRenta({ ...nuevaRenta, duracion: e.target.value })} className="crud-rentas-input" /> {}
      </div>
      <button onClick={agregarRenta} className="crud-rentas-button">Agregar</button> {}
    </div>
  );
}

export default CRURentas;
