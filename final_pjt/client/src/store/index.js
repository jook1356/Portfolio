import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)
const API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    authError: null,
    isAuthError: false,
    userInfo: null,
    isNewUser: false,
    navbarShow: true,
    genreList: [],
    topRatedList: [],
    popularList: [],
    moviesByGenreList: [],
    moviesByViewedList: [],
    moviesByRelatedList: [],
    moviesByScoreList: [],
    backgroundMovie: null,
    isDetailMode: false,
    wallpaperFix: false,
    cardXY: {
      cardX: null,
      cardY: null
    },
    token: null,
  },
  getters: {
    isAuthError: state => state.isAuthError,
    authError: state => state.authError,
  },
  mutations: {
    SET_AUTH_ERROR: (state, error) => {
      state.authError = error
      state.isAuthError = true
    },
    IDENTIFY_NEW_USER(state, bool) {
      state.isNewUser = bool
    },
    DELETE_USREINFO(state) {
      state.userInfo = null
      state.token = null
    },
    GET_USER_INFO(state, userInfo) {
      state.userInfo = userInfo
    },
    GET_CARD_XY(state, cardXY) {
      state.cardXY = cardXY
    },
    RECEIVE_GENRE_DATA(state, payload) {
      state.genreList = payload
    },
    RECEIVE_TOP_RATED_DATA(state, payload) {
      state.topRatedList = payload
    },
    RECEIVE_POPULAR_DATA(state, payload) {
      state.popularList = payload
    },
    RECEIVE_MOVIES_BY_GENRE_DATA(state, payload) {
      state.moviesByGenreList = payload
    },
    RECEIVE_MOVIES_BY_VIEWED_DATA(state, payload) {
      state.moviesByViewedList = payload
    },
    RECEIVE_MOVIES_BY_RELATED_DATA(state, payload) {
      state.moviesByRelatedList = payload
    },
    RECEIVE_MOVIES_BY_SCORE_DATA(state, payload) {
      state.moviesByScoreList = payload
    },
    BACKGROUND_MOVIE(state, movie) {
      state.backgroundMovie = movie
    },
    IS_DETAIL_MODE(state, bool) {
      state.isDetailMode = bool
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name: 'movie'})
    },
    SAVE_TOKEN_WITHOUT_ROUTER(state, token) {
      state.token = token
    },
    WALLPAPER_FIX_ON(state) {
      state.wallpaperFix = true
    },
    WALLPAPER_FIX_OFF(state) {
      state.wallpaperFix = false
    },
    NAVBAR_SHOW_ON(state) {
      state.navbarShow = true
    },
    NAVBAR_SHOW_OFF(state) {
      state.navbarShow = false
    },
  },
  actions: {
    receiveTopRatedData(context) {
      const URL = 'http://127.0.0.1:8000/movies/get_top_rated_movies/'
      axios({
        method: 'GET',
        url: URL,
      })
        .then(response => {
          const payload = response.data
          context.commit('RECEIVE_TOP_RATED_DATA', payload)
        })
        .catch(error => {
          console.log('receiveTopRatedData => ', error)
        })
    },
    receivePopularData(context) {
      const URL = 'http://127.0.0.1:8000/movies/get_popular_movies/'
      axios({
        method: 'GET',
        url: URL,
      })
        .then(response => {
          const payload = response.data
          context.commit('RECEIVE_POPULAR_DATA', payload)
          console.log('Popular')
          console.log(payload)
        })
        .catch(error => {
          console.log('receivePopularData => ', error)
        })
    },
    receiveMoviesByGenreData(context) {
      const URL = 'http://127.0.0.1:8000/movies/get_movies_by_genre/all/'
      axios({
        method: 'GET',
        url: URL,
      })
        .then(response => {
          const payload = response.data
          context.commit('RECEIVE_MOVIES_BY_GENRE_DATA', payload)
        })
        .catch(error => {
          console.log('receiveMoviesByGenreData => ', error)
        })
    },
    receiveMoviesByViewedData(context) {
      const URL = 'http://127.0.0.1:8000/movies/recommend_most_viewed/'
      axios({
        method: 'GET',
        url: URL,
      })
        .then(response => {
          const payload = response.data
          context.commit('RECEIVE_MOVIES_BY_VIEWED_DATA', payload)
        })
        .catch(error => {
          console.log('receiveMoviesByViewedData => ', error)
        })
    },
    receiveMoviesByRelatedData(context) {
      const URL = 'http://127.0.0.1:8000/movies/recommend_related/'
      axios({
        method: 'POST',
        url: URL,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then(response => {
          const payload = response.data
          context.commit('RECEIVE_MOVIES_BY_RELATED_DATA', payload)
        })
        .catch(error => {
          console.log('receiveMoviesByRelatedData => ', error)
        })
    },
    receiveMoviesByScoreData(context) {
      const URL = 'http://127.0.0.1:8000/movies/recommend_score/'
      axios({
        method: 'POST',
        url: URL,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then(response => {
          const payload = response.data
          context.commit('RECEIVE_MOVIES_BY_SCORE_DATA', payload)
        })
        .catch(error => {
          console.log('receiveMoviesByScoreData => ', error)
        })
    },
    login(context) {
      
          // 로그인시 store에 유저 정보 저장하기
      axios({
        method: 'get',
        url: `${API_URL}/accounts/get_additional_user_info/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log('USERINFO')
          console.log('USERINFO')
          console.log('USERINFO')
          console.log('USERINFO')
          console.log('USERINFO')
          console.log(res.data)
          context.commit('GET_USER_INFO', res.data)
      })
        .catch((err) => {
          console.log('USERINFOFAIL')
          console.log('USERINFOFAIL')
          console.log('USERINFOFAIL')
          console.log('USERINFOFAIL')
          console.log('USERINFOFAIL')
          console.log(err)
      })
      
    },
    logout(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then(() => {
          context.commit('DELETE_USREINFO')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    receiveGenreData(context) {
      const URL = 'http://127.0.0.1:8000/movies/get_genre_list/'
      axios({
        method: 'GET',
        url: URL,
      })
        .then(response => {
          const payload = response.data
          context.commit('RECEIVE_GENRE_DATA', payload)
        })
        .catch(error => {
          console.log('receiveGenreData => ', error)
        })
    },
    
  },
  modules: {
  }
})
