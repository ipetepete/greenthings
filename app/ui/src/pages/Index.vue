<template>
  <q-page class="flex flex-center">
    <q-card class="my-card">
      <q-card-section>
        {{ sup }}
        <q-card-actions>
          <q-btn flat @click="foobar">Action 1</q-btn>
          <q-btn flat>Action 2</q-btn>
        </q-card-actions>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import {
  QCard,
  QCardSection,
  QCardActions,
} from 'quasar'

export default {
    name: 'PageIndex',
    components: {
      QCard,
      QCardSection,
      QCardActions
    },
    methods: {
      foobar: function(){
        this.$axios.get("http://localhost:5000/get_state")
            .then(function(data){
              console.log("got this", data);
            })
            .catch(function(err){
              console.error(err);
            });
      }
    },
    data (){
      return {
        sup: "Sup yo"
      }
    }

}
</script>
