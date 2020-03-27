<template>
  <!-- Just a cool way to show our news -->
  <div>
    <div id="news-bar">
      <marquee direction="right" scrollamount="5" loop="infinite" onmouseover="this.stop()" onmouseout="this.start()">
        <a v-for="item of news" :key="item" href="#" class="hvr-pop" v-html="item"></a>
      </marquee>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    news: {
      type: Array,
      required: true
    }
  }
};
</script>

<style>

#news-bar {
  font-family: "Cairo", sans-serif;
  position: fixed;
  bottom: 0;
  width: 100%;
  background: #ffc023;
  padding-left: 20px;
  padding-right: 20px;
  z-index: 99999999;
}

#news-bar:hover {
  transition: 0.37s;
}

#news-bar a {
  padding: 8px;
  color: black;
  text-decoration: none;
}

#news-bar a:hover {
  transition: 0.37s;
  color: rgb(59, 59, 59);
}

.arrow-up {
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid rgb(185, 50, 50);
display: inline-block;
}

/* Pop */

@-webkit-keyframes hvr-pop {
  50% {
    -webkit-transform: scale(1.2);
    transform: scale(1.2);
  }
}

@keyframes hvr-pop {
  50% {
    -webkit-transform: scale(1.2);
    transform: scale(1.2);
  }
}

.hvr-pop {
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: translateZ(0);
  transform: translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -moz-osx-font-smoothing: grayscale;
}

.hvr-pop:hover,
.hvr-pop:focus,
.hvr-pop:active {
  -webkit-animation-name: hvr-pop;
  animation-name: hvr-pop;
  -webkit-animation-duration: 0.3s;
  animation-duration: 0.3s;
  -webkit-animation-timing-function: linear;
  animation-timing-function: linear;
  -webkit-animation-iteration-count: 1;
  animation-iteration-count: 1;
}

</style>
