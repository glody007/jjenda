<template>
  <v-card-actions>
    <v-btn
      color="#c2185b"
      text
      :to="linkVendeur"
    >
      <v-icon>mdi-account-circle</v-icon>
      VENDEUR
    </v-btn>

    <v-btn
      color="#25D366"
      text
      :href="whatsapp"
      v-if="userLoaded"
    >
      <v-icon>mdi-whatsapp</v-icon>
      MESSSAGE
    </v-btn>
  </v-card-actions>
</template>

<script>
import $backend from '../backend'

export default {
  name: 'VendeurContact',

  props: ['article'],

  data: () => ({
    vendeur: {},
    error: '',
    userLoaded: false
  }),

  computed: {
    linkVendeur () {
      return '/vendeur/' + this.article.vendeur_id
    },
    whatsapp () {
      return 'https://wa.me/' + this.vendeur.phone_number
    }
  },

  mounted () {
    this.fetchVendeur()
  },

  methods: {
    fetchVendeur () {
      $backend.fetchVendeur(this.article.vendeur_id)
        .then(responseData => {
          this.vendeur = responseData
          this.userLoaded = true
        })
        .catch(error => {
          this.error = error
        })
    }
  }
}
</script>
