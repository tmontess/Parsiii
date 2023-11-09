<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container">
    <a class="navbar-brand" href="#">Parsii</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto" >
        <li class="nav-item mx-2">
          <router-link class="btn btn-primary" aria-current="page" to="/">Home</router-link>
        </li><li class="nav-item mx-2">
          <router-link class="btn btn-primary" aria-current="page" to="/QuienesSomos">Quienes somos</router-link>
        </li>
        <li class="nav-item mx-2">
          <router-link class="btn btn-primary" aria-current="page" to="/servicios">Servicios</router-link>
        </li>
        <li class="nav-item mx-2">
          <router-link class="btn btn-primary" aria-current="page" to="/Clientes">Clientes</router-link>
        </li>
        <li class="nav-item mx-2">
          <router-link class="btn btn-primary" aria-current="page" to="/QuienesSomos">Experiencia</router-link>
        </li>
        <li class="nav-item">
          <router-link class="btn btn-success" to="/create">Contacto</router-link>
        </li>
      
      </ul>
    </div>
  </div>
</nav>
</template>

<script>
export default {

}
</script>

<style>
.text-style{
  font-size: 30px !important; /*desactiva las reglas en cascada*/
  font-family: fantasy !important;
  color: brown;
}
</style>