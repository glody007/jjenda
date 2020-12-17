<template>
  <v-img
    class="white--text align-end grey lighten-2"
    :height="height"
    :aspect-ratio="aspectRatio"
    :src="article.url_photo"
    :lazy-src="article.url_thumbnail_photo"
  >
    <template v-slot:placeholder>
      <v-row
        class="fill-height ma-0"
        align="center"
        justify="center"
      >
        <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
      </v-row>
    </template>
  </v-img>
</template>

<script>

export default {
  name: 'ArticleImage',

  props: ['article', 'aspectRatio', 'height']
}
</script>
