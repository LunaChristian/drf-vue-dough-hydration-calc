<script setup>
import { ref } from 'vue'

// Variables reactivas para cada input
const cantidadHarina = ref(null)
const cantidadAgua = ref(null)

// Estado para loading, resultado y errores
const loading = ref(false)
const resultado = ref(null)
const errores = ref(null)

async function calcularHidratacion() {
  
  // Marcamos que estamos cargando
  loading.value = true
  resultado.value = null
  errores.value = null

  // Armado del objeto a enviar al backend
  const payload = {
    cantidad_harina: Number(cantidadHarina.value),
    cantidad_agua: Number(cantidadAgua.value)
  }

  try {
    const response = await fetch('http://127.0.0.1:8000/api/v1/calcular-hidratacion/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    })

    if (response.ok) {
      const data = await response.json()
      resultado.value = data
    } else {
      const errorData = await response.json()
      errores.value = errorData
    }
  } catch (error) {
    errores.value = { detalle: ['Error de conexión con el servidor.'] }
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <!-- Parte visual: HTML con “superpoderes” de Vue -->
  <div class="app-container">
    <h1>Calculadora de hidratacion para la masa</h1>
    <p class="descripcion">
      Esta mini herramienta usa la API en Django REST Framework para calcular
      la hidratacion de la masa.
    </p>

    <!-- Acá más adelante vamos a poner el formulario -->
    <div class="panel">

      <div class="campo">
        <label>Cantidad Harina:</label>
        <input type="number" v-model="cantidadHarina" />
      </div>

      <div class="campo">
        <label>Cantidad Agua:</label>
        <input type="number" v-model="cantidadAgua" />
      </div>

      <button class="btn-calcular" @click="calcularHidratacion" :disabled="loading">
        {{ loading ? 'Calculando...' : 'Calcular' }}
      </button>

      <div v-if="resultado" class="resultado">
        <h2>Resultado</h2>
        <p><strong>Hidratacion total:</strong> {{ resultado.hidratacion }} %</p>
      </div>

      <div v-if="errores" class="errores">
        <h2>Errores</h2>
        <pre>{{ errores }}</pre>
      </div>

    </div>

  </div>
</template>

<style scoped></style>
