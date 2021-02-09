<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      app
      dark
    >
      <v-list
        nav
        dense
      >
        <v-subheader>DASHBOARD</v-subheader>
        <v-list-item-group
          v-model="group"
        >
          <v-list-item>
            <v-list-item-title>Overview</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Products from  crawler</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>KPI</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row align="end" justify="center">
          <ArticlesFromCrawler/>
        </v-row>
      </v-container>
    </v-main>

  </v-app>
</template>

<script>
import ArticlesFromCrawler from './ArticlesFromCrawler'

export default {
  name: 'dashboard',
  components: {
    ArticlesFromCrawler
  },
  data: () => ({
  })
}

</script>

<style lang="scss">
</style>
