<template>
  <div>
    <!-- <div style="display:flex; padding-top: 14px; padding:18px; margin-bottom:18px; width:100%; height: 40px;">
      
    </div> -->
    <div style="display:flex; padding-left:18px; padding-top:15px; width:100%; height: 48px;">
      <h3>댓글 리뷰</h3>
      <span style="margin-left:10px; margin-top:12px; color:rgb(150,150,150); font-size: 14px; ">댓글은 여러번 작성할 수 있으며 평점은 한번만 반영됩니다.</span>
    </div>

    <div style="display:flex; margin-top:14px; padding:18px; width:100%; height: 48px;">
      
      <star-rating :star-size="18" v-model="myVote" :rating="propsMovie.vote_average" :increment="0.5" :show-rating="false" :animate="true" :active-color="['#520000','#520000']" :active-border-color="['#F6546A','#948989']" :border-width="4" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]" :active-on-click="true" :clearable="true"></star-rating>
      <span style="margin-left:10px; margin-top:-4px; color:rgb(150,150,150); font-size: 14px; ">별점을 선택해 주세요.</span>
    </div>
    
    
    <div style="display:flex; margin-bottom:16px;">
      <input class="comment-input" placeholder="댓글을 입력하세요." type="text" v-model="commentInput">
      <div class="comment-submit" @click="createComment">등록</div>

    </div>
    <hr>
    <div>
      <ul v-for="(comment, idx) in comments" :key="idx">
        <MovieCardDetailCommentsComment :comment="comment" :idx="idx" @idx="deleteComment" />
      </ul>
    </div>
    
    <div v-if="comments.length === 0">
      
      <div style="width:100%; height: 100px; display: flex; justify-content: center; align-items: center;">
        <span style="color:rgb(150,150,150);">가장 먼저 댓글을 남겨보세요!</span>
      </div>
      <hr>
    </div>
    
    
    
    
  </div>
</template>

<script>

import axios from 'axios'
import StarRating from 'vue-star-rating'
import MovieCardDetailCommentsComment from '@/components/MovieCardDetailCommentsComment'

export default {
  name: 'MovieCardDetailComments',
  components: {
    MovieCardDetailCommentsComment,
    StarRating,
  },
  props: {
    propsMovie: Object,
  },
  data() {
    return {
      comments: [],
      myVote: null,
      commentInput : null
    }
  },
  methods: {
    createComment() {
      const API_URL = "http://127.0.0.1:8000"
      const movie = this.propsMovie.id
      const content = this.commentInput
      const vote = this.myVote
      axios({
        method: 'post',
        url: `${API_URL}/movies/create_comment/`,
        data: {
          movie,
          content,
          vote,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(response => {
          this.comments = response.data
          this.commentInput = null
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteComment(childData) {
      this.comments.splice(childData, 1)
    }
  },
  created() {
    const API_URL = "http://127.0.0.1:8000"

    axios({
      method: 'GET',
      url: `${API_URL}/movies/comment_list/${this.propsMovie.id}/`,
    })
      .then(response => {
        this.comments = response.data

      })
      .catch(error => {
        console.log(error)
      })
  }

}
</script>

<style>
.comment-input {
  width:100%;
  height:64px;
  padding-left:18px;
  background-color: rgb(40, 40, 40);
  border: 0px black none;
  outline: none;
  color:white;
}
.comment-input:focus {
  border: 0px;
}

.comment-submit {
  background-color: rgb(40, 40, 40);
  display: flex;
  justify-content: center;
  align-items: center;
  width: 96px;
  cursor: pointer;
  transition-property: background-color;
  transition-duration: 0.5s;
}
.comment-submit:hover {
  background-color: rgb(50, 50, 50);
}
</style>