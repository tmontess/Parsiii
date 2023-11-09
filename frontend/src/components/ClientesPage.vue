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
      <!-- Tu contenido principal aquí -->
    </div>

    <div class="deportes-titles">
      <h1>NUESTROS CLIENTES</h1>
    </div>

    <section class="historia" id="container-aside">
      <div class="clientes-grid">
        <div class="cliente-box">
          <h2>Alvear Icon</h2>
          <img src="../assets/imagenes/Alvearicon.jpeg" alt="Alvear Icon">
          <p>Puerto Madero, Buenos Aires.</p>
        </div>

        <div class="cliente-box">
          <h2>Alvear Palace</h2>
          <img src="../assets/imagenes/palace-1.jpg" alt="Alvear Palace">
          <p>Recoleta, Buenos Aires.</p>
        </div>

        <div class="cliente-box">
          <h2>Sanatorio Otamendi</h2>
          <img src="../assets/imagenes/otamendii.png" alt="Sanatorio Otamendi">
          <p>Recoleta, Buenos Aires.</p>
        </div>

        <div class="cliente-box">
          <h2>Vuelta de Obligado 2237</h2>
          <img src="../assets/imagenes/VUELTA-DE-OBLIGADO-2237-1-scaled.jpg" alt="Vuelta de Obligado 2237">
          <p>Belgrano, Buenos Aires.</p>
        </div>
      </div>
    </section>

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

<style>
.footer {
  background-color: #333;
  color: #fff;
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

.clientes-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  padding: 20px;
}

.cliente-box {
  text-align: center;
}

.cliente-box h2 {
  font-size: 18px;
}

.cliente-box img {
  max-width: 100%;
}

.footer-nav {
text-align: center;
}
</style>

<script>
export default {
// Tu lógica de componentes aquí
}
</script>