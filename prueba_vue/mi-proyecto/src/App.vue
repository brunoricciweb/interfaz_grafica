<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'

import ProductCard from './components/ProductCard.vue'

function mostrarEmisor(nombre){ // muestra cuál componente emitió el evento "product-click"
  console.log('se hizo click en: ', nombre);
}

const productList = [
  {
    nombre: 'Pantalon',
    precio: 123
  },
  {
    nombre: 'Camisa',
    precio: 234
  }
]

</script>

<template>

  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="Hola qué tal?" />
    </div>
  </header>

  <ProductCard v-for="product in productList"
    v-bind:nombre="product.nombre" 
    v-bind:precio="product.precio" 
    :key="product.nombre" 
    v-on:product-click="mostrarEmisor"
  />
 


  <!-- <ProductCard nombre="Pantalón" precio="1234.45" v-on:product-click="mostrarEmisor" ></ProductCard>
  <ProductCard nombre="Camisa" precio="567.45" v-on:product-click="mostrarEmisor"></ProductCard> -->
  
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
