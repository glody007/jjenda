<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      dark
      app
      clipped
    >
      <v-list dense>
        <v-list-item link to="/">
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Acceuil</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to="/about">
          <v-list-item-action>
            <v-icon>mdi-information</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>À propos</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      dark
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Jjenda</v-toolbar-title>
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
     fixed
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
    link: 'https://play.google.com/store/apps/details?id=com.jjenda'
  }),
  created () {
    this.$vuetify.theme.dark = false
  }
}
</script>
