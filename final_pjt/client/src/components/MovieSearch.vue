<template>
  <div class="search-wrapper">
    <div class="search-inner-form">
      <!-- <div style="width:100%; display:flex; justify-content:center;"> -->

        <div class="search-input-form" style="width:100%; display:flex; justify-content:center;">
          <input type="text" placeholder="영화 이름을 입력해 주세요." @input="getWord" class="searchInput">
          <div class="search-button" @click="getMovie">검색</div>
          <div class="search-hide-button" @click="hideSearchForm">취소</div>
        </div>
          

        
      <!-- </div> -->
      

      <div class="search-card-wrapper">
        <div class="container text-center" style="margin-top:100px;">
          <div class="row row-cols-5">

            
            <div v-for="(movie, idx) in searchMovieList" :key="idx" style=" margin-bottom:20px;">
              <MovieSearchCard :movie="movie" :identifier="identifier"/>
              
            </div>
          </div>
          
        </div>
      </div>
      
      
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import MovieSearchCard from '@/components/MovieSearchCard'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieSearch',
  components: {
    MovieSearchCard,
  },
  data() {
    return {
      searchWord: null,
      searchMovieList: null,
      identifier: 'searchMovie'
    }
  },
  methods: {
    getWord(event) {
      this.searchWord = event.target.value
    },
    getMovie() {
      if (this.searchWord.trim() !== '') {

      
        const searchWord = this.searchWord
        axios({
          method: 'get',
          url: `${API_URL}/movies/get_search_movies/`,
          params: {
            searchWord
          },
        })
          .then((res) => {
            this.searchMovieList = res.data.slice(0,15)

          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    hideSearchForm() {
      const bodyTag = document.querySelector('body')
      bodyTag.style.overflowY = 'scroll'
      
      const searchForm = document.querySelector('.search-form')
      const searchInnerForm = document.querySelector('.search-inner-form')
      
      searchInnerForm.style.opacity = '0%'
      searchInnerForm.style.width = '100vw'
      searchInnerForm.style.height = '300vh'
      // searchForm.style.backgroundColor = 'rgba(0, 0, 0, 0)'
      setTimeout(() => {
        
        searchForm.style.top = '-300%'
        this.searchMovieList = null
        this.searchWord = null
      }, 1000);
    }
    

  },
  watch: {
    searchWord(val) {
      if (val.trim() !== '') {
      const searchWord = this.searchWord
      axios({
        method: 'get',
        url: `${API_URL}/movies/get_search_movies/`,
        params: {
          searchWord
        },
      })
        .then((res) => {
          this.searchMovieList = res.data.slice(0,15)

        })
        .catch((err) => {
          console.log(err)
        })
      }
    }
  }

}
</script>

<style>
* {
  font-family: 'SUIT', sans-serif;
}
.search-wrapper {
  transition-duration: 0.2s;
  transition-property: top background-color ;
  /* background-color: rgba(0, 0, 0, 0.3); */
  top:-300%;
  left: 0%;
  position: fixed;
  width:100vw;
  height:100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index:99999998;
  
}
.search-inner-form {

  
  transition-duration: 1s;
  transition-property: width height opacity 1s;
  width: 100vw;
  height: 300vh;
  opacity: 0;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(20px);
  /* box-shadow: 0px 0px 5px 1px rgba(0, 0, 0, 0.700); */
  /* border-radius: 10px; */
  z-index:99999999;
  padding:32px;
  padding-top:48px;
  
  
}
.search-input-form {
  display:flex;

}

.search-card-wrapper {
/* 
  display:flex;
  justify-content:center; */
  width:100%;
  height:100%;
}

.search-button {
  transition-duration: 0.5s;
  transition-property: background-color;
  background-color: rgba(255, 255, 255, 0.10);
  border-radius: 0px 10px 10px 0px;
  width:7%;
  height:64px;
  display: flex;
  justify-content: center;
  align-items:center;
  color:white;
  cursor: pointer;
  /* text-shadow: 0px 0px 2px rgb(0, 0, 0); */
}

.search-hide-button {
  transition-duration: 0.5s;
  transition-property: background-color;
  background-color: rgba(255, 255, 255, 0.10);
  border-radius: 10px;
  width:7%;
  margin-left:16px;
  height:64px;
  display: flex;
  justify-content: center;
  align-items:center;
  color:white;
  cursor: pointer;
  /* text-shadow: 0px 0px 2px rgb(0, 0, 0); */
}
.search-hide-button:hover {
  background-color: rgba(255, 255, 255, 0.05);
}

.search-button:hover {
  background-color: rgba(255, 255, 255, 0.05);
}

.searchInput {
  width:40%;
  height:64px;
  padding-left:16px;
  border: 0px rgb(0, 0, 0) none;
  outline: none;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 10px 0px 0px 10px;
  color:rgba(255, 255, 255, 1);
  /* text-shadow: 0px 0px 2px rgb(0, 0, 0); */
}
.searchInput::placeholder {
    color: rgba(255, 255, 255, 0.5);
  }


</style>