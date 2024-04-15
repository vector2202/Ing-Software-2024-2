import React, { useState } from 'react';
import './CRUDClientes.css'; // Importar archivo de estilos CSS

function CRUDClientes() {
  const [clientes, setClientes] = useState([]);
  const [nuevoCliente, setNuevoCliente] = useState({
    nombre: '',
    apellidoPaterno: '',
    apellidoMaterno: '',
    email: '',
    contraseña: '',
    fotoPerfil: '',
    esSuperUsuario: false
  });
  const [clienteEditado, setClienteEditado] = useState(null);

  const agregarCliente = () => {
    if (nuevoCliente.nombre && nuevoCliente.apellidoPaterno && nuevoCliente.apellidoMaterno && nuevoCliente.email && nuevoCliente.contraseña) {
      setClientes([...clientes, nuevoCliente]);
      setNuevoCliente({
        nombre: '',
        apellidoPaterno: '',
        apellidoMaterno: '',
        email: '',
        contraseña: '',
        fotoPerfil: '',
        esSuperUsuario: false
      });
    } else {
      alert('Por favor, complete todos los campos.');
    }
  };

  const eliminarCliente = (id) => {
    setClientes(clientes.filter((cliente, index) => index !== id));
  };

  const editarCliente = () => {
    if (clienteEditado && clienteEditado.nombre && clienteEditado.apellidoPaterno && clienteEditado.apellidoMaterno && clienteEditado.email && clienteEditado.contraseña) {
      const nuevosClientes = [...clientes];
      nuevosClientes[clienteEditado.id] = clienteEditado;
      setClientes(nuevosClientes);
      setClienteEditado(null);
    } else {
      alert('Por favor, complete todos los campos.');
    }
  };

  const activarEdicion = (id, cliente) => {
    setClienteEditado({ id, ...cliente });
  };

  return (
    <div className="crud-clientes-container"> {/* Utilizar la clase CSS correspondiente */}
      <h2 className="crud-clientes-header">Clientes</h2> {/* Utilizar la clase CSS correspondiente */}
      <ul className="crud-clientes-list"> {/* Utilizar la clase CSS correspondiente */}
        {clientes.map((cliente, index) => (
          <li key={index} className="crud-clientes-item"> {/* Utilizar la clase CSS correspondiente */}
            <div>
              <strong>Nombre:</strong> {cliente.nombre} {cliente.apellidoPaterno} {cliente.apellidoMaterno}
            </div>
            <div>
              <strong>Email:</strong> {cliente.email}
            </div>
            <div>
              <strong>Foto de Perfil:</strong> {cliente.fotoPerfil}
            </div>
            <div>
              <strong>Es Super Usuario:</strong> {cliente.esSuperUsuario ? 'Sí' : 'No'}
            </div>
            <button onClick={() => eliminarCliente(index)} className="crud-clientes-button">Eliminar</button> {/* Utilizar la clase CSS correspondiente */}
            <button onClick={() => activarEdicion(index, cliente)} className="crud-clientes-button">Editar</button> {/* Utilizar la clase CSS correspondiente */}
          </li>
        ))}
      </ul>

      <h2>Agregar Cliente</h2>
      <div>
        <label>Nombre:</label>
        <input type="text" value={nuevoCliente.nombre} onChange={(e) => setNuevoCliente({ ...nuevoCliente, nombre: e.target.value })} className="crud-clientes-input" /> {/* Utilizar la clase CSS correspondiente */}
      </div>
      <div>
        <label>Apellido Paterno:</label>
        <input type="text" value={nuevoCliente.apellidoPaterno} onChange={(e) => setNuevoCliente({ ...nuevoCliente, apellidoPaterno: e.target.value })} className="crud-clientes-input" /> {/* Utilizar la clase CSS correspondiente */}
      </div>
      <div>
        <label>Apellido Materno:</label>
        <input type="text" value={nuevoCliente.apellidoMaterno} onChange={(e) => setNuevoCliente({ ...nuevoCliente, apellidoMaterno: e.target.value })} className="crud-clientes-input" /> {/* Utilizar la clase CSS correspondiente */}
      </div>
      <div>
        <label>Email:</label>
        <input type="email" value={nuevoCliente.email} onChange={(e) => setNuevoCliente({ ...nuevoCliente, email: e.target.value })} className="crud-clientes-input" /> {/* Utilizar la clase CSS correspondiente */}
      </div>
      <div>
        <label>Contraseña:</label>
        <input type="password" value={nuevoCliente.contraseña} onChange={(e) => setNuevoCliente({ ...nuevoCliente, contraseña: e.target.value })} className="crud-clientes-input" /> {/* Utilizar la clase CSS correspondiente */}
      </div>
      <div>
        <label>Foto de Perfil:</label>
        <input type="file" value={nuevoCliente.fotoPerfil} onChange={(e) => setNuevoCliente({ ...nuevoCliente, fotoPerfil: e.target.value })} className="crud-clientes-input" /> {/* Utilizar la clase CSS correspondiente */}
      </div>
      <div>
        <input type="checkbox" checked={nuevoCliente.esSuperUsuario} onChange={(e) => setNuevoCliente({ ...nuevoCliente, esSuperUsuario: e.target.checked })} />
        <label>Es Super Usuario</label>
      </div>
      <button onClick={agregarCliente} className="crud-clientes-button">Agregar</button> {/* Utilizar la clase CSS correspondiente */}

      {clienteEditado && (
        <div>
          <h2>Editar Cliente</h2>
          <div>
            <label>Nombre:</label>
            <input type="text" value={clienteEditado.nombre} onChange={(e) => setClienteEditado({ ...clienteEditado, nombre: e.target.value })} className="crud-clientes-input" /> {/* Utilizar la clase CSS correspondiente */}
          </div>
          <div>
            <label>Apellido Paterno:</label>
            <input type="text" value={clienteEditado.apellidoPaterno} onChange={(e) => setClienteEditado({ ...clienteEditado, apellidoPaterno: e.target.value })} className="crud-clientes-input" /> {/* Utilizar la clase CSS correspondiente */}
          </div>
          <div>
            <label>Apellido Materno:</label>
            <input type="text" value={clienteEditado.apellidoMaterno} onChange={(e) => setClienteEditado({ ...clienteEditado, apellidoMaterno: e.target.value })} className="crud-clientes-input" /> {/* Utilizar la clase CSS correspondiente */}
          </div>
          <div>
            <label>Email:</label>
            <input type="email" value={clienteEditado.email} onChange={(e) => setClienteEditado({ ...clienteEditado, email: e.target.value })} className="crud-clientes-input" /> {/* Utilizar la clase CSS correspondiente */}
          </div>
          <div>
            <label>Contraseña:</label>
            <input type="password" value={clienteEditado.contraseña} onChange={(e) => setClienteEditado({ ...clienteEditado, contraseña: e.target.value })} className="crud-clientes-input" /> {/* Utilizar la clase CSS correspondiente */}
          </div>
          <div>
            <label>Foto de Perfil:</label>
            <input type="file" value={clienteEditado.fotoPerfil} onChange={(e) => setClienteEditado({ ...clienteEditado, fotoPerfil: e.target.value })} className="crud-clientes-input" /> {/* Utilizar la clase CSS correspondiente */}
          </div>
          <div>
            <input type="checkbox" checked={clienteEditado.esSuperUsuario} onChange={(e) => setClienteEditado({ ...clienteEditado, esSuperUsuario: e.target.checked })} />
            <label>Es Super Usuario</label>
          </div>
          <button onClick={editarCliente} className="crud-clientes-button">Guardar</button> {/* Utilizar la clase CSS correspondiente */}
        </div>
      )}
    </div>
  );
}

export default CRUDClientes;
