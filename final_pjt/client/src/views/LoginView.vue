<template>
  <div class="login-page-wrapper">
    <div class="wallpaper"></div>

    <div class="login-form-wrapper">
      <div class="login-content">
        <div class="login-title">SIGN IN</div>
        <!-- <AccountErrorList v-if="isAuthError" /> -->
        <form @submit.prevent="login" @keyup.enter="login">
          <input placeholder="아이디" type="text" id="username" v-model="username" class="input-box"><br>
          <input placeholder="비밀번호" type="password" id="password" v-model="password" class="input-box"><br>
          <div class="login-button" @click="login">LET'S GO</div>
          <span class="signup-label">아직 회원이 아니신가요?{{'\u00a0'}}{{'\u00a0'}}{{'\u00a0'}}</span>
          <span class="signup-router" @click="signupButton">회원가입</span>
          <!-- <input type="submit" value="login"> -->
        </form>
      </div>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'
import router from '@/router'
// import AccountErrorList from '@/components/AccountErrorList'
import { mapGetters } from 'vuex'


export default {
  name: 'LoginView',
  components: {
    // AccountErrorList,
  },
  data() {
    return {
      username: null,
      password: null,
    }
  },
  computed: {
    backgroundMovie() {
      const movie = this.$store.state.backgroundMovie
      return movie
    },
    ...mapGetters(['isAuthError'])
  },
  methods: {
    login() {
      const API_URL = "http://127.0.0.1:8000"
      const username = this.username
      const password = this.password

      const payload = {
        username,
        password
      }
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password
        }
      })
        .then(res => {
          this.$store.commit('SAVE_TOKEN_WITHOUT_ROUTER', res.data.key)
          this.$store.dispatch('login')
          const token = res.data.key
          axios({
            method: 'get',
            url: `${API_URL}/accounts/get_additional_user_info/`,
            headers: {
              Authorization: `Token ${token}`
            }
          })
            .then((res) => {

              this.$store.commit('IDENTIFY_NEW_USER', res.data.new_user)

            })
            .catch((err) => {
              console.log(err)
            })
          const bodyTag = document.querySelector('body')
          bodyTag.style.overflow = 'hidden'

          const wrapperTag = document.querySelector('.login-form-wrapper')
          const contentTag = document.querySelector('.login-content')
          wrapperTag.style.borderRadius = '100000px'
          wrapperTag.style.backdropFilter = 'blur(10px)'
          wrapperTag.style.width = '300%'
          wrapperTag.style.height = '300%'
          contentTag.style.opacity = 0
          setTimeout(() => {
            wrapperTag.style.opacity = 0
            setTimeout(() => {
              
              this.$store.commit('WALLPAPER_FIX_ON')
              const bodyTag = document.querySelector('body')
              bodyTag.style.overflowY = 'scroll'
              
              if (this.$store.state.isNewUser === true) {
                console.log(this.$store.state.isNewUser)

                this.$store.commit('SAVE_TOKEN_WITHOUT_ROUTER', res.data.key)
                this.$router.push({name: 'SignupSelectMovies'})
              } else {
                this.$store.commit('SAVE_TOKEN', res.data.key)
              }
              
              
            }, 800);
          }, 1000);

          
        })
        .catch((err) => {
          console.log(err)
          this.$store.commit('SET_AUTH_ERROR', err.response.data)
          alert('존재하지 않는 계정이거나 잘못된 정보입니다.')
        })
      
      // 
    },
    signupButton() {
      router.push({name: 'signup'})
    }
  },
  mounted() {
    this.$store.commit('NAVBAR_SHOW_OFF')
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
    //     const bodyTag = document.querySelector('.wallpaper')
    //     bodyTag.setAttribute(`style`, `background-image:url('https://image.tmdb.org/t/p/original${this.backgroundMovie.backdrop_path}'); width: 100vw; height: 100vh;  background-size:cover; background-color: black; position:absolute; background-repeat:no-repeat; -webkit-filter: brightness(60%); background-attachment: fixed;`)
    //     // const bodyTag = document.querySelector('#app')
    //     // bodyTag.setAttribute(`style`, `z-index:-10; width: 100vw; height: 100vh; background-size:100vw; position:absolute; background-color: black;`)
    //   })
    //   .catch(error => {
    //     console.log('receiveTopRatedData => ', error)
    //   })
      
    
  }
}
</script>

<style>
  .login-page-wrapper {
    margin-top:-72px;
    width: 100vw;
    height: 100vh;
    display:flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.6);
  }
  .login-form-wrapper {
    transition-duration: 1s;
    transition-property: width height opacity;
    width: 30vw;
    height: 400px;
    min-width: 600px;
    min-height: 400px;
    background-color: rgba(255, 255, 255, 0.1);
    display: flex;
    justify-content: center;
    padding-top:50px;
    z-index: 9999;;
    backdrop-filter: blur(10px);
    box-shadow: 0px 0px 2px 1px rgba(0, 0, 0, 0.200);
    border-radius: 2px;
  }
  /* .left-box {
    border-radius: 5px 0px 0px 5px;
    width:40%;
    height:100%;
    overflow: hidden;
    position: relative;
  } */
  /* .login-image {
    background-image:url('../images/login-1.jpg');
    width:100%;
    height:100%;
    background-size: 100%;
    background-color: black;
    position:absolute;

    background-repeat:no-repeat;
  } */

  .login-content {
    text-align: left;
    transition-duration: 0.5s;
    transition-property: opacity;
  }
  .input-box {
    border: 0px;
    /* border-radius: 3px;; */
    background-color: rgba(255, 255, 255, 0);
    border-bottom: 2px rgba(255, 255, 255, 0.2) solid;
    min-width: 400px;
    width: 20vw;
    height: 40px;
    /* background-color: rgba(255, 255, 255, 0); */
    outline: none;
    color: white;
    transition-duration: 0.5s;
    transition-property: border background-color top opacity;
    margin-bottom:20px;
  }
  .input-box::placeholder {
    color: white;
  }
  .input-box:focus {
    border-bottom: 2px rgb(255, 255, 255) solid;
    background-color: #e8f0fe80;
    box-shadow: 0px 0px 3px 1px rgba(0, 0, 0, 0.3);
    /* background: linear-gradient(rgba(255, 255, 255, 0) 50% , rgba(255, 255, 255, 0.3)); */
  }
  .login-title {
    min-width: 400px;

    text-align: left;
    margin-bottom: 10px;
    width: 20vw;
    font-size: 36px;;
  }
  .login-button {
    margin-top:10px;
    border-radius: 3px;
    box-shadow: 0px 0px 10px 1px rgba(0, 0, 0, 0.1);
    transition-duration: 0.5s;
    transition-property: background-color;
    background-color: #ff0000b5;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 20vw;
    min-width: 400px;
    height: 48px;
    margin-bottom: 10px;
  }
  .login-button:hover {
    
    user-select: none;
    cursor: pointer;
    background-color: #ff0000;
  }
  .signup-label {
    color: rgba(255, 255, 255, 0.5);
    text-decoration: none;
    font-size: 13px;
  }
  .signup-router {
    transition-duration: 0.5s;
    transition-property: color;
    color: rgba(255, 255, 255, 0.7);
    text-decoration: none;
    font-size: 13px;
    cursor: pointer;
  }
  
  .signup-router:hover {
    color: rgb(255, 255, 255);
    text-decoration: none;
  }
</style>