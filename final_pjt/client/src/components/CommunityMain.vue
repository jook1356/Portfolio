<template>
  <div class="listBox">
    <!-- <hr style="width: 800px; margin-top: 0px;"> -->
    <h1>게시글</h1>
    <hr style="width: 800px; margin: 0px;">
    <div class="option-box">
      <router-link :to="{name: 'create'}" class="create-btn" v-if="userInfo"><i class="bi bi-pencil-square write-icon"></i> 게시글 작성</router-link>
      <div id="select-box">
        <div id="select-button" @click="openSelectBox">
          <div id="selected-value">
            <span>필터</span>
          </div>
          <div id="chevrons">
            <i class="bi bi-caret-down-fill" style="color: #9D0102; font-size: 1.3rem;"></i>
          </div>
        </div>
        <div class="options noshow">
          <div class="option" @click="filterReviews(1)">
            <span>최신순</span>
          </div>
          <div class="option" @click="filterReviews(2)">
            <span>좋아요순</span>
          </div>
          <div class="option" @click="filterReviews(3)">
            <span>조회수순</span>
          </div>
        </div>
      </div>
      <!-- <select name="filters" id="filter-select" @change="filterReviews" v-model="filter">
        <option value="0">필터</option>
        <option value="1">최신순</option>
        <option value="2">좋아요순</option>
        <option value="3">조회수순</option>
      </select> -->
    </div>
    <CommunityMainArticleList :reviews="reviews" />
    <div style="margin-bottom: 20px">
      <a id="append-article" @click.prevent="appendArticle" class="append-btn">게시글 더보기</a>
      <p id="last-review-msg" class="noshow">마지막 게시글입니다.</p>
    </div>
  </div>
</template>

<script>
import CommunityMainArticleList from "@/components/CommunityMainArticleList"

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityMain',
  components: {
    CommunityMainArticleList,
  },
  data() {
    return {
      idx: 0,
      reviews: [],
      reviews_all: [],
      reviews_all_length: 0,
      filter: 1,
    }
  },
  computed: {
    userInfo() {
      return this.$store.state.userInfo
    }
  },
  methods: {
    getArticleByNewest() {
      axios({
      method: 'get',
      url: `${API_URL}/community/review/list/`,
      })
        .then((res) => {
          this.reviews_all = res.data
          this.reviews_all_length = this.reviews_all.length
          this.reviews = []
          this.idx = 0
          this.appendArticle()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    appendArticle() {
      if (this.idx >= this.reviews_all_length) {
        const aTag = document.querySelector('#append-article')
        const pTag = document.querySelector('#last-review-msg')
        aTag?.classList.toggle('noshow')
        pTag?.classList.toggle('noshow')
      } else if (this.idx + 10 > this.reviews_all_length) {
        this.reviews = [
          ...this.reviews,
          ...this.reviews_all.slice(this.idx, this.reviews_all_length)
        ]
        this.idx += 10
      } else {
        this.reviews = [
          ...this.reviews,
          ...this.reviews_all.slice(this.idx, this.idx + 10)
        ]
        this.idx += 10
      }
    },
    getArticleByVisit() {
      axios({
        method: 'GET',
        url: `${API_URL}/community/review/list/visit/`,
      })
        .then((res) => {
          this.reviews_all = res.data
          this.reviews_all_length = this.reviews_all.length
          this.reviews = []
          this.idx = 0
          this.appendArticle()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getArticleByLike() {
      axios({
        method: 'GET',
        url: `${API_URL}/community/review/list/like/`,
      })
        .then((res) => {
          this.reviews_all = res.data
          this.reviews_all_length = this.reviews_all.length
          this.reviews = []
          this.idx = 0
          this.appendArticle()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    filterReviews(value) {
      const spanTag = document.querySelector("#selected-value > span")
      if (value == 3) {
        this.getArticleByVisit()
        spanTag.innerText = "조회수순"
      } else if (value == 2) {
        this.getArticleByLike()
        spanTag.innerText = "좋아요순"
      } else if(value == 1){
        spanTag.innerText = "최신순"
        this.getArticleByNewest()
      } else {
        spanTag.innerText = "최신순"
        this.getArticleByNewest()
      }
      const divTag = document.querySelector(".options")
      divTag.classList.toggle("noshow")
    },
    openSelectBox() {
      const divTag = document.querySelector('.options')
      divTag.classList.toggle('noshow')
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${API_URL}/community/review/list/`,
      })
        .then((res) => {
          this.reviews_all = res.data
          this.reviews_all_length = this.reviews_all.length
          this.appendArticle()
        })
        .catch((err) => {
          console.log(err)
        })
  },
  mounted() {
    window.onscroll = (() => {
    if((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
      this.appendArticle()
    }
})
  }
}
</script>

<style scoped>
.noshow {
  display: none;
}
.listBox {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.option-box {
  margin: 25px 0px 25px 0px;
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: center;
  width: 800px;
}

.write-icon {
  color: #9D0102;
}

.create-btn {
  text-decoration: none;
  color: white;
  font-size:1rem;
  padding:10px 20px 10px 20px;
  border-radius: 10px;
  background-color: #282828;
  border: solid 1px #1a1919;
  margin-right: 20px;
}

.create-btn:hover {
  border: 1px solid rgba(255, 0, 0, 0.295);
  outline: 3px solid rgba(255, 0, 0, 0.247);
}

/* #filter-select {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  width: 135.28px;
  height: 45px;
  border-radius: 10px;
  border: 0px;
  color: white;
  background-color: #282828;
  text-align: center;
  font-size: 1rem;
} */

/* #filter-select:focus {
  border: 1px solid rgba(255, 0, 0, 0.295);
  outline: 3px solid rgba(255, 0, 0, 0.247);
} */

#select-button:hover {
  border: 1px solid rgba(255, 0, 0, 0.295);
  outline: 3px solid rgba(255, 0, 0, 0.247);
  cursor: pointer;
}




#select-button {
  width: 135.28px;
  height: 45px;
  border-radius: 10px;
  border: 0px;
  color: white;
  background-color: #282828;
  text-align: center;
  font-size: 1rem;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 0px 15px 0px 15px;
}

.options {
  margin-top: 6px;
  width: 135.28px;
  background-color: #282828;
  color: white;
  border-radius: 10px;
  position: absolute;
  border: 1px solid #1b1b1ba8;
  outline: 1px solid #1b1b1b9a;
  z-index: 99;
}

.option {
  height: 45px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  transition: 0.2s ease all;
}

#select-box > div.options > div:nth-child(1) {
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

#select-box > div.options > div:nth-child(3) {
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}

.option:hover {
  cursor: pointer;
  background-color: #9D0102;
}

.append-btn {
  text-decoration: none;
  color: white;
  font-weight: 200;
  padding: 8px 5px 8px 5px;
}

.append-btn:hover {
  cursor: pointer;
  border-bottom: solid 2px #9D0102;
  /* border-top:solid 2px #9D0102; */
}

</style>