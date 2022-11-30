<template>
  <div class="movie-view">
    <div class="fade-in-animation"></div>
    <div class="gradient"></div>

    


    <div class="movie-view-wrapper">
      <div>
            <MovieCardDetail :effect-element="`background-movie-button`" :props-movie="backgroundMovie" :identifier="backgroundMovieIdentifier" ref="apiRequest" style="z-index:99999; visibility: hidden;" />
      </div>

      <div class="background-movie-form">
        <div v-if="browserWidth >= 992">
          <p class="background-movie-title-width"><b>{{backgroundMovie.title}}</b></p>
        </div>
        <div v-else>
          <p class="background-movie-title-height"><b>{{backgroundMovie.title}}</b></p>
        </div>
        
        <div v-if="browserWidth >= 768 && browserHeight >= 576">
          <p class="background-movie-overview">{{backgroundMovie.overview}}</p>
        </div>
        <div class="background-movie-button" id="background-movie-button" @click="backgroundMovieDetail">
          <span class="background-movie-button-font"><b>상세 정보</b></span>
        </div>
        <!-- <button type="button" class="btn btn-light background-movie-button">
          
          
        </button> -->

        

      </div>


      <div class="movie-list-wrapper">
        <!-- {{moviesByRelatedList}}
        <p style="color:red;">{{moviesByScoreList}}</p> -->

        <div v-if="moviesByRelatedList.length >= cardSplitter">
          <div class="category-title"><b>비슷한 취향을 가진 사람들이 많이 찾는 영화</b></div>
          <MovieCard :movieList="moviesByRelatedList" :identifier="`moviesByRelated`" :card-splitter="cardSplitter"/>
          <br>
          <br>
        </div>

        <div v-if="moviesByScoreList.length >= cardSplitter">
          <div class="category-title"><b>취향 저격, 당신만을 위한 영화</b></div>
          <MovieCard :movieList="moviesByScoreList" :identifier="`moviesByScore`" :card-splitter="cardSplitter"/>
          <br>
          <br>
        </div>
        

        <div class="category-title"><b>최고의 인기 화제작 TOP 20</b></div>
        <MovieCard :movieList="topRatedList" :identifier="`topRated`" :card-splitter="cardSplitter"/>
        <br>
        <br>

        <div class="category-title"><b>좋아요를 가장 많이 받은 영화</b></div>
        <MovieCard :movieList="popularList" :identifier="`popular`" :card-splitter="cardSplitter"/>
        <br>
        <br>

        <div class="category-title"><b>사람들이 가장 많이 본 영화</b></div>
        <MovieCard :movieList="moviesByViewedList" :identifier="`mostViewed`" :card-splitter="cardSplitter"/>
        <br>
        <br>

        <div v-for="genre in moviesByGenreList" :key="genre.name">
          <div v-if="'movies' in genre && genre.movies.length >= cardSplitter">
            <div class="category-title"><b>{{ genre.name }}</b></div>
            <MovieCard :movieList="genre.movies" :identifier="`${genre.name}`" :card-splitter="cardSplitter"/>
            <br>
            <br>
          </div>
        </div>
      

        <div style="display:flex; justify-content:center; width:100%; padding-top:80; padding-bottom:80px; color:rgb(150,150,150);">
          <div style="display:flex; align-items: center; flex-direction:column;">
            <span>SSAFY MOVIE RECOMMEND PROJECT</span>
            <span>2022.11.16 ~ 2022.11.24</span>
            <span>Copyright 김동주 & 이민지 All right reserved.</span>
          </div>
          

        </div>
        
      
      </div>
    </div>
    

  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import MovieCardDetail from '@/components/MovieCardDetail'
// import axios from 'axios'
// import _ from 'lodash'


export default {
  name: 'MovieView',
  components: {
    MovieCard,
    MovieCardDetail,

  },
  data() {
    return {
      browserWidth: null,
      browserHeight: null,
      cardSplitter: null,
      backgroundMovieIdentifier: 'background-fade',
    }
  },
  computed: {
    
    backgroundMovie() {
      const movie = this.$store.state.backgroundMovie
      return movie
    },
    topRatedList() {
      return this.$store.state.topRatedList
    },
    popularList() {
      return this.$store.state.popularList
    },
    moviesByGenreList() {
      return this.$store.state.moviesByGenreList
    },
    moviesByViewedList() {
      return this.$store.state.moviesByViewedList
    },
    moviesByRelatedList() {
      return this.$store.state.moviesByRelatedList
    },
    moviesByScoreList() {
      return this.$store.state.moviesByScoreList
    }



  },
  methods: {
    receiveTopRatedData() {
      this.$store.dispatch('receiveTopRatedData')
    },
    receivePopularData() {
      this.$store.dispatch('receivePopularData')
    },
    receiveMoviesByGenreData() {
      this.$store.dispatch('receiveMoviesByGenreData')
    },
    receiveMoviesByViewedData() {
      this.$store.dispatch('receiveMoviesByViewedData')
    },
    receiveMoviesByRelatedData() {
      this.$store.dispatch('receiveMoviesByRelatedData')
    },
    receiveMoviesByScoreData() {
      this.$store.dispatch('receiveMoviesByScoreData')
    },
    getCardXY() {

    const cardTag = document.querySelector('.background-movie-button')
    const cardX = cardTag.getBoundingClientRect().left;
    const cardY = cardTag.getBoundingClientRect().top;
    const cardXY = {cardX:cardX, cardY:cardY}
    this.$store.commit('GET_CARD_XY', cardXY)

    //   alert(this.$store.state.cardXY.cardX)
    //   alert(this.$store.state.cardXY.cardY)

    },
    backgroundMovieDetail() {
      // const idx = this.backgroundMovie.id
      // this.$parent.getCardXY(idx)
      // const backgroundTag = document.getElementById(`background-${this.backgroundMovieIdentifier}-${idx}`)
      // backgroundTag.style.opacity = 0
      this.$store.commit('IS_DETAIL_MODE', true)
      this.mouseOnCard = false
      this.getCardXY()
      this.$refs.apiRequest.showDetail();
    }
  },
  created() {
    this.receiveTopRatedData()
    this.receivePopularData()
    this.receiveMoviesByGenreData()
    this.receiveMoviesByViewedData()
    this.receiveMoviesByScoreData()
    this.receiveMoviesByRelatedData()
    
    this.browserWidth = document.body.offsetWidth
    this.browserHeight = window.innerHeight
    this.$store.commit('IS_DETAIL_MODE', false)

    // const API_URL = "http://127.0.0.1:8000"

    // axios({
    //   method: 'get',
    //   url: `${API_URL}/accounts/user/`,
    //   headers: {
    //     Authorization: `Token ${this.$store.state.token}`
    //   }
    // })
    //   .then((res) => {
    //     this.$store.commit('GET_USER_INFO', res.data)
    //     console.log(res)
    // })
    //   .catch((err) => {
    //     console.log(err)
    // })

  },
  mounted() {
    this.$store.commit('NAVBAR_SHOW_ON')
    if (this.$store.state.wallpaperFix === true) {
      // const bodyTag = document.querySelector('.movie-view')
      // bodyTag.setAttribute(`style`, `background-image:url('https://image.tmdb.org/t/p/original${this.backgroundMovie.backdrop_path}'); width: 100vw; height:100vh; background-size:cover; background-color: black; background-repeat:no-repeat; `)
    
      const viewTag = document.querySelector('.fade-in-animation')
      viewTag.setAttribute(`style`, `background-image:url('https://image.tmdb.org/t/p/original${this.backgroundMovie.backdrop_path}'); width: 100vw; height:100vh; z-index:99999; background-size:cover; background-color: black; background-repeat:no-repeat; `)
      setTimeout(() => {
        viewTag.style.opacity = 0
      }, 10);
      
      setTimeout(() => {
        viewTag.style.display = 'none'
      }, 1010);
    }

    
    
    // if (this.$store.state.wallpaperFix === false) {
    // const URL = 'http://127.0.0.1:8000/movies/get_popular_movies/'
    // axios({
    //   method: 'GET',
    //   url: URL,
    // })
    //   .then(response => {
    //     const movies = response.data
    //     let selected = _.sample(_.range(0, movies.length))
    //     while (movies[selected].overview === '') {
    //       selected = _.sample(_.range(0, movies.length))
    //     }
    //     this.$store.commit('BACKGROUND_MOVIE', response.data[selected])
    //     // const bodyTag = document.querySelector('.movie-view')
    //     // bodyTag.setAttribute(`style`, `background-image:url('https://image.tmdb.org/t/p/original${this.backgroundMovie.backdrop_path}'); width: 100vw; height:100vh; background-size:cover; background-color: black; background-repeat:no-repeat; `)
    //   })
    //   .catch(error => {
    //     console.log('receiveTopRatedData => ', error)
        
    //   })
    // }
    
    this.$store.commit('WALLPAPER_FIX_OFF')

    // const URL = 'http://127.0.0.1:8000/movies/get_popular_movies/'
    // axios({
    //   method: 'GET',
    //   url: URL,
    // })
    //   .then(response => {
    //     const movies = response.data
    //     let selected = _.sample(_.range(0, movies.length))
    //     while (movies[selected].overview === '') {
    //       selected = _.sample(_.range(0, movies.length))
    //     }
    //     this.$store.commit('BACKGROUND_MOVIE', response.data[selected])
    //     const bodyTag = document.querySelector('.movie-view')
    //     bodyTag.setAttribute(`style`, `background-image:url('https://image.tmdb.org/t/p/original${movies[selected].backdrop_path}'); width: 100vw; height: 100vh; background-size:100vw; position:absolute;  background-repeat:no-repeat; `)
    //   })
    //   .catch(error => {
    //     console.log('receiveTopRatedData => ', error)
    //   })
    
    
    
    this.cardSplitter = parseInt(document.body.offsetWidth / 300) + 1
    
    window.onresize = (() => {
      this.browserWidth = document.body.offsetWidth //event.delegateTarget.innerWidth
      this.browserHeight = window.innerHeight
      this.cardSplitter = parseInt(document.body.offsetWidth / 300) + 1 //event.delegateTarget.innerWidth

      
    });

  },

}
</script>

<style>
  .movie-view {
    margin-top: -72px;
    padding-top: 72px;
    
  }
  .fade-in-animation {
    transition-duration: 1s;
    width: 100vw;
    height: auto;
    position:fixed;
    left: 0%;
    top: 0%;
    transition-property: width height opacity;
    z-index:9999999;
  }

  .gradient {

  margin-top:128px;
  background-image:url('../images/background.png');
  width:100vw;
  height:150vh;
  background-size:100vw 150vh;
  z-index: -1;
  position: absolute;

  }


  .movie-view-wrapper {
    /* background-color: black; */
    
    text-align: left;
    
    
  }
  .movie-list-wrapper {
    /* background-color: black; */
    background: linear-gradient(rgba(0, 0, 0, 0), rgb(0, 0, 0, 1), rgb(0, 0, 0, 1), rgb(0, 0, 0, 1), rgb(0, 0, 0, 1));
    padding-top: 12vh;
    text-align: left;
    /* overflow: hidden; */
  }
  .background-movie-form {
    margin-top: 2vh;
    margin-left: 5vw;

    /* position: absolute; */

  }
  .background-movie-title-width {
    font-size: 4vw;
    display: inline;
  }
  .background-movie-title-height {
    font-size: 6vh;
    display: inline;
  }
  .background-movie-overview {
    /* width: 60vh;
    max-height: 144px;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 5 (integer);
    overflow: hidden;
    text-overflow: ellipsis; */

    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    width: 60vh;
    max-height: 144px;
    -webkit-line-clamp: 3; /* 표시하고자 하는 라인 수 */
    -webkit-box-orient: vertical;
  }

  .background-movie-button {
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 150px;
    height: 60px;
    backdrop-filter: blur(10px);

    border: 1px solid rgba(255, 255, 255, 0.4);
    transition-duration: 0.5s;
    transition-property: background-color backdrop-filter border;
    color: rgba(255, 255, 255, 0.9);
    cursor: pointer;
  }
  .background-movie-button:hover {
    border: 1px solid rgba(255, 255, 255, 0.6);
    background-color: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
  }

  .background-movie-button-font {
    opacity: 100%;
    user-select : none;
    font-size: 24px;
  }
  .category-title {
    font-size: 30px;
    margin-top: -20px;
    margin-bottom: -10px;
    margin-left: 5vw;
    z-index:999999;
  }



</style>