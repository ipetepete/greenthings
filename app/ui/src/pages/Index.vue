<template>
  <q-page class="flex flex-center">
    <q-card class="my-card">
      <q-card-section>
        {{ sup }}
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import {
  QCard,
  QCardSection
} from 'quasar'

export default {
    name: 'PageIndex',
    components: {
      QCard,
      QCardSection
    },
    data (){
      return {
        sup: "Sup yo"
      }
    }

}
</script>
