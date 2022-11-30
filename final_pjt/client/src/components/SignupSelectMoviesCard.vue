<template>
<div id="card-app" >
    
    <!-- <div class="row mx-auto my-auto justify-content-center carousel-ancester"></div> -->
    <div class="carousel-ancester">
        <div :id="`${identifier}`" class="carousel slide" data--interval="false">
            <div class="carousel-inner" role="listbox">
                
                <div class="carousel-item active" >

                    <div class="card-wrapper" v-for="idx in cardSplitter" :key="idx">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[idx-1].id}`" @mouseover="cardAnimationOn(movieList[idx-1].id)" @mouseleave="cardAnimationOff(movieList[idx-1].id)" @click="toggleSelection(movieList[idx-1].id, idx-1)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[idx-1].backdrop_path}`" class="img-fluid signup-image" :id="`image-${identifier}-${movieList[idx-1].id}`">
                                <div class="label-background"><span class="movie-title">{{ movieList[idx-1].title }}</span></div>
                            </div>
                            <!-- <MovieCardModalForm v-if="modalIndex === movieList[idx-1].id || mouseOnCard === movieList[idx-1].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[idx-1].id}`" :props-movie="movieList[idx-1]" @mouseover="modalCardAnimationOn(movieList[idx-1].id)" :identifier="identifier" /> -->
                        </div>
                    </div>
                </div>

                <div class="carousel-item"  style="justify-items: center;" v-for="page in pageSplitter" :key="page">
                    
                    <div class="card-wrapper" v-for="idx in cardSplitter" :key="idx" >
                        <div class="cards" v-if="(page * cardSplitter) + idx - 1 < movieList.length" >
                            <div class="card-img" :id="`card-${identifier}-${movieList[(page * cardSplitter) + idx - 1].id}`" @mouseover="cardAnimationOn(movieList[(page * cardSplitter) + idx - 1].id)" @mouseleave="cardAnimationOff(movieList[(page * cardSplitter) + idx - 1].id)" @click="toggleSelection(movieList[(page * cardSplitter) + idx - 1].id, (page * cardSplitter) + idx - 1)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[(page * cardSplitter) + idx - 1].backdrop_path}`" class="img-fluid image" :id="`image-${identifier}-${movieList[(page * cardSplitter) + idx - 1].id}`">
                                <div class="label-background"><span class="movie-title">{{ movieList[(page * cardSplitter) + idx - 1].title }}</span></div>
                            </div>
                            <!-- <MovieCardModalForm v-if="modalIndex === movieList[(page * cardSplitter) + idx - 1].id || mouseOnCard === movieList[(page * cardSplitter) + idx - 1].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[(page * cardSplitter) + idx - 1].id}`" :props-movie="movieList[(page * cardSplitter) + idx - 1]" @mouseover="modalCardAnimationOn(movieList[(page * cardSplitter) + idx - 1].id)" :identifier="identifier" /> -->
                        </div>
                    </div>


                </div>


            
            </div>
            <a class="carousel-control-prev bg-transparent w-aut control-button" :href="`#${identifier}`" role="button" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            </a>
            <a class="carousel-control-next bg-transparent w-aut control-button" :href="`#${identifier}`" role="button" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
            </a>
        </div>
    </div>

    
</div>
</template>

<script>



export default {
  name: 'SignupSelectMoviesCard',
  components: {
  },
  props: {
    movieList: Array,
    splitted: Array,
    identifier: String,
    cardSplitter: Number,
    selectedMovies: Array,
  },
  data() {
    return{
        cardWidth: 240,
        cardHeight: 140,
        cardExtendedWidth: 250,
        modalWidth: 290,
        modalHeight: 400,
        mouseOnCard: null,
        modalIndex: null,

        
    }
  },
  computed: {
    // idxSplitter() {
    //   return this.$store.getters.idxSplitter
    // },
    isDetailMode() {
      return this.$store.state.isDetailMode
    },
    pageSplitter() {
      if (this.movieList.length % this.cardSplitter === 0) {
        return parseInt(this.movieList.length / this.cardSplitter) - 1
      } else {
        return parseInt(this.movieList.length / this.cardSplitter)
      }
      
    }

  },
  methods: {
    getCardXY(idx) {

        const cardTag = document.querySelector(`#card-${this.identifier}-${idx}`)
        const cardX = cardTag.getBoundingClientRect().left;
        const cardY = cardTag.getBoundingClientRect().top;
        const cardXY = {cardX:cardX, cardY:cardY}
        this.$store.commit('GET_CARD_XY', cardXY)

    //   alert(this.$store.state.cardXY.cardX)
    //   alert(this.$store.state.cardXY.cardY)
      
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
        
    },
    cardAnimationOff(idx) {
        
        this.mouseOnCard = false
        const cardTag = document.getElementById(`card-${this.identifier}-${idx}`)
        cardTag.style.width = this.cardWidth + 'px'
        setTimeout(function() { cardTag.style.position = 'static' }, 150);
        
    },

    toggleSelection(movieIdx, listIdx) {
      const classify = this.selectedMovies.indexOf(this.movieList[listIdx])
      if (classify === -1) {
        const cardTag = document.getElementById(`card-${this.identifier}-${movieIdx}`)
        const imageTag = document.getElementById(`image-${this.identifier}-${movieIdx}`)
        cardTag.style.borderRadius = '10px'
        cardTag.style.boxShadow = '0px 0px 1px 4px rgba(255, 255, 255, 1)'
        imageTag.setAttribute('style', '-webkit-filter: brightness(100%);')
        this.$emit('select-movie', this.movieList[listIdx])
      } else {
        const cardTag = document.getElementById(`card-${this.identifier}-${movieIdx}`)
        const imageTag = document.getElementById(`image-${this.identifier}-${movieIdx}`)
        cardTag.style.borderRadius = '10px'
        cardTag.style.boxShadow = 'none'
        imageTag.setAttribute('style', '-webkit-filter: brightness(60%);')
        this.$emit('select-movie', this.movieList[listIdx])
      }
      

      // -webkit-filter: brightness(30%);
      
    }
    // modalCardAnimationOn(idx) {
    //     if (this.isDetailMode === false) {
    //         this.modalCardAnimationOff()
    //         this.mouseOnCard = true
    //         const modalTag = document.getElementById(`modal-card-${this.identifier}-${idx}`)
    //         modalTag.style.visibility = 'visible'
    //         modalTag.style.width = this.modalWidth + 'px'
    //         modalTag.style.height = this.modalHeight + 'px'
    //     }
        
        
    // },
    // modalCardAnimationOff() {
        
    //     const modalTag = document.querySelectorAll('.modal-card')
    //     modalTag.forEach((elem) => {
    //         elem.style.width = '100%'
    //         elem.style.height = '100%'
    //         elem.style.visibility = 'hidden'
    //     })
    // },


    // },
    // 자식 컴포넌트가 아닌 현재 컴포넌트에서 모달 폼을 썼을 때
    // modalCardAnimationOffP(idx) {

    //     this.mouseOnCard = false
    //     const modalTag = document.getElementById(`modal-card-${idx}`)
    //     modalTag.style.width = '100%'
    //     modalTag.style.height = '100%'
    //     modalTag.style.visibility = 'hidden'
    // },
    
  },
  created() {
    this.$store.commit('IS_DETAIL_MODE', false)
    const bodyTag = document.querySelector('body')
    bodyTag.style.overflowY = 'scroll'
    

    
  },



}
</script>

<style>

.carousel-ancester {
    width:100vw !important;
    
    display: flex;
    justify-content: center;
    justify-items: center;
    user-select: none;
    
  }

  .slide {
    
    width:100vw !important;
    
    display: flex;
    justify-content: center;
    justify-items: center;
    

  }
  .carousel-inner {
    overflow: visible !important;
    
    /* left: 4rem; */
  }

  .carousel-item {
    display: flex;
    justify-content: center;
    justify-items: center;
    
  }
    

  
  .card-wrapper {
    border-radius: 10px;
    height: auto;
    padding: 10px;
    /* z-index:-1; */
    /* border-radius: 10px; */
    /* display: flex; */
    
  }
  .cards {
    /* width: 14vw; */
    width: 240px;
    border-radius: 10px;
    height: 140px;
    
    
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    
    
  }
  .card-img {
    border-radius: 10px;
    justify-self:  center;
    position: absolute;
    transition-property: width;
    transition-duration: 0.15s;
    
  }
  .signup-image {
    border-radius: 10px;
    -webkit-filter: brightness(60%);

  }


  .movie-title {
    margin: 0px;
    margin-left:15px;
    margin-top:0px;
    white-space:nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }


  .label-background {
    /* margin-left: 20px; */
    width:100%;
    height: 40px;
    display: flex;
    align-items: center;
    margin-top:-40px;
    border-radius: 0px 0px 9px 9px;
    position: absolute;


    background: linear-gradient(rgba(0, 0, 0, 0.5) , rgb(0, 0, 0, 0.3));
    /* background-color: rgba(0, 0, 0, 0.500); */
    
  }

  .control-button {
    width: 5% !important;
  }

  ::-webkit-scrollbar {
    width: 3px;

}

::-webkit-scrollbar-track {
    box-shadow: inset 0 0 10px 10px rgb(0, 0, 0);
    border: solid 0px transparent;
}

::-webkit-scrollbar-thumb {
    box-shadow: inset 0 0 10px 10px rgb(255, 0, 0);
    border: solid 0px transparent;
}





  @media (max-width: 100px) {
      .carousel-inner .carousel-item > div {
          display: none;
      }
      .carousel-inner .carousel-item > div:first-child {
          display: block;
      }
  }

  .carousel-inner .carousel-item.active,
  .carousel-inner .carousel-item-next,
  .carousel-inner .carousel-item-prev {
      display: inline-flex;
  }


</style>