<script setup>
defineProps({
  nombre: {
    type: String,
    required: true,
  },
  precio: {
    type: Number,
    required: true,
  }
})



</script>

<template>
  <link rel="stylesheet" href="https://icons.getbootstrap.com/assets/font/bootstrap-icons.min.css"> 
  <div class="main-container">
        <div class="img-container">
            <div class="box img-btn left"></div>
            <div class="box img-btn right"></div>
            <img src="https://acdn.mitiendanube.com/stores/001/333/138/products/rem-rojo1-3c3a10a972a3f9e21e16957472045682-640-0.png" alt="">
        </div>  

        <div class="horiz-section">
            <p class="product-name">{{nombre}}</p>
            <div class="product-prices">
                <p class="price primary">$ {{precio}}</p>
                <p class="price secondary">$ 4.56</p>
            </div>
        </div>

        <div class="horiz-section spoiler hidden" >
            <p>Remera de 100% algodón, ajuste regular, extra suave.</p>
        </div>

        <div class="horiz-section">
            <div class="color-selection">
                <div value="red" class="selector red"></div>
                <div value="green" class="selector green"></div>
                <div value="blue" class="selector blue"></div>
            </div>

            <div class="size-selection">
                <div class="selector">S</div>
                <div class="selector">M</div>
                <div class="selector">L</div>
            </div>
        </div>

        <div class="horiz-section">
            <div class="rating-section">
                <i class="bi bi-star"></i>
                <p>4.8</p>                
            </div>

            <div class="buy-btn" v-on:click="$emit('product-click', this.nombre)">
                <p> BUY + </p>
            </div>
        </div>
    </div>  

  <!-- <div>
    <h2>Mi componente!</h2>
    <p>Nombre: {{nombre}} </p>
    <p>Precio: {{precio}} </p>
  </div> -->

</template>

<style scoped>
  body{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: rgb(29, 29, 29);
}

.main-container{
    min-height: 450px;
    min-width: 300px;
    width:300px;
    border-radius: 15px;

    display: flex;
    flex-direction: column;
    box-shadow: 3px 3px 10px rgb(173, 173, 173);
}

.img-container{
    height: 300px;
    border-radius: 15px;
    position: relative;
    overflow: hidden;
    text-align: center;
}

.img-container>img{
    height:fit-content;
    width: 100%;
}

.img-btn{
   position: absolute; 
   top:15px;
}
.img-btn.left{
    left: 15px;
}
.img-btn.right{
    right: 15px;
}

div{
    /* border: 0.5px dashed blue; */
}

.horiz-section{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-inline: 10px;
    margin: 5px;
}

p{
    margin:0px;
}

.product-name{
    max-width: 60%;
    padding-left: 5px;
    font-weight: bold;
    font-size: 20px;
}

.product-prices{
    width: auto;
}

p.price{
    text-align: right;
    font-weight: bold;

}
.primary{
    font-size: 25px;
    color: rgb(255, 19, 19);
}
.secondary{
    font-size: 15px;
    color: darkgray;
}

.size-selection{
    display:flex;
    flex-direction: row;
}
.selector{
    border-radius: 50%;
    border: 2px solid gray;
    width: 25px;
    height: 25px;
    margin: 3px;
    align-content: center;
    text-align: center;
}

.color-selection{
    display:flex;
}

div.color-selection>div { 
    border-width: 5px;
    width: 20px;
    height: 20px;
}

.selector.red{ color: red;border-color: red; }
.selector.green{ color: green;border-color: green; }
.selector.blue{ color: blue;border-color: blue; }
.selector.yellow{ color: yellow;border-color: yellow; }
.selector.white{ color: white;border-color: white; }
.selector.black{ color: black;border-color: black; }

.rating-section{
    display: flex;
}

.rating-section>p{
    margin-left: 7px;
}

.buy-btn>p{
    font-size: 20px;
    color: rgb(190, 41, 190);
}

div.box{
    /* width: 30px;
    height: 30px;
    border: 0.5px dashed orange; */
}

.spoiler{
    /* transition: 0.5s ease; */
}
.hidden{
    display: none;
}

</style>
