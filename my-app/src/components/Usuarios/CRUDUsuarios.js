import React, { useState } from 'react';
import CRUDClientes from './CRUDUsuarios';
import CRUDPeliculas from '../Peliculas/CRUDPeliculas';
import CRUDRentas from '../Rentas/CRUDRentas';

function Usuarios() {
  // Estado para almacenar la lista de clientes
  const [clientes, setClientes] = useState([]);
  const [nuevoCliente, setNuevoCliente] = useState('');
  const [clienteEditado, setClienteEditado] = useState(null);

  // Funciones CRUD para clientes
  const agregarCliente = () => {
    setClientes([...clientes, nuevoCliente]);
    setNuevoCliente('');
  };

  const eliminarCliente = (id) => {
    setClientes(clientes.filter((cliente, index) => index !== id));
  };

  const editarCliente = (id, nuevoNombre) => {
    const nuevosClientes = [...clientes];
    nuevosClientes[id] = nuevoNombre;
    setClientes(nuevosClientes);
    setClienteEditado(null);
  };

  const activarEdicionCliente = (id, nombreCliente) => {
    setClienteEditado({ id, nombreCliente });
  };

  // Resto del CRUD para Películas y Rentas

  return (
    <div>
      {/* CRUD para clientes */}
      <h2>Clientes</h2>
      <CRUDClientes />

      {/* CRUD para películas */}
      <h2>Películas</h2>
      <CRUDPeliculas />

      {/* CRUD para rentas */}
      <h2>Rentas</h2>
      <CRUDRentas />
    </div>
  );
}

export default Usuarios;
