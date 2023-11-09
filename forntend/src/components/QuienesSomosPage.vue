<template>
    <div>
    <header class="header">
        <div class="header-content">
            <nav class="header-nav">
                <div class="header-logo">
                    <img src="{{ url_for('static', filename='images/parssi logo.jpeg') }}" alt="escudo" width="70" height="70">
                </div>
               <div class="header-btns" id="show-menu">
                <ul class="nav-menu">
                    <li><a href="/">Home</a></li>
                    <li><a href="/quienes-somos">Quiénes somos</a></li>
                    <li><a href="/#title-Servicios">Servicios</a></li>
                    <li><a href="/clientes">Clientes</a></li>
                    <li><a href="/experience">Experiencia</a></li>
                    <li><a href="/contacto">Contacto</a></li>
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
        <div class="deportes-titles">
            <h1>PARSII</h1>
        </div>
        <section class="historia" id="container-aside">
            <div class="el-club-div1">
                <h2>Quienes Somos - Solución integral de gestión para estacionamientos</h2> <br>
                <div class="text-box">
                    <h3>Lo que hacemos</h3>
                    <p>
                        Parsii es el software de gestión para estacionamientos más completo del mercado latinoamericano.
                        <br> <br>
                        Al instante, con Parsii podrás controlar toda la operatoria de tu estacionamiento en tiempo real.
                        <br> <br>
                        Herramientas de trabajo: Proporcionamos herramientas para facilitar el trabajo de tus empleados y mejorar la experiencia de tus clientes.
                        <br> <br>
                        Tecnología: Mediante nuestra tecnología mejoramos el control para reducir el fraude y maximizar el rendimiento de tu negocio.
                    </p>
                </div>
            </div>
            <div>
                <img src="Images/IMAGES PARSII/Captura de pantalla 2023-06-12 a la(s) 16.41.47.png" alt="foto-club" width="500px">
            </div>
        </section>
        
        
        <section>
            <div class="el-club-div2">
               <p>
                Reemplazamos viejos sistemas operativos que son obsoletos, tienen altos costos de reparación y que generan dependencia.. </p>
            </div>
        </section>
    </main>
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-logo">
          <img src="Images/LOGO.png" alt="escudo" width="80px" height="80px">
        </div>
        <div class="footer-info">
          <h1 class="title-footer">Parsii Estaciona Rapido</h1>
          <div class="menu-footer">
            <ul>
              <li><a href="index.html">Home</a></li>
              <li><a href="forms-contacto.html">Cómo Llegar</a></li>
              <li><a href="forms-contacto.html">Contacto</a></li>
            </ul>
          </div>
          <p class="p-footer">
            <strong>Dirección:</strong> Ing. Enrique Butty 275, C1001 CABA<br>
            <strong>Teléfono:</strong> 2923 45-8661
          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
.footer {
  background-color: #333; /* Cambia el color de fondo a tu elección */
  color: #fff; /* Cambia el color del texto a tu elección */
  padding: 20px 0;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}

.footer-logo img {
  margin-right: 20px;
}

.title-footer {
  font-size: 24px;
  margin-bottom: 10px;
}

.menu-footer ul {
  list-style: none;
  padding: 0;
  display: flex;
}

.menu-footer li {
  margin-right: 20px;
}

.p-footer {
  font-size: 14px;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .menu-footer {
    margin-top: 20px;
    display: block;
  }
}
</style>