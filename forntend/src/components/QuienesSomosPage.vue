<template>
  <div>
    <header class="header" style="background-color: #87CEEB; text-align: center;">
      <div class="header-content">
        <nav class="header-nav">
          <div class="header-logo">
            <img src="{{ url_for('static', filename='assets/imagenes/LOGO.png') }}" alt="escudo" width="70" height="70">
          </div>
          <div class="header-btns" id="show-menu">
            <ul class="nav-menu" style="list-style: none; padding: 0; display: flex; justify-content: space-around;">
              <li><a href="/" style="text-decoration: none; color: black;">Home</a></li>
              <li><a href="/quienes-somos" style="text-decoration: none; color: black;">Quiénes somos</a></li>
              <li><a href="/#title-Servicios" style="text-decoration: none; color: black;">Servicios</a></li>
              <li><a href="/clientes" style="text-decoration: none; color: black;">Clientes</a></li>
              <li><a href="/experience" style="text-decoration: none; color: black;">Experiencia</a></li>
              <li><a href="/contacto" style="text-decoration: none; color: black;">Contacto</a></li>
            </ul>
          </div>
        </nav>
      </div>
      <div class="header-card">
        <div class="container-header-card">
          <img src="parsii baner.jpeg" alt="foto-equipos" width="100%">
        </div>
      </div>
      <div id="icon-menu">
        <i class="fas fa-bars"></i>
      </div>
    </header>

    <div class="container-all" id="move-content"></div>

    <main>
      <div class="deportes-titles" style="background-color: #87CEEB; font-family: 'Arial'; color: black; text-align: left; padding: 10px; margin-left: 5%;">
        <h1 style="font-weight: bold; background-color: #87CEEB; color: black; padding: 10px; display: inline;">PARSII</h1>
      </div>
      <section class="historia" id="container-aside" style="text-align: left; margin-left: 5%;">
        <div class="el-club-div1">
          <h2 style="background-color: #87CEEB; color: black; font-weight: bold; padding: 10px;">Quienes Somos - Solución integral de gestión para estacionamientos</h2> <br>
          <div class="text-box" style="background-color: #87CEEB; color: black; padding: 5px;">
            <h3 style="font-weight: bold; background-color: #87CEEB; color: black; padding: 5px;">Lo que hacemos</h3>
            <p>
              Parsii es el software de gestión para estacionamientos más completo del mercado latinoamericano.
              <br> <br>
              Al instante, con Parsii podrás controlar toda la operatoria de tu estacionamiento en tiempo real.
              <br> <br>
              Herramientas de trabajo: Proporcionamos herramientas para facilitar el trabajo de tus empleados y mejorar
              la experiencia de tus clientes.
              <br> <br>
              Tecnología: Mediante nuestra tecnología mejoramos el control para reducir el fraude y maximizar el
              rendimiento de tu negocio.
            </p>
          </div>
        </div>
        <div>
          <img src="Images/IMAGES PARSII/Captura de pantalla 2023-06-12 a la(s) 16.41.47.png" alt="foto-club" width="500px">
        </div>
      </section>

      <section>
        <div class="el-club-div2" style="background-color: #87CEEB; font-family: 'Arial'; color: black; padding: 10px; margin-left: 5%;">
          <p>
            Reemplazamos viejos sistemas operativos que son obsoletos, tienen altos costos de reparación y que generan
            dependencia.
          </p>
        </div>
      </section>
    </main>

    <footer class="footer" style="background-color: #87CEEB; font-family: 'Arial'; color: black; padding: 20px 0; text-align: center;">
      <div class="footer-content">
        <div class="footer-logo">
          <img src="Images/LOGO.png" alt="escudo" width="80px" height="80px">
        </div>
        <div class="footer-info">
          <h1 class="title-footer" style="font-size: 24px; font-weight: bold; background-color: #87CEEB; color: black; padding: 10px; margin-bottom: 10px;">Parsii Estaciona Rapido</h1>
          <div class="menu-footer" style="background-color: #87CEEB; color: black;">
            <ul>
              <li><a href="index.html" style="text-decoration: none; color: black;">Home</a></li>
              <li><a href="forms-contacto.html" style="text-decoration: none; color: black;">Cómo Llegar</a></li>
              <li><a href="forms-contacto.html" style="text-decoration: none; color: black;">Contacto</a></li>
            </ul>
          </div>
          <p class="p-footer" style="font-size: 14px; line-height: 1.5;">
            <strong>Dirección:</strong> Ing. Enrique Butty 275, C1001 CABA<br>
            <strong>Teléfono:</strong> 2923 45-8661
          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

