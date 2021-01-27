<template>
  <div>
    <v-app-bar
      app
      dark
      clipped-left
    >
      <v-container class="py-0 fill-height">
        <v-avatar
          class="mr-2"
          size="40"
        >
        <img
          src="https://ik.imagekit.io/djenda/web_hi_res_512_O-MaEysDV.png"
          alt="JJenda icon"
        >
        </v-avatar>

        <v-toolbar-title>Jjenda</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-responsive max-width="500">
          <v-text-field
            dense
            filled
            solo-inverted
            hide-details
            label="Rechercher des articles"
            prepend-inner-icon="mdi-magnify"
            @focus="onFocus"
          >
          </v-text-field>
        </v-responsive>

        <v-spacer></v-spacer>

        <v-btn
          v-for="link in links"
          :key="link"
          text
        >
          {{ link }}
        </v-btn>

      </v-container>
    </v-app-bar>

    <v-main>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row align="end" justify="center">
          <router-view :key="$route.fullPath"/>
        </v-row>
      </v-container>
    </v-main>
  </div>
</template>

<script>
export default {
  name: 'Main',
  props: {
    source: String
  },
  data: () => ({
    drawer: false,
    snackbar: true,
    link: 'https://play.google.com/store/apps/details?id=com.jjenda',
    links: ['About']
  }),
  methods: {
    onFocus () {
      this.$router.push({ path: 'research' })
    }
  },
  created () {
    this.$vuetify.theme.dark = false
  }
}
</script>
