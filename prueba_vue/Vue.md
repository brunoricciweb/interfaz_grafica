## Ejemplo usando Vue.js

### Inicializar proyecto nuevo




### Correr el proyecto


---
## Usando 2-way data binding

Esto se usa para que si una variable/parámetro se modifica en el componente padre, automáticamente se vea reflejado el cambio en la variable correspondiente en el componente hijo, y viceversa. Es decir que lo mismo se cumple si la modificación se hace en el componente hijo: se verá automáticamente reflejada en el componente padre.

### Padre.vue
```
<script setup>
import { ref } from 'vue'
import UserName from './UserName.vue'

const first = ref('John')
const last = ref('Doe')
</script>

<template class="padre">

  <h1>{{ first }} {{ last }}</h1>

  Inputs dentro del componente padre
  <br>
  <input type="text" v-model="first" />
  <input type="text" v-model="last" />
  <br><br>
  
  <UserName
    v-model:first-name="first"
    v-model:last-name="last"
  />
</template>

```
### Hijo.vue
``` 
<script setup>
const firstName = defineModel('firstName')
const lastName = defineModel('lastName')
</script>

<template>
  <div>
    Inputs del componente hijo.
    <br>
    <input type="text" v-model="firstName" />
    <input type="text" v-model="lastName" />
  </div>
</template>

<style scoped>
  div{
    border: 1px dashed red;
  }
</style>

```

https://play.vuejs.org/#eNqFkstuwjAQRX/F8iZUAqKKHQpIfbAoUmnVx86bKEzANLEt26FUkf+9Y4MDSAg2UWbu9fjckVv6oNRw2wAd08wUmitLDNhGTZngtZLakpZoKIkjpZY1SdCadNK3Ab3IazhowzQ2/ES0MVFIYSwpucbvxA/qJXO5FsldlKr8qDxL8EKW7kEQAQsLtapyC1gRkq3vp217mOccwf8wwLksRSlYIoMvCNkOarmEahyODAT2J4yGgtFzhx8UDf5/r6c4NEs7CNqnpxkvbO0kcVjNhCyh5AJe/SW9pBPOV3DJGvu3dsKFaiyxf8qTW9gheQwVs4Z90BDm5oF47cF/Ht4aZC75argxUmD61g9ktJC14hXoN2U5ZmJ0TILitbyq5O889KxuoB/7xRqKnwv9jdn5HqPvGnDVWwTpNJvrFSCul2efi4DeiRigqdB9RfwAI6vGM+5tj41YIvaJL9C+hOfNxerLzHYWhImhPKh3uuBnFJ/A05XoR9zRcBTOMeGo+wcs+yse
