<template>
  <v-container>
      <v-row justify="center">
        <v-col
          v-for="(article, i) in articles"
          :key="i"
          cols="9" sm="4" md="3"
          class="mb-5"
        >
          <Article :article="article"/>
        </v-col>
      </v-row>
  </v-container>
</template>

<script>
import Article from '../components/Article'

export default {
  name: 'listeArticles',

  components: {
    Article
  },

  props: ['articles'],

  data: () => ({
  }),

  methods: {

  }
}
</script>
