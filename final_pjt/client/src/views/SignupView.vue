<template>
  <div class="signup-page-wrapper">
    <div class="wallpaper"></div>

    <div class="signup-form-wrapper">
      <div class="signup-content">
        <div class="signup-title">SIGN UP</div>
        <!-- <AccountErrorList v-if="isAuthError" /> -->
        <!-- <form @submit.prevent="login"> -->
          <input placeholder="아이디" type="text" id="username" v-model="username" class="input-box"><br>
          <div class="id-alert alert-text" style="color:red; font-size:12px; margin-bottom:6px; margin-top:-20px; font-weight: bold;">{{'\u00a0'}}</div>
          <input placeholder="닉네임" type="text" id="nickname" @input="getNickname" class="input-box"><br>
          <div class="nickname-alert alert-text" style="color:red; font-size:12px; margin-bottom:6px; margin-top:-20px; font-weight: bold;">{{'\u00a0'}}</div>
          <input placeholder="이메일" type="text" id="email" v-model="email" class="input-box"><br>
          <div class="email-alert alert-text" style="color:red; font-size:12px; margin-bottom:6px; margin-top:-20px; font-weight: bold;">{{'\u00a0'}}</div>
          <input placeholder="비밀번호" type="password" id="password1" v-model="password1" class="input-box"><br>
          <div class="password1-alert alert-text" style="color:red; font-size:12px; margin-bottom:6px; margin-top:-20px; font-weight: bold;">{{'\u00a0'}}</div>
          <input placeholder="비밀번호 확인" type="password" id="password2" v-model="password2" class="input-box"><br>
          <div class="password2-alert alert-text" style="color:red; font-size:12px; margin-bottom:6px; margin-top:-20px; font-weight: bold;">{{'\u00a0'}}</div>
          <div class="signup-button" @click="signup">JOIN</div>
          
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
  name: 'SignupView',
  data() {
    return {
      username: '',
      nickname: '',
      email: null,
      password1: '',
      password2: '',
      validation: {id: false, nickname: false, email: false, password1: false, password2: false}
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
    getNickname(event) {
      this.nickname = event.target.value
    },
    signup() {
      for (const key in this.validation) {
        if (this.validation[key] === false) {
          alert('정보를 제대로 입력해 주세요.')
          return
        }
      }
      const API_URL = "http://127.0.0.1:8000"
      const username = this.username
      const nickname = this.nickname
      const email = this.email
      const password1 = this.password1
      const password2 = this.password2
      console.log(username, email, password1, password2)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          nickname,
          email,
          password1,
          password2,
        }
      })
        .then(() => {
          router.push({name: 'login'})
        })
        .catch((err) => {
          this.$store.commit('SET_AUTH_ERROR', err.response.data)
          alert('이미 존재하는 ID이거나 EMAIL이 이미 등록되어 있습니다.')
          console.log(err)
        })
    }

  },
  mounted() {
    this.$store.commit('NAVBAR_SHOW_OFF')
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
    username(val) {
      const idAlert = document.querySelector('.id-alert')
      const idInput = document.querySelector('#username')
      const nicknameInput = document.querySelector('#nickname')
      const emailInput = document.querySelector('#email')
      const password1Input = document.querySelector('#password1')
      const password2Input = document.querySelector('#password2')
      // idInput.setAttribute('style', '')
      nicknameInput.setAttribute('style', '')
      emailInput.setAttribute('style', '')
      password1Input.setAttribute('style', '')
      password2Input.setAttribute('style', '')
      const idValidation = /^[A-Za-z0-9]+$/.test(val)
      if ( idValidation) {
        if (val.trim() === '' || val.length < 4) {
          idAlert.innerText = '아이디는 최소 4자 이상 입력해야 합니다.'
          idInput.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.id = false
        } else if (val.length >= 15) {
          idAlert.innerText = '아이디는 최대 15자까지 입력할 수 있습니다.'
          idInput.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.id = false
        } else {
          idAlert.innerText = '\u00a0'
          this.validation.id = true
          idInput.setAttribute('style', 'border-bottom: 2px rgb(255, 255, 255) solid; background-color: #e8f0fe80;')
        }
      } else {
        if (val.trim() === '') {
          idAlert.innerText = '아이디는 최소 4자 이상 입력해야 합니다.'
          idInput.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.id = false
        } else {
          idAlert.innerText = '아이디에 사용할 수 없는 문자가 포함되어 있습니다.'
          idInput.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.id = false
        }
          
      }
    },
    nickname(val) {
      const nicknameAlert = document.querySelector('.nickname-alert')
      const idInput = document.querySelector('#username')
      const nicknameInput = document.querySelector('#nickname')
      const emailInput = document.querySelector('#email')
      const password1Input = document.querySelector('#password1')
      const password2Input = document.querySelector('#password2')
      idInput.setAttribute('style', '')
      // nicknameInput.setAttribute('style', '')
      emailInput.setAttribute('style', '')
      password1Input.setAttribute('style', '')
      password2Input.setAttribute('style', '')
      const nicknameValidation = /^[A-Za-z0-9ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+$/.test(val)
      if ( nicknameValidation) {
        if (val.trim() === '' || val.length < 3) {
          nicknameAlert.innerText = '닉네임은 최소 3자 이상 입력해야 합니다.'
          nicknameInput.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.nickname = false
        } else if (val.length >= 15) {
          nicknameAlert.innerText = '닉네임은 최대 15자까지 입력할 수 있습니다.'
          nicknameInput.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.nickname = false
        } else {
          nicknameAlert.innerText = '\u00a0'
          this.validation.nickname = true
          nicknameInput.setAttribute('style', 'border-bottom: 2px rgb(255, 255, 255) solid; background-color: #e8f0fe80;')
        }
      } else {
        if (val.trim() === '') {
          nicknameAlert.innerText = '닉네임은 최소 3자 이상 입력해야 합니다.'
          nicknameInput.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.nickname = false
        } else {
          nicknameAlert.innerText = '닉네임에 사용할 수 없는 문자가 포함되어 있습니다.'
          nicknameInput.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.nickname = false
        }
          
      }
    },
    email(val) {
      const emailAlert = document.querySelector('.email-alert')
      const idInput = document.querySelector('#username')
      const nicknameInput = document.querySelector('#nickname')
      const emailInput = document.querySelector('#email')
      const password1Input = document.querySelector('#password1')
      const password2Input = document.querySelector('#password2')
      idInput.setAttribute('style', '')
      nicknameInput.setAttribute('style', '')
      // emailInput.setAttribute('style', '')
      password1Input.setAttribute('style', '')
      password2Input.setAttribute('style', '')
      const emailValidation = /^[A-Za-z0-9_\\.\\-]+@[A-Za-z0-9\\-]+\.[A-Za-z0-9\\-]+/.test(val)
      if (emailValidation) {
        emailAlert.innerText = '\u00a0'
        emailInput.setAttribute('style', 'border-bottom: 2px rgb(255, 255, 255) solid; background-color: #e8f0fe80;')
        this.validation.email = true
      } else {
        if (val.trim() === '') {
          emailAlert.innerText = '이메일은 필수 사항입니다.'
          emailInput.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.email = false
        } else {
          emailAlert.innerText = '이메일을 양식에 맞게 입력해 주세요.'
          emailInput.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.email = false
        }
        
      }
    },
    password1(val) {
      const passwordAlert = document.querySelector('.password1-alert')
      const idInput = document.querySelector('#username')
      const nicknameInput = document.querySelector('#nickname')
      const emailInput = document.querySelector('#email')
      const password1Input = document.querySelector('#password1')
      const password2Input = document.querySelector('#password2')
      idInput.setAttribute('style', '')
      nicknameInput.setAttribute('style', '')
      emailInput.setAttribute('style', '')
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
    password2(val) {
      const passwordAlert = document.querySelector('.password2-alert')
      const idInput = document.querySelector('#username')
      const nicknameInput = document.querySelector('#nickname')
      const emailInput = document.querySelector('#email')
      const password1Input = document.querySelector('#password1')
      const password2Input = document.querySelector('#password2')
      idInput.setAttribute('style', '')
      nicknameInput.setAttribute('style', '')
      emailInput.setAttribute('style', '')
      password1Input.setAttribute('style', '')
      // password2Input.setAttribute('style', '')
      // const passwordValidation = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,16}$/.test(val)
      if (val !== this.password1) {
          passwordAlert.innerText = '비밀번호가 일치하지 않습니다.'
          password2Input.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
          this.validation.password2 = false
        } else {
          passwordAlert.innerText = '\u00a0'
          password2Input.setAttribute('style', 'border-bottom: 2px rgb(255, 255, 255) solid; background-color: #e8f0fe80;')
          this.validation.password2 = true
        }
      // if (passwordValidation) {
      //   if (val !== this.password1) {
      //     passwordAlert.innerText = '비밀번호가 일치하지 않습니다.'
      //     password2Input.setAttribute('style', 'border-bottom: 2px red solid; background-color: rgba(255, 0, 0, 0.342);')
      //     this.validation.password2 = false
      //   } else {
      //     passwordAlert.innerText = '\u00a0'
      //     password2Input.setAttribute('style', 'border-bottom: 2px rgb(255, 255, 255) solid; background-color: #e8f0fe80;')
      //     this.validation.password2 = true
      //   }
          
      // } else {
      //   if (val !== this.password1) {
      //     passwordAlert.innerText = '비밀번호가 일치하지 않습니다.'
      //     this.validation.password2 = false
      //   } else if (val.trim() === '' || val.length < 8) {
      //     passwordAlert.innerText = '비밀번호는 최소 8자 이상 입력해야 합니다.'
      //     this.validation.password2 = false
      //   } else if (val.length > 16) {
      //     passwordAlert.innerText = '비밀번호는 최대 16자까지 입력할 수 있습니다.'
      //     this.validation.password2 = false
      //   } else {
      //     passwordAlert.innerText = '비밀번호는 대문자/소문자/숫자가 1개 이상 반드시 포함되어야 합니다.'
      //     this.validation.password2 = false
      //   }
        
      // }
    }
  }
}
</script>

<style>
  .signup-page-wrapper {
    margin-top:-72px;
    width: 100vw;
    height: 100vh;
    display:flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.6);
  }
  .signup-form-wrapper {
    transition-duration: 1s;
    transition-property: width height opacity;
    width: 30vw;
    height: 550px;
    min-width: 600px;
    min-height: 550px;
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

  .signup-content {
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
  .signup-title {
    min-width: 400px;
    text-align: left;
    margin-bottom: 10px;
    width: 20vw;
    font-size: 36px;;
  }
  .signup-button {
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
  .signup-button:hover {
    
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

  .alert-text {
    color:red;
    font-size:12px;
    margin-bottom:6px;
    margin-top:-20px;
    font-weight: bold;
  }
</style>