<template>
  <div class="container mt-5">
    <!-- Sección 1: Servicio 1 -->
    <div class="service-section">
      <img src="../assets/imagenes/pc.png" alt="Servicio 1" @click="redirectToServicio1" />
      <h3>Servicio 1</h3>
      <p>Descripción del servicio 1.</p>
    </div>

    <!-- Sección 2: Servicio 2 -->
    <div class="service-section">
      <img src="../assets/imagenes/producto.jpeg" alt="Servicio 2" @click="redirectToServicio2" />
      <h3>Servicio 2</h3>
      <p>Descripción del servicio 2.</p>
    </div>

    <!-- Sección 3: Servicio 3 -->
    <div class="service-section">
      <img src="../assets/imagenes/producto.jpeg" alt="Servicio 3" @click="redirectToServicio3" />
      <h3>Servicio 3</h3>
      <p>Descripción del servicio 3.</p>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    redirectToServicio1() {
      // Redirige a la página del Servicio 1
      this.$router.push('/servicio-1');
    },
    redirectToServicio2() {
      // Redirige a la página del Servicio 2
      this.$router.push('/servicio-2');
    },
    redirectToServicio3() {
      // Redirige a la página del Servicio 3
      this.$router.push('/servicio-3');
    },
  },
};
</script>

<style>
.service-section {
  text-align: center;
  margin: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.service-section img {
  width: 150px; /* Ajusta el tamaño de la imagen según tus necesidades */
  cursor: pointer; /* Cambia el cursor al pasar sobre la imagen */
}

.service-section h3 {
  font-size: 20px;
}

.service-section p {
  font-size: 16px;
}
</style>
