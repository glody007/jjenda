import axios from 'axios'

let $axios = axios.create({
  baseURL: 'https://djendardc.herokuapp.com/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {

  fetchArticles () {
    return $axios.get(`produits`)
      .then(response => response.data)
  }
}
