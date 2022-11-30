<template>
<div id="card-app" >
    
    <!-- <div class="row mx-auto my-auto justify-content-center carousel-ancester"></div> -->
    <div class="carousel-ancester">
        <div :id="`${identifier}`" class="carousel slide" data--interval="false">
            <div class="carousel-inner" role="listbox">
                
                <div class="carousel-item active">
                    <div class="card-wrapper">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[0].id}`" @mouseover="cardAnimationOn(movieList[0].id)" @mouseleave="cardAnimationOff(movieList[0].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[0].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[0].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[0].id || mouseOnCard === movieList[0].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[0].id}`" :props-movie="movieList[0]" @mouseover="modalCardAnimationOn(movieList[0].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <div class="card-wrapper">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[1].id}`" @mouseover="cardAnimationOn(movieList[1].id)" @mouseleave="cardAnimationOff(movieList[1].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[1].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[1].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[1].id || mouseOnCard === movieList[1].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[1].id}`" :props-movie="movieList[1]" @mouseover="modalCardAnimationOn(movieList[1].id)" :identifier="identifier"/>
                        </div>
                    </div>
                    
                    <div class="card-wrapper">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[2].id}`" @mouseover="cardAnimationOn(movieList[2].id)" @mouseleave="cardAnimationOff(movieList[2].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[2].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[2].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[2].id || mouseOnCard === movieList[2].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[2].id}`" :props-movie="movieList[2]" @mouseover="modalCardAnimationOn(movieList[2].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <div class="card-wrapper">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[3].id}`" @mouseover="cardAnimationOn(movieList[3].id)" @mouseleave="cardAnimationOff(movieList[3].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[3].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[3].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[3].id || mouseOnCard === movieList[3].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[3].id}`" :props-movie="movieList[3]" @mouseover="modalCardAnimationOn(movieList[3].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <div class="card-wrapper">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[4].id}`" @mouseover="cardAnimationOn(movieList[4].id)" @mouseleave="cardAnimationOff(movieList[4].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[4].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[4].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[4].id || mouseOnCard === movieList[4].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[4].id}`" :props-movie="movieList[4]" @mouseover="modalCardAnimationOn(movieList[4].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <div class="card-wrapper">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[5].id}`" @mouseover="cardAnimationOn(movieList[5].id)" @mouseleave="cardAnimationOff(movieList[5].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[5].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[5].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[5].id || mouseOnCard === movieList[5].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[5].id}`" :props-movie="movieList[5]" @mouseover="modalCardAnimationOn(movieList[5].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <div class="card-wrapper">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[6].id}`" @mouseover="cardAnimationOn(movieList[6].id)" @mouseleave="cardAnimationOff(movieList[6].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[6].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[6].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[6].id || mouseOnCard === movieList[6].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[6].id}`" :props-movie="movieList[6]" @mouseover="modalCardAnimationOn(movieList[6].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <!-- <div class="card-wrapper">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[7].id}`" @mouseover="cardAnimationOn(movieList[7].id)" @mouseleave="cardAnimationOff(movieList[7].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[7].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[7].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[7].id || mouseOnCard === movieList[7].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[7].id}`" :props-movie="movieList[7]" @mouseover="modalCardAnimationOn(movieList[7].id)" :identifier="identifier" />
                        </div>
                    </div> -->
                    <!-- <div class="card-wrapper">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[8].id}`" @mouseover="cardAnimationOn(movieList[8].id)" @mouseleave="cardAnimationOff(movieList[8].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[8].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[8].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[8].id || mouseOnCard === movieList[8].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[8].id}`" :props-movie="movieList[8]" @mouseover="modalCardAnimationOn(movieList[8].id)" :identifier="identifier" />
                        </div>
                    </div> -->

                </div>

                <div class="carousel-item" v-for="(idx, idxindex) in splitted[7]" :key="idxindex" style="justify-items: center;">
                    <div class="card-wrapper" v-if="idx[0]">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[idx[0]].id}`" @mouseover="cardAnimationOn(movieList[idx[0]].id)" @mouseleave="cardAnimationOff(movieList[idx[0]].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[idx[0]].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[idx[0]].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[idx[0]].id || mouseOnCard === movieList[idx[0]].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[idx[0]].id}`" :props-movie="movieList[idx[0]]" @mouseover="modalCardAnimationOn(movieList[idx[0]].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <div class="card-wrapper" v-if="idx[1]">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[idx[1]].id}`" @mouseover="cardAnimationOn(movieList[idx[1]].id)" @mouseleave="cardAnimationOff(movieList[idx[1]].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[idx[1]].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[idx[1]].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[idx[1]].id || mouseOnCard === movieList[idx[1]].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[idx[1]].id}`" :props-movie="movieList[idx[1]]" @mouseover="modalCardAnimationOn(movieList[idx[1]].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <div class="card-wrapper" v-if="idx[2]">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[idx[2]].id}`" @mouseover="cardAnimationOn(movieList[idx[2]].id)" @mouseleave="cardAnimationOff(movieList[idx[2]].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[idx[2]].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[idx[2]].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[idx[2]].id || mouseOnCard === movieList[idx[2]].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[idx[2]].id}`" :props-movie="movieList[idx[2]]" @mouseover="modalCardAnimationOn(movieList[idx[2]].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <div class="card-wrapper" v-if="idx[3]">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[idx[3]].id}`" @mouseover="cardAnimationOn(movieList[idx[3]].id)" @mouseleave="cardAnimationOff(movieList[idx[3]].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[idx[3]].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[idx[3]].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[idx[3]].id || mouseOnCard === movieList[idx[3]].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[idx[3]].id}`" :props-movie="movieList[idx[3]]" @mouseover="modalCardAnimationOn(movieList[idx[3]].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <div class="card-wrapper" v-if="idx[4]">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[idx[4]].id}`" @mouseover="cardAnimationOn(movieList[idx[4]].id)" @mouseleave="cardAnimationOff(movieList[idx[4]].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[idx[4]].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[idx[4]].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[idx[4]].id || mouseOnCard === movieList[idx[4]].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[idx[4]].id}`" :props-movie="movieList[idx[4]]" @mouseover="modalCardAnimationOn(movieList[idx[4]].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <div class="card-wrapper" v-if="idx[5]">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[idx[5]].id}`" @mouseover="cardAnimationOn(movieList[idx[5]].id)" @mouseleave="cardAnimationOff(movieList[idx[5]].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[idx[5]].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[idx[5]].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[idx[5]].id || mouseOnCard === movieList[idx[5]].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[idx[5]].id}`" :props-movie="movieList[idx[5]]" @mouseover="modalCardAnimationOn(movieList[idx[5]].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <div class="card-wrapper" v-if="idx[6]">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[idx[6]].id}`" @mouseover="cardAnimationOn(movieList[idx[6]].id)" @mouseleave="cardAnimationOff(movieList[idx[6]].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[idx[6]].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[idx[6]].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[idx[6]].id || mouseOnCard === movieList[idx[6]].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[idx[6]].id}`" :props-movie="movieList[idx[6]]" @mouseover="modalCardAnimationOn(movieList[idx[6]].id)" :identifier="identifier" />
                        </div>
                    </div>
                    <!-- <div class="card-wrapper" v-if="idx[7]">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[idx[7]].id}`" @mouseover="cardAnimationOn(movieList[idx[7]].id)" @mouseleave="cardAnimationOff(movieList[idx[7]].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[idx[7]].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[idx[7]].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[idx[7]].id || mouseOnCard === movieList[idx[7]].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[idx[7]].id}`" :props-movie="movieList[idx[7]]" @mouseover="modalCardAnimationOn(movieList[idx[7]].id)" :identifier="identifier" />
                        </div>
                    </div> -->
                    <!-- <div class="card-wrapper" v-if="idx[8]">
                        <div class="cards">
                            <div class="card-img" :id="`card-${identifier}-${movieList[idx[8]].id}`" @mouseover="cardAnimationOn(movieList[idx[8]].id)" @mouseleave="cardAnimationOff(movieList[idx[8]].id)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${movieList[idx[8]].backdrop_path}`" class="img-fluid image">
                                <div class="label-background"><p class="movie-title">{{ movieList[idx[8]].title }}</p></div>
                            </div>
                            <MovieCardModalForm v-if="modalIndex === movieList[idx[8]].id || mouseOnCard === movieList[idx[8]].id" class="modal-card" :id="`modal-card-${identifier}-${movieList[idx[8]].id}`" :props-movie="movieList[idx[8]]" @mouseover="modalCardAnimationOn(movieList[idx[8]].id)" :identifier="identifier" />
                        </div>
                    </div> -->

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
import MovieCardModalForm from '@/components/MovieCardModalForm'


export default {
  name: 'MovieCard7',
  components: {
    MovieCardModalForm
  },
  props: {
    movieList: Array,
    splitted: Array,
    identifier: String,
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
    idxSplitter() {
      return this.$store.getters.idxSplitter
    },
    isDetailMode() {
      return this.$store.state.isDetailMode
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
        
        if (this.isDetailMode === false) {
            
            setTimeout(() => {
                if ( this.mouseOnCard === idx ) {
                    this.modalIndex = idx
                    const modalTag = document.getElementById(`modal-card-${this.identifier}-${idx}`)
                    console.log(modalTag)
                    const backgroundTag = document.getElementById(`background-${this.identifier}-${idx}`)
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
  }


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
    /* box-shadow: 0px 0px 5px 1px rgba(0, 0, 0, 0.700); */
    
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    
    
  }
  .card-img {
    
    justify-self:  center;
    position: absolute;
    transition-property: width;
    transition-duration: 0.15s;
    
  }
  .image {
    border-radius: 10px;
  }




  .movie-title {
    margin-top:10px;
    margin-left:15px;
    white-space:nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .label-background {
    /* margin-left: 20px; */
    width:100%;
    margin-top:-45px;
    border-radius: 0px 0px 15px 15px;
    position: absolute;

    
    background-color: rgba(0, 0, 0, 0.500);
    
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