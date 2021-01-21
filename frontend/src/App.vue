<template>
  <v-app id="inspire">
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
          alt="John"
        >
        </v-avatar>

        <v-toolbar-title>Jjenda</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-responsive max-width="500" class="mt-1">
          <v-text-field
            flat
            clearable
            hide-details
            solo-inverted
            label="Rechercher des articles"
            prepend-inner-icon="mdi-magnify"
          >
            <template v-slot:append-outer>
              <v-btn
                large
                color="pink"
                class="mb-0"
                style="top: -10px"
                offset-y
              >
                <v-icon>mdi-magnify</v-icon>
              </v-btn>
            </template>
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

    <v-footer
     dark
    >
      <v-container>
        <v-row justify="center">
          <v-snackbar
            :timeout="-1"
            :value="true"
            color="black"
            v-model="snackbar"
          >
            Pour vendre télécharger l'application

            <template v-slot:action="{ attrs }">
              <v-btn
                color="pink"
                v-bind="attrs"
                :href="link"
              >
                <v-icon>mdi-google-play</v-icon>
                TELECHARGER
              </v-btn>

              <v-btn
                color="pink"
                text
                v-bind="attrs"
                @click="snackbar = false"
              >
                Fermer
              </v-btn>
            </template>
          </v-snackbar>
        </v-row>
        <v-row justify="center" class="mt-1">
          <span>&copy; {{ new Date().getFullYear() }}</span>
        </v-row>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  props: {
    source: String
  },
  data: () => ({
    drawer: false,
    snackbar: true,
    link: 'https://play.google.com/store/apps/details?id=com.jjenda',
    links: ['About']
  }),
  created () {
    this.$vuetify.theme.dark = false
  }
}
</script>
