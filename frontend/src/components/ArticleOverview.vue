<template>
  <div>
    <v-card-title class="ma-0">
      {{article.categorie}}
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
  </div>
</template>

<script>
import moment from 'moment'

export default {
  name: 'ArticleOverview',

  components: {

  },

  data: () => ({
    format: 'yyyy-MM-dd HH:mm:ss.SSS'
  }),

  props: ['article'],

  computed: {
    linkDetails () {
      if (this.article.id) return `/article/${this.article.id}`
      return `/article/${this.article._id.$oid}`
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
