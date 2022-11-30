<template>
  <div class="movie-view-wrapper">

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
      <button type="button" class="btn btn-light background-movie-button"><span class="background-movie-button-font"><b>상세 정보</b></span></button>

      

    </div>


    <div class="movie-list-wrapper">
      <div class="category-title"><b>Top Rated 20</b></div>
      <div v-if="browserWidth < 768">
        <MovieCard2 :movieList="topRatedList" :splitted="topRatedListSplitter" :identifier="`topRated`"/>
      </div>
      <div v-if="browserWidth >= 768 && browserWidth < 992">
        <MovieCard3 :movieList="topRatedList" :splitted="topRatedListSplitter" :identifier="`topRated`"/>
      </div>
      <div v-if="browserWidth >= 992 && browserWidth < 1200">
        <MovieCard4 :movieList="topRatedList" :splitted="topRatedListSplitter" :identifier="`topRated`"/>
      </div>
      <div v-if="browserWidth >= 1200 && browserWidth < 1600">
        <MovieCard5 :movieList="topRatedList" :splitted="topRatedListSplitter" :identifier="`topRated`"/>
      </div>
      <div v-if="browserWidth >= 1600 && browserWidth < 1920">
        <MovieCard6 :movieList="topRatedList" :splitted="topRatedListSplitter" :identifier="`topRated`"/>
      </div>
      <div v-if="browserWidth >= 1920 && browserWidth < 2160">
        <MovieCard7 :movieList="topRatedList" :splitted="topRatedListSplitter" :identifier="`topRated`"/>
      </div>
      <div v-if="browserWidth >= 2160 && browserWidth < 2320">
        <MovieCard8 :movieList="topRatedList" :splitted="topRatedListSplitter" :identifier="`topRated`"/>
      </div>
      <div v-if="browserWidth >= 2320">
        <MovieCard9 :movieList="topRatedList" :splitted="topRatedListSplitter" :identifier="`topRated`"/>
      </div>
      
      <br>
      <div class="category-title"><b>Popular</b></div>
      <div v-if="browserWidth < 768">
        <MovieCard2 :movieList="popularList" :splitted="popularListSplitter" :identifier="`popular`"/>
      </div>
      <div v-if="browserWidth > 768 && browserWidth < 992">
        <MovieCard3 :movieList="popularList" :splitted="popularListSplitter" :identifier="`popular`"/>
      </div>
      <div v-if="browserWidth > 992 && browserWidth < 1200">
        <MovieCard4 :movieList="popularList" :splitted="popularListSplitter" :identifier="`popular`"/>
      </div>
      <div v-if="browserWidth > 1200 && browserWidth < 1600">
        <MovieCard5 :movieList="popularList" :splitted="popularListSplitter" :identifier="`popular`"/>
      </div>
      <div v-if="browserWidth >= 1600 && browserWidth < 1920">
        <MovieCard6 :movieList="popularList" :splitted="popularListSplitter" :identifier="`popular`"/>
      </div>
      <div v-if="browserWidth >= 1920 && browserWidth < 2160">
        <MovieCard7 :movieList="popularList" :splitted="popularListSplitter" :identifier="`popular`"/>
      </div>
      <div v-if="browserWidth >= 2160 && browserWidth < 2320">
        <MovieCard8 :movieList="popularList" :splitted="popularListSplitter" :identifier="`popular`"/>
      </div>
      <div v-if="browserWidth >= 2320">
        <MovieCard9 :movieList="popularList" :splitted="popularListSplitter" :identifier="`popular`"/>
      </div>

    

      <div class="fill-black">
          
      </div>
      
    
    </div>
 
  </div>
</template>

<script>
import MovieCard2 from '@/components/MovieCard2'
import MovieCard3 from '@/components/MovieCard3'
import MovieCard4 from '@/components/MovieCard4'
import MovieCard5 from '@/components/MovieCard5'
import MovieCard6 from '@/components/MovieCard6'
import MovieCard7 from '@/components/MovieCard7'
import MovieCard8 from '@/components/MovieCard8'
import MovieCard9 from '@/components/MovieCard9'
import axios from 'axios'


export default {
  name: 'MovieView',
  components: {
    MovieCard2,
    MovieCard3,
    MovieCard4,
    MovieCard5,
    MovieCard6,
    MovieCard7,
    MovieCard8,
    MovieCard9,
  },
  data() {
    return {
      browserWidth: null,
      browserHeight: null,
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
    topRatedListSplitter() {
      const listLength = this.$store.state.topRatedList.length
      const splitted = [[]]
      for (let j = 1; j <= 9; j++) {
        splitted.push([])
        for (let i = j; listLength - 1 > i; i++) {
          if (i % j === 0) {
            splitted[j].push([])
            splitted[j][splitted[j].length - 1].push(i)
          } else {
            splitted[j][splitted[j].length - 1].push(i)
          }
        }
      }

      
      return splitted
    },
    // topRatedListSplitter() {
    //   const listLength = this.$store.state.topRatedList.length
    //   const splitted = []
    //   for (let i = 6; listLength - 1 > i; i++) {
    //     if (i % 6 === 0) {
    //       splitted.push([])
    //       splitted[splitted.length - 1].push(i)
    //     } else {
    //       splitted[splitted.length - 1].push(i)
    //     }
    //   }
      
    //   return splitted
    // },
    popularList() {
      return this.$store.state.popularList
    },
    popularListSplitter() {
      const listLength = this.$store.state.popularList.length
      const splitted = [[]]
      for (let j = 1; j <= 9; j++) {
        splitted.push([])
        for (let i = j; listLength - 1 > i; i++) {
          if (i % j === 0) {
            splitted[j].push([])
            splitted[j][splitted[j].length - 1].push(i)
          } else {
            splitted[j][splitted[j].length - 1].push(i)
          }
        }
      }


      return splitted
    },
    // popularListSplitter() {
    //   const listLength = this.$store.state.popularList.length
    //   const splitted = []
      
    //   for (let i = 6; listLength - 1 > i; i++) {
    //     if (i % 6 === 0) {
    //       splitted.push([])
    //       splitted[splitted.length - 1].push(i)
    //     } else {
    //       splitted[splitted.length - 1].push(i)
    //     }
    //   }
      
    //   return splitted
    // }
  },
  methods: {
    receiveTopRatedData() {
      this.$store.dispatch('receiveTopRatedData')
    },
    receivePopularData() {
      this.$store.dispatch('receivePopularData')
    },
  },
  created() {
    this.receiveTopRatedData()
    this.receivePopularData()
    this.browserWidth = document.body.offsetWidth
    this.browserHeight = window.innerHeight
    this.$store.commit('IS_DETAIL_MODE', false)

    const API_URL = "http://127.0.0.1:8000"

    axios({
      method: 'get',
      url: `${API_URL}/accounts/user/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`
      }
    })
      .then((res) => {
        this.$store.commit('GET_USER_INFO', res.data)
        console.log(res)
    })
      .catch((err) => {
        console.log(err)
    })
    
  },
  mounted() {
    window.onresize = (() => {
      this.browserWidth = document.body.offsetWidth //event.delegateTarget.innerWidth
      this.browserHeight = window.innerHeight
    });



  }
}
</script>

<style>

  .movie-view-wrapper {
    text-align: left;
    
  }
  .movie-list-wrapper {
    padding-top: 10vh;
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
    -webkit-line-clamp: 5; /* 표시하고자 하는 라인 수 */
    -webkit-box-orient: vertical;
  }
  .background-movie-button {
    margin-top: 10px;
    width: 150px;
    height: 60px;
    opacity: 40%;
    border-radius: 10px;
    border: 0px;
  }

  .background-movie-button-font {
    opacity: 100%;
    color: rgba(0, 0, 0, 1);
    font-size: 24px;
  }
  .category-title {
    font-size: 4vh;
    margin-top: -20px;
    margin-left: 5vw;
  }

  .fill-black {
    left:0;
    width: 100vw;
    margin-top:-10rem;
    
    height: 600px;;


    background-color: black;
  }


</style>