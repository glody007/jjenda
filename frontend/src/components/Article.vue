<template>
  <v-card
    class="mx-auto"
    max-width="400"
    outlined
    tile
    hover
    :to="linkDetails"
  >
    <ArticleImage :article="article" :height="200"/>

    <v-card-title class="ma-0">{{article.categorie}}</v-card-title>

    <v-card-text class="text--primary">
      <div>{{article.description}}</div>

      <div>{{elapsedTime}}</div>

      <v-badge
        class="mt-5"
        color="black"
        inline
        :content="prix"
      >
      </v-badge>
    </v-card-text>

  </v-card>
</template>

<script>
import ArticleImage from '../components/ArticleImage'
import VendeurContact from '../components/VendeurContact'
import moment from 'moment'

export default {
  name: 'Article',

  components: {
    ArticleImage, VendeurContact
  },

  data: () => ({
    format: 'yyyy-MM-dd HH:mm:ss.SSS'
  }),

  props: ['article'],

  computed: {
    linkDetails () {
      return '/article/' + this.article._id.$oid
    },
    prix () {
      return `${this.article.prix}$`
    },
    elapsedTime () {
      moment.locale('fr')
      return moment(this.article.created_at, this.format).fromNow()
    }
  }
}
</script>
