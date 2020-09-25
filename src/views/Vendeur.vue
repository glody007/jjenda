<template>
  <v-container>
    <v-row
      justify='space-between'
      class="mb-3"
    >
      <h2 class="text-h3 ml-3" >
        Article de <span :style="{color:'#c2185b'}">{{vendeur.nom}}</span>
      </h2>
    </v-row>

    <v-row>
      <v-btn
        fab
        dark
        :href="whatsapp"
        color="#25D366"
        class="ml-3"
      >
        <v-icon>mdi-whatsapp</v-icon>
      </v-btn>
      <h4 class="text-h5 ml-3 my-3" >{{vendeur.phone_number}}</h4>
    </v-row>

    <v-row justify="center">
      <VendeurArticles :vendeurId="$route.params.id"/>
    </v-row>
  </v-container>
</template>

<script>
import VendeurArticles from '../components/VendeurArticles'
import $backend from '../backend'

export default {
  name: 'Vendeur',

  components: {
    VendeurArticles
  },

  data: () => ({
    vendeur: {},
    error: ''
  }),

  mounted () {
    this.fetchVendeur()
  },

  computed: {
    whatsapp () {
      return 'https://wa.me/' + this.vendeur.phone_number
    }
  },

  methods: {
    fetchVendeur () {
      $backend.fetchVendeur(this.$route.params.id)
        .then(responseData => {
          this.vendeur = responseData
        })
        .catch(error => {
          this.error = error
        })
    }
  }
}
</script>
