<template>
  <div class="adapter-wrapper" :id="`adapter-wrapper-${identifier}-${movie.id}`" @click="showDetail" style="position:absolute; top:0%; width:100%; height:100%; z-index: 99999;">
    <MovieCardDetail :props-movie="movie" :identifier="identifier" ref="apiRequest" style="z-index:99999; visibility: hidden;" />


    
    
  </div>
</template>

<script>
import MovieCardDetail from '@/components/MovieCardDetail'

export default {

  name: 'CommunityMovieDetailAdapter',
  components: {
    MovieCardDetail,
  },
  props: {
    movie: Object,
    identifier: String,
  },
  data() {
    return {
      mouseOnCard: null,
    }
  },
  methods: {
    getCardXY() {

    const cardTag = document.querySelector(`#adapter-wrapper-${this.identifier}-${this.movie.id}`)
    const cardX = cardTag.getBoundingClientRect().left;
    const cardY = cardTag.getBoundingClientRect().top;
    const cardXY = {cardX:cardX, cardY:cardY}
    this.$store.commit('GET_CARD_XY', cardXY)

    //   alert(this.$store.state.cardXY.cardX)
    //   alert(this.$store.state.cardXY.cardY)

    },
    showDetail() {
      if (this.$store.state.isDetailMode === false) {
        this.$store.commit('IS_DETAIL_MODE', true)
        this.mouseOnCard = false
        this.getCardXY()
        this.$refs.apiRequest.showDetail();
      }
      
    }
  }
}
</script>

<style>

</style>