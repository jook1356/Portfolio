<template>
  <div class="cards" >
    <div class="card-img" style="border-radius: 10px;; box-shadow: 0px 0px 5px 1px rgba(0, 0, 0, 0.300);" :id="`card-${identifier}-${movie.id}`" @mouseover="cardAnimationOn(movie.id)" @mouseleave="cardAnimationOff(movie.id)">
      <img :src="`https://image.tmdb.org/t/p/w500/${movie.backdrop_path}`" class="img-fluid image">
      <div class="label-background"><p class="movie-title">{{ movie.title }}</p></div>
    </div>
    <MovieCardModalForm style="width:100%; height:100%;" v-if="modalIndex === movie.id || mouseOnCard === movie.id" class="modal-card" :id="`modal-card-${identifier}-${movie.id}`" :props-movie="movie" @mouseover="modalCardAnimationOn(movie.id)" :identifier="identifier" />
    <!-- <MovieCardDetail :props-movie="movie" :identifier="identifier" ref="apiRequest" style="z-index:99999; visibility: hidden;" /> -->
    
  </div>
</template>

<script>
import MovieCardModalForm from '@/components/MovieCardModalForm'
// import MovieCardDetail from '@/components/MovieCardDetail'
export default {
  name: 'MovieSearchCard',
  components: {
    MovieCardModalForm,
    // MovieCardDetail
  },
  props: {
    movie: Object,
    identifier: String
  },
  computed: {
    isDetailMode() {
      return this.$store.state.isDetailMode
    },
  },
  data() {
    return {
      cardWidth: 240,
      cardHeight: 140,
      cardExtendedWidth: 250,
      modalWidth: 290,
      modalHeight: 400,
      mouseOnCard: null,
      modalIndex: null,
    }
  },
  methods: {
    getCardXY(idx) {

    const cardTag = document.querySelector(`#card-${this.identifier}-${idx}`)
    //const fixedForm = document.querySelector('.search-inner-form')
    const cardX = cardTag.getBoundingClientRect().left //- fixedForm.getBoundingClientRect().left;
    const cardY = cardTag.getBoundingClientRect().top //- fixedForm.getBoundingClientRect().top;
    const cardXY = {cardX:cardX, cardY:cardY}
    this.$store.commit('GET_CARD_XY', cardXY)

    //   alert(this.$store.state.cardXY.cardX)
    //   alert(this.$store.state.cardXY.cardY)

    },
    searchMovieDetail(idx) {
      if (this.$store.state.isDetailMode === false) {
        this.$store.commit('IS_DETAIL_MODE', true)
        this.getCardXY(idx)
        this.mouseOnCard = false
        this.$refs.apiRequest.showDetail();
      }
      
      
      // const movieSearchForm = document.querySelector('.search-wrapper')


      // const modalTag = document.getElementById(`modal-card-${this.identifier}-${idx}`)
      // modalTag.setAttribute('style', '0px 0px 0px 0px rgba(0, 0, 0, 0)')
      // this.getCardXY(idx)
      // // const backgroundTag = document.getElementById(`background-${this.identifier}-${idx}`)
      // // backgroundTag.style.opacity = 0
      // this.$store.commit('IS_DETAIL_MODE', true)
      // this.mouseOnCard = false
      // this.$refs.apiRequest.showDetail();

    },
    cardAnimationOn(idx) {
    if (this.isDetailMode === false) {
        const modalTags = document.querySelectorAll('.modal-card')
        modalTags.forEach((elem) => {
            if (elem.id !== `modal-card-${this.identifier}-${idx}`) {
                elem.style.width = '100%'
                elem.style.height = '100%'
                elem.style.visibility = 'hidden'
            }
        })

    } 

    this.mouseOnCard = idx
    const cardTag = document.getElementById(`card-${this.identifier}-${idx}`)
    cardTag.style.position = 'absolute'
    cardTag.style.width = this.cardExtendedWidth + 'px'

    if (this.isDetailMode === false) {
        
        setTimeout(() => {
            if ( this.mouseOnCard === idx ) {
                this.modalIndex = idx
                
                const modalTag = document.getElementById(`modal-card-${this.identifier}-${idx}`)
                console.log(modalTag)
                console.log('fweafwafewfefawfefwa')
                const backgroundTag = document.getElementById(`background-${this.identifier}-${idx}`)
                console.log(backgroundTag)
                console.log('fweafwafewfefawfefwa')
                backgroundTag.style.opacity = 255
                modalTag.style.width = this.cardWidth + 'px'
                modalTag.style.height = this.cardheight + 'px'

                modalTag.style.visibility = 'visible'
                modalTag.style.width = this.modalWidth + 'px'
                modalTag.style.height = this.modalHeight + 'px'
            } 
        }, 300);
    }
    },
    cardAnimationOff(idx) {

    this.mouseOnCard = false
    const cardTag = document.getElementById(`card-${this.identifier}-${idx}`)
    cardTag.style.width = this.cardWidth + 'px'
    setTimeout(function() { cardTag.style.position = 'static' }, 150);

    },
  }

}
</script>

<style>

</style>