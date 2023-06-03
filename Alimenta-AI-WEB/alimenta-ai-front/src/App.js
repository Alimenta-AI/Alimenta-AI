import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Cadastro from './Paginas/Clientes/Cadastro/Cadastro';
import Login from './Paginas/Clientes/Login/Login';
import { Navbar, Footer } from './Componentes/Imports';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/cadastro" element={<Cadastro />} />
        <Route path="/login" element={<Login />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
