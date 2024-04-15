import React, { useState } from 'react';
import './CRUDPeliculas.css';

function CRUDPeliculas() {
  const [peliculas, setPeliculas] = useState([]);
  const [nuevaPelicula, setNuevaPelicula] = useState({
    titulo: '',
    genero: '',
    inventario: 0,
    duracion: 0
  });
  const [peliculaEditada, setPeliculaEditada] = useState(null);

  const agregarPelicula = () => {
    if (nuevaPelicula.titulo && nuevaPelicula.genero && nuevaPelicula.inventario && nuevaPelicula.duracion) {
      setPeliculas([...peliculas, nuevaPelicula]);
      setNuevaPelicula({
        titulo: '',
        genero: '',
        inventario: 0,
        duracion: 0
      });
    } else {
      alert('Por favor, complete todos los campos.');
    }
  };

  const eliminarPelicula = (id) => {
    setPeliculas(peliculas.filter((pelicula, index) => index !== id));
  };

  const editarPelicula = () => {
    if (peliculaEditada && peliculaEditada.titulo && peliculaEditada.genero && peliculaEditada.inventario && peliculaEditada.duracion) {
      const nuevasPeliculas = [...peliculas];
      nuevasPeliculas[peliculaEditada.id] = peliculaEditada;
      setPeliculas(nuevasPeliculas);
      setPeliculaEditada(null);
    } else {
      alert('Por favor, complete todos los campos.');
    }
  };

  const activarEdicionPelicula = (id, pelicula) => {
    setPeliculaEditada({ id, ...pelicula });
  };

  return (
    <div className="crud-peliculas-container"> {}
      <h2 className="crud-peliculas-header">Películas</h2> {}
      <ul className="crud-peliculas-list"> {}
        {peliculas.map((pelicula, index) => (
          <li key={index} className="crud-peliculas-item"> {}
            <div>
              <strong>Título:</strong> {pelicula.titulo}
            </div>
            <div>
              <strong>Género:</strong> {pelicula.genero}
            </div>
            <div>
              <strong>Inventario:</strong> {pelicula.inventario}
            </div>
            <div>
              <strong>Duración:</strong> {pelicula.duracion} minutos
            </div>
            <button onClick={() => eliminarPelicula(index)} className="crud-peliculas-button">Eliminar</button> {}
            <button onClick={() => activarEdicionPelicula(index, pelicula)} className="crud-peliculas-button">Editar</button> {}
          </li>
        ))}
      </ul>

      <h2>Agregar Película</h2>
      <div>
        <label>Título:</label>
        <input type="text" value={nuevaPelicula.titulo} onChange={(e) => setNuevaPelicula({ ...nuevaPelicula, titulo: e.target.value })} className="crud-peliculas-input" /> {}
      </div>
      <div>
        <label>Género:</label>
        <input type="text" value={nuevaPelicula.genero} onChange={(e) => setNuevaPelicula({ ...nuevaPelicula, genero: e.target.value })} className="crud-peliculas-input" /> {}
      </div>
      <div>
        <label>Inventario:</label>
        <input type="number" value={nuevaPelicula.inventario} onChange={(e) => setNuevaPelicula({ ...nuevaPelicula, inventario: parseInt(e.target.value) })} className="crud-peliculas-input" /> {}
      </div>
      <div>
        <label>Duración (minutos):</label>
        <input type="number" value={nuevaPelicula.duracion} onChange={(e) => setNuevaPelicula({ ...nuevaPelicula, duracion: parseInt(e.target.value) })} className="crud-peliculas-input" /> {}
      </div>
      <button onClick={agregarPelicula} className="crud-peliculas-button">Agregar</button> {}

      {peliculaEditada && (
        <div>
          <h2>Editar Película</h2>
          <div>
            <label>Título:</label>
            <input type="text" value={peliculaEditada.titulo} onChange={(e) => setPeliculaEditada({ ...peliculaEditada, titulo: e.target.value })} className="crud-peliculas-input" /> {}
          </div>
          <div>
            <label>Género:</label>
            <input type="text" value={peliculaEditada.genero} onChange={(e) => setPeliculaEditada({ ...peliculaEditada, genero: e.target.value })} className="crud-peliculas-input" /> {}
          </div>
          <div>
            <label>Inventario:</label>
            <input type="number" value={peliculaEditada.inventario} onChange={(e) => setPeliculaEditada({ ...peliculaEditada, inventario: parseInt(e.target.value) })} className="crud-peliculas-input" /> {}
          </div>
          <div>
            <label>Duración (minutos):</label>
            <input type="number" value={peliculaEditada.duracion} onChange={(e) => setPeliculaEditada({ ...peliculaEditada, duracion: parseInt(e.target.value) })} className="crud-peliculas-input" /> {}
          </div>
          <button onClick={editarPelicula} className="crud-peliculas-button">Guardar</button> {}
        </div>
      )}
    </div>
  );
}

export default CRUDPeliculas;
