<template>
  <div id="app">
    <MovieSearch class="search-form"/>
      <div class="app-wallpaper" style="position:fixed; z-index:-10; width: 100vw; height:100vh; background-color:black;"></div>
      <!-- <div class="gradient" ></div> -->

      <div class="app-wrapper">

        <nav class="navbar navbar-expand-lg position-fixed w-100" v-if="this.$store.state.navbarShow === true">
          <div class="navbar-wrapper-block"></div>
          <div class="navbar-wrapper-gradient"></div>
          <div class="container-fluid navbar navbar-dark" style="display:flex; justify-content:space-between;">
            <!-- <img src="/docs/5.2/assets/brand/bootstrap-logo.svg" alt="Logo" width="30" height="24" class="d-inline-block align-text-top"> -->
            <router-link class="navbar-brand" :to="{ name: 'movie'}" style="color:red; margin-left: 20px;">SSAFLIX</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav" >
              <ul class="navbar-nav" >
                <li class="nav-item">
                <router-link :to="{ name: 'movie'}" class="nav-link">Movie</router-link>
                </li>
                <li class="nav-item">
                  <router-link :to="{ name: 'community'}" class="nav-link">Community</router-link>
                </li>
                <li class="nav-item" v-if="userInfo === null"><!--  v-if="!userInfo" -->
                  <router-link :to="{ name: 'login'}" class="nav-link">Login</router-link>
                </li>
                <li class="nav-item" v-if="userInfo">

                  <span @click="logout" class="nav-link" style="cursor:pointer;">Logout</span>
                </li>
                <li class="nav-item" v-if="userInfo">
                  <router-link :to="{ name: 'change_password'}" class="nav-link">{{ userInfo.username }}</router-link>
                </li>
              </ul>
              <div class="search" @click="showSearchForm">
                <span style="margin-right:10px; margin-left:8px;">Search</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-search-heart-fill" viewBox="0 0 16 16">
                  <path d="M6.5 13a6.474 6.474 0 0 0 3.845-1.258h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.008 1.008 0 0 0-.115-.1A6.471 6.471 0 0 0 13 6.5 6.502 6.502 0 0 0 6.5 0a6.5 6.5 0 1 0 0 13Zm0-8.518c1.664-1.673 5.825 1.254 0 5.018-5.825-3.764-1.664-6.69 0-5.018Z"/>
                </svg>
              </div>
            </div>
            

          </div>
        </nav>


        <div class="view-wrapper">
          <router-view/>
        </div>


      </div>

  </div>
</template>

<script>
import MovieSearch from '@/components/MovieSearch'
import axios from 'axios'
import _ from 'lodash'

export default {
  components: {
    MovieSearch
  },
  data() {
    return {
    }
  },
  computed: {
    userInfo() {
      return this.$store.state.userInfo
    },
    backgroundMovie() {
      const movie = this.$store.state.backgroundMovie
      return movie
    },
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    },
    showSearchForm() {
      this.$store.commit('IS_DETAIL_MODE', false)
      const bodyTag = document.querySelector('body')
      bodyTag.style.overflow = 'hidden'
      
      const searchForm = document.querySelector('.search-form')
      const searchInnerForm = document.querySelector('.search-inner-form')
      searchForm.style.top = '0%'
      searchInnerForm.style.opacity = '100%'
      searchInnerForm.style.width = '100vw'
      searchInnerForm.style.height = '100vh'

      const searchInput = document.querySelector('.searchInput')
      searchInput.value = null
      searchInput.focus()

      // setTimeout(() => {
      //   searchForm.style.backgroundColor = 'rgba(0, 0, 0, 0.6)'
      // }, 200);
    }
  },
  mounted() {
    
    
    // const URL = 'http://127.0.0.1:8000/movies/get_popular_movies/'
    const URL = 'http://127.0.0.1:8000/movies/get_movies_by_genre/10749/'
    axios({
      method: 'GET',
      url: URL,
    })
      .then(response => {
        const movies = response.data[0].movies
        
        let selected = _.sample(_.range(0, movies.length))
        while (movies[selected].overview === '') {
          selected = _.sample(_.range(0, movies.length))
        }
        this.$store.commit('BACKGROUND_MOVIE', response.data[0].movies[selected])
        
        const bodyTag = document.querySelector('.app-wallpaper')
        bodyTag.setAttribute(`style`, `background-image:url('https://image.tmdb.org/t/p/original${response.data[0].movies[selected].backdrop_path}'); width: 100vw; height:100vh; background-size:cover; background-color: black; background-repeat:no-repeat; position:fixed; z-index:-10; background-attachment: fixed; `)

      })
      .catch(error => {
        console.log('receiveTopRatedData => ', error)
      })


    
    
    
      window.addEventListener('scroll', () => {
        let scrollLocation = document.documentElement.scrollTop; // 현재 스크롤바 위치
        // let windowHeight = window.innerHeight; // 스크린 창
        // let fullHeight = document.body.scrollHeight; //  margin 값은 포함 x
        const navbarBlock = document.querySelector('.navbar-wrapper-block')
        const navbarGradient = document.querySelector('.navbar-wrapper-gradient')
        if (scrollLocation === 0) {
          navbarBlock.style.opacity = 0
          navbarGradient.style.opacity = 255
        } else {
          navbarBlock.style.opacity = 255
          navbarGradient.style.opacity = 0
        }

      })

    
  },
}
</script>



<style>
html,#app{
  /* background-color: black; */
  width: 100%;
  height: 100%;
}

#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  z-index: 100;
  

}
/* @font-face {
    font-family: 'SUIT-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_suit@1.0/SUIT-Regular.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

* {
  font-family: 'SUIT-Regular';
} */

* {
  font-family: 'SUIT', sans-serif;
}

.app-wrapper {
  width: 100vw;
  height: 100vh;

  
}



.nav {
  position:fixed;
  top: 0;
  left: 0;
  right: 0;
  
}
.navbar {
  z-index:99;
}

.view-wrapper {
  padding-top: 72px;
  
}

/* .gradient {

  top:10vw;
  background-image:url('images/background.png');
  width: 100%;
  height: 100%;
  background-size:100vw 100vh;
  z-index: -1;
  position: absolute;

} */

.navbar-wrapper-block {
  position:absolute;
  background-color: rgba(0, 0, 0, 0.4);
  width:100%;
  height:100%;
  opacity: 0;
  transition-duration: 0.5s;
  transition-property: opacity;
  backdrop-filter: blur(50px);
}
.navbar-wrapper-gradient {
  position:absolute;
  background: linear-gradient(rgb(0, 0, 0, 0.8), rgba(0, 0, 0, 0));
  width:100%;
  height:100%;
  transition-duration: 0.5s;
  transition-property: opacity;
  
}

.search {
  margin-right:24px;
  color:rgba(255, 255, 255, 0.5);
  transition-duration: 0.5s;
  transition-property: color;
  cursor: pointer;
}
.search:hover {
  color:rgba(255, 255, 255, 1);
}

</style>
