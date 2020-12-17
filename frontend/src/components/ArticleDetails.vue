<template>
  <v-container fill-height fluid>
    <v-row justify="center">
      <v-col cols="12" sm="6">
          <ArticleImage :article="article" :aspectRatio="2/3"/>
      </v-col>

      <v-col cols="12" sm="4">
        <v-card
          class="mx-auto"
          max-width="400"
          outlined
          tile
          hover
        >
          <v-card-title class="ma-0">
            <div>{{article.categorie}}</div>
          </v-card-title>

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

          <VendeurContact class="mt-6" :article= "article"/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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
