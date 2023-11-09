<template>
    <div>
      <div class="header-card">
        <div class="container-header-card">
          <img src="../assets/imagenes/parsii baner.jpeg" alt="foto-equipos" width="100%">
        </div>
      </div>
      <div id="icon-menu">
        <i class="fas fa-bars"></i>
      </div>
  
      <div class="container-all" id="move-content">
        <div class="deportes-titles">
          <h1 class="centered-title"></h1>
        </div>
  
        <section class="historia" id="container-aside">
            <div class="container-all" id="move-content">
      <div class="deportes-titles">
        <h1 class="centered-title">NUESTROS CLIENTES DICEN</h1>
      </div>

      <section class="historia" id="container-aside">
  <div class="el-club-div1">
    <div class="cliente-box" style="background-color: #f2f2f2; padding: 10px; border-radius: 5px;">
      <p style="font-size: 18px; font-weight: bold; color: #333;">¡Únete a Parsii y maximiza tus ganancias!</p>
    </div>
    <div class="cliente-comment" style="background-color: rgba(200, 200, 200, 0.5); padding: 10px; border-radius: 5px; margin-top: 20px;">
      <div class="cliente-info">
        <img src="../assets/imagenes/abuela.png" alt="Foto Usuario 1" style="width: 50px; height: 50px; margin-right: 10px;">
        <h3 style="margin: 0;">MARIANO JASIN, ADMINISTRADOR DE ESTACIONAMIENTOS:</h3>
        <!-- Agrega las estrellas de valoración aquí -->
        <div class="valoracion">
          <span class="star">&#9733;</span>
          <span class="star">&#9733;</span>
          <span class="star">&#9733;</span>
          <span class="star">&#9733;</span>
          <span class="star">&#9733;</span>
        </div>
      </div>
      <p style="font-size: 16px; line-height: 1.5;">“Parsii realmente es una solución para mi empresa, somos una red de 18 estacionamientos y estamos muy contentos de poder tener claridad en la información de cada uno de los edificios. También, la atención al clientes es increíble. Realmente son socios nuestros y generan un valor agregado enorme (…)”</p>
    </div>
    <div class="cliente-comment" style="background-color: rgba(200, 200, 200, 0.5); padding: 10px; border-radius: 5px; margin-top: 20px;">
      <div class="cliente-info">
        <img src="../assets/imagenes/ramon.png" alt="Foto Usuario 2" style="width: 50px; height: 50px; margin-right: 10px;">
        <h3 style="margin: 0;">JORGE DE BARTOLO, SUPERVISOR DE ESTACIONAMIENTOS:</h3>
        <!-- Agrega las estrellas de valoración aquí -->
        <div class="valoracion">
          <span class="star">&#9733;</span>
          <span class="star">&#9733;</span>
          <span class="star">&#9733;</span>
          <span class="star">&#9733;</span>
          <span class="star">&#9733;</span>
        </div>
      </div>
      <p style="font-size: 16px; line-height: 1.5;">“El sistema de Parsii es una solución muy completa. Nos pasaba de tener un sistema distinto en cada estacionamiento con lo cual auditar y poder comparar era un dolor de cabeza; ni hablar de capacitar a los empleados. Una vez que unificamos todo con Parsii, el día a día se simplificó mucho y eso es muy bueno.”</p>
    </div>
  </div>
</section>
    </div>
    
        </section>
      </div>
      <footer class="footer">
      <div class="footer-content">
        <div class="footer-logo">
          <img src="../assets/imagenes/LOGO.png" alt="escudo" width="80px" height="80px">
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
  
  <style scoped>
  .header-card {
    background-color: #004aad;
    text-align: center;
  }
  
  .container-header-card {
    max-width: 100%;
  }
  
  #icon-menu {
    text-align: center;
  }
  
  .deportes-titles {
    background-color: #004aad;
    color: #00bfff;
    text-align: center;
  }
  
  .historia {
    background-color: #fff; /* Cambia el color de fondo a tu elección */
    color: #333; /* Cambia el color del texto a tu elección */
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
  