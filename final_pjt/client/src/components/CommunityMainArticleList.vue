<template>
  <div> 
    <CommunityMainArticleListItem
      v-for="review in reviews"
      :key="review.id"
      :review="review"
      @click.native="goDetail(review)"
    />
  </div>
</template>

<script>
import CommunityMainArticleListItem from '@/components/CommunityMainArticleListItem'

export default {
  name: "CommunityMainArticleList",
  components: {
    CommunityMainArticleListItem,
  },
  data() {
    return {
    }
  },
  props: {
    reviews: Array,
  },
  methods: {
    goDetail(review) {
      this.$router.push({name: 'detail', params: {id: review.id }})
    }
  },
}
</script>

<style scoped>


</style>