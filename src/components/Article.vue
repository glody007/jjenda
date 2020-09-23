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

      <div>{{article.created_at}}</div>

      <v-badge
        class="mt-5"
        color="black"
        inline
        :content="prix"
      >
      </v-badge>
    </v-card-text>

    <VendeurContact :article="article"/>
  </v-card>
</template>

<script>
import ArticleImage from '../components/ArticleImage'
import VendeurContact from '../components/VendeurContact'

export default {
  name: 'Article',

  components: {
    ArticleImage, VendeurContact
  },

  props: ['article'],

  computed: {
    linkDetails () {
      return '/article/' + this.article._id.$oid
    },
    prix () {
      return `${this.article.prix}$`
    }
  }
}
</script>
