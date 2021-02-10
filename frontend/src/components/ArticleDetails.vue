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
          <ArticleOverview :article="article"/>

          <VendeurContact class="mt-6" :article="article"/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ArticleImage from '../components/ArticleImage'
import VendeurContact from '../components/VendeurContact'
import ArticleOverview from '../components/ArticleOverview'

export default {
  name: 'Article',

  components: {
    ArticleImage,
    ArticleOverview,
    VendeurContact
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
