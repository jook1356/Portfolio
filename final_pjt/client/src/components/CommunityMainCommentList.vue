<template>
  <div> 
    <CommunityMainCommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
      @click.native="goDetail(comment.review.id)"
    />
  </div>
</template>

<script>
import CommunityMainCommentListItem from '@/components/CommunityMainCommentListItem'

export default {
  name: "CommunityMainCommentList",
  components: {
    CommunityMainCommentListItem,
  },
  data() {
    return {
    }
  },
  props: {
    comments: Array,
  },
  methods: {
    goDetail(review_id) {
      this.$router.push({name: 'detail', params: {id: review_id }})
    }
  },
}
</script>

<style scoped>


</style>