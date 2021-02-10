<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="400px"
    >
      <v-card>
        <v-card-title>
          <span class="headline">Upload raw products file</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row justify="center">
              <v-file-input
                label="raw products file .json"
                @change="selectFile"
                accept=".json"
                outlined
                dense
                chips
              ></v-file-input>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="closeDialog"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="postArticles"
          >
            Upload
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import $backend from '../../backend'

export default {
  name: 'DialogAjouterArticlesRawFromFile',
  data: () => ({
    formData: new FormData(),
    error: ''
  }),
  props: ['dialog'],
  methods: {
    postArticles () {
      $backend.postArticlesRawFromFile(this.formData)
        .then(responseData => {
          //this.closeDialog()
          console.log(responseData)
        })
        .catch(error => {
          this.error = error
        })
    },
    closeDialog () {
      this.$emit('closeDialog')
    },
    selectFile (file) {
      this.formData.append('file', file)
    }
  }
}
</script>
