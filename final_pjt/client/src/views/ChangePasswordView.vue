<template>
  <div class="change-password-page-wrapper">
    <div class="wallpaper"></div>

    <div class="change-password-form-wrapper">
      <div class="change-password-content">
        <div class="change-password-title">회원정보 수정</div>
        <!-- <AccountErrorList v-if="isAuthError" /> -->
        <!-- <form @submit.prevent="login"> -->
          <input placeholder="기존 비밀번호" type="password" id="old-password" v-model="old_password" class="input-box"><br>
          <div class="old-password-alert alert-text" style="color:red; font-size:12px; margin-bottom:6px; margin-top:-20px; font-weight: bold;">{{'\u00a0'}}</div>
          <input placeholder="새 비밀번호" type="password" id="password1" v-model="new_password1" class="input-box"><br>
          <div class="password1-alert alert-text" style="color:red; font-size:12px; margin-bottom:6px; margin-top:-20px; font-weight: bold;">{{'\u00a0'}}</div>
          <input placeholder="새 비밀번호 확인" type="password" id="password2" v-model="new_password2" class="input-box"><br>
          <div class="password2-alert alert-text" style="color:red; font-size:12px; margin-bottom:6px; margin-top:-20px; font-weight: bold;">{{'\u00a0'}}</div>
          <div class="change-password-button" @click="changePassword">CHANGE</div>
          
          <!-- <input type="submit" value="login"> -->
        <!-- </form> -->
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
  name: 'ChangePasswordView',
  data() {
    return {
      new_password1: '',
      new_password2: '',
      old_password: '',
      validation: {password1: false, password2: false, old_password: false}
    }
  },
  components: {
    // AccountErrorList
  },
  computed: {
    backgroundMovie() {
      const movie = this.$store.state.backgroundMovie
      return movie
    },
    ...mapGetters(['isAuthError'])
  },
  methods: {
    changePassword(){
      const API_URL = "http://127.0.0.1:8000"
      const new_password1 = this.new_password1
      const new_password2 = this.new_password2
      const old_password = this.old_password
 
      axios({
        method: 'post',
        url : `${API_URL}/accounts/password/change/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data:{
          new_password1,
          new_password2,
          old_password,
        }
      })
      .then((response) =>{
        router.push({name: 'movie'})
        console.log(response)
    
      })
      .catch((error) =>{
        console.log(error)
      })

    }

  },
  mounted() {
    // if (this.$store.state.backgroundMovie !== null) {
    //   const bodyTag = document.querySelector('.wallpaper')
    //   bodyTag.setAttribute(`style`, `background-image:url('https://image.tmdb.org/t/p/original${this.backgroundMovie.backdrop_path}'); width: 100vw; height:100vh;  background-size:cover; background-color: black; position:absolute; background-repeat:no-repeat; -webkit-filter: brightness(60%);`)
    // }
    // if (this.$store.state.backgroundMovie === null) {
    //   const URL = 'http://127.0.0.1:8000/movies/get_popular_movies/'
    //   axios({
    //     method: 'GET',
    //     url: URL,
    //   })
    //     .then(response => {
    //       const movies = response.data
    //       let selected = _.sample(_.range(0, movies.length))
    //       while (movies[selected].overview === '') {
    //         selected = _.sample(_.range(0, movies.length))
    //       }
    //       this.$store.commit('BACKGROUND_MOVIE', response.data[selected])
    //       const bodyTag = document.querySelector('.wallpaper')
    //       bodyTag.setAttribute(`style`, `background-image:url('https://image.tmdb.org/t/p/original${this.backgroundMovie.backdrop_path}'); width: 100vw; height:100vh;  background-size:cover; background-color: black; position:absolute; background-repeat:no-repeat; -webkit-filter: brightness(60%);`)
    //       // const bodyTag = document.querySelector('#app')
    //       // bodyTag.setAttribute(`style`, `z-index:-10; width: 100vw; height: 100vh; background-size:100vw; position:absolute; background-color: black;`)
    //     })
    //     .catch(error => {
    //       console.log('receiveTopRatedData => ', error)
    //     })
    // }
  },
  watch: {
    new_password1(val) {
      const passwordAlert = document.querySelector('.password1-alert')

      const password1Input = document.querySelector('#password1')
      const password2Input = document.querySelector('#password2')
      // password1Input.setAttribute('style', '')
      password2Input.setAttribute('style', '')

      const passwordValidation = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,16}$/.test(val)
      if (passwordValidation) {
          passwordAlert.innerText = '\u00a0'
          password1Input.setAttribute('style', 'border-bottom: 2px rgb(255, 255, 255) solid; background-color: #e8f0fe80;')
          this.validation.password1 = true
      } else {
        if (val.trim() === '' || val.length < 8) {
          passwordAlert.innerText = '비밀번호는 최소 8자 이상 입력해야 합니다.'
          password1Input.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.password1 = false
        } else if (val.length > 16) {
          passwordAlert.innerText = '비밀번호는 최대 16자까지 입력할 수 있습니다.'
          password1Input.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.password1 = false
        } else {
          passwordAlert.innerText = '비밀번호는 대문자/소문자/숫자가 1개 이상 반드시 포함되어야 합니다.'
          password1Input.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.password1 = false
        }
        
      }
    },
    new_password2(val) {
      const passwordAlert = document.querySelector('.password2-alert')
      const password1Input = document.querySelector('#password1')
      const password2Input = document.querySelector('#password2')
      password1Input.setAttribute('style', '')
      // password2Input.setAttribute('style', '')
      // const passwordValidation = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,16}$/.test(val)
      if (val !== this.new_password1) {
          passwordAlert.innerText = '비밀번호가 일치하지 않습니다.'
          password2Input.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.password2 = false
        } else {
          passwordAlert.innerText = '\u00a0'
          password2Input.setAttribute('style', 'border-bottom: 2px rgb(255, 255, 255) solid; background-color: #e8f0fe80;')
          this.validation.password2 = true
        }

    }
  }
}
</script>

<style>
  .change-password-page-wrapper {
    margin-top:-72px;
    width: 100vw;
    height: 100vh;
    display:flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.6);
  }
  .change-password-form-wrapper {
    transition-duration: 1s;
    transition-property: width height opacity;
    width: 30vw;
    height: 420px;
    min-width: 600px;
    min-height: 420px;
    background-color: rgba(255, 255, 255, 0.1);
    display: flex;
    justify-content: center;
    padding-top:50px;
    z-index: 9999;;
    backdrop-filter: blur(10px);
    box-shadow: 0px 0px 2px 1px rgba(0, 0, 0, 0.200);
    border-radius: 2px;
  }

  .change-password-content {
    text-align: left;
    transition-duration: 0.5s;
    transition-property: opacity;
  }
  .input-box {
    min-width: 400px;
    border: 0px;
    /* border-radius: 3px;; */
    background-color: rgba(255, 255, 255, 0);
    border-bottom: 2px rgba(255, 255, 255, 0.2) solid;
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
  .change-password-title {
    min-width: 400px;
    text-align: left;
    margin-bottom: 10px;
    width: 20vw;
    font-size: 36px;;
  }
  .change-password-button {
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
  .change-password-button:hover {
    
    user-select: none;
    cursor: pointer;
    background-color: #ff0000;
  }
  .change-password-label {
    color: rgba(255, 255, 255, 0.5);
    text-decoration: none;
    font-size: 13px;
  }
  .change-password-router {
    transition-duration: 0.5s;
    transition-property: color;
    color: rgba(255, 255, 255, 0.7);
    text-decoration: none;
    font-size: 13px;
    cursor: pointer;
  }
  
  .change-password-router:hover {
    color: rgb(255, 255, 255);
    text-decoration: none;
  }

  .alert-text {
    color:red;
    font-size:12px;
    margin-bottom:6px;
    margin-top:-20px;
    font-weight: bold;
  }
</style>