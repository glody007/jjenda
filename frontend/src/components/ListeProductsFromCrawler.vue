<template>
  <v-container>
    <div v-infinite-scroll="loadMore" infinite-scroll-distance="10">
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
    </div>
  </v-container>
</template>

<script>
import Article from '../components/Article'

export default {
  name: 'ListeProductsFromCrawlere',

  components: {
    Article
  },

  props: ['articles'],

  data: () => ({
  }),

  mounted () {

  },

  methods: {
    loadMore: function () {
      this.$emit('loadMore')
    }
  }

}
</script>
