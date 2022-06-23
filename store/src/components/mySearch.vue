<template>
  <div id="main">
    <div id="content">
      <ul class="logo">
        <li>
          <span>优购</span>
          <span>yougou</span>
        </li>
        <li><i class="iconfont icon">&#xeba1;</i>100% 正品</li>
        <li><i class="iconfont icon">&#xe673;</i>免邮</li>
        <li><i class="iconfont icon">&#xe71f;</i>退换无忧</li>
      </ul>

      <div class="search">
        <div>
          <span
            class="iconfont"
            style="font-size: 25px; color: #dbdada; font-weight: bold"
            >&#xe64e;</span
          >
          <input
            type="text"
            name="search"
            placeholder="搜索商品"
            autocomplete="off"
            v-model="value"
          />
          <label for="search">
            <img src="@/assets/camera.png" alt="" />
          </label>
          <input
            type="file"
            @change="SearchMap"
            style="display: none"
            id="search"
            accept="image/*"
            ref="search"
          />
          <button @click="LookUp">搜索</button>
        </div>
        <ul>
          <li>潮洪激</li>
          <li>伏肤套装</li>
          <li>女式T袖</li>
          <li>耐克Nike</li>
        </ul>
      </div>

      <div id="shop-cart" @click="showCart">
        <span class="iconfont one">&#xe899;</span>
        <span class="two">我的购物车</span>
        <i class="number">{{ num }}</i>
      </div>
    </div>
    <img :src="test" alt="" style="width: 150px;height: 150px;" v-if="test"/>
  </div>
</template>

<script>
import emitter from '@/utils/event'
export default {
  name: 'mySearch',
  data () {
    return {
      value: '',
      num: 0,
      test: '',
      shop_info: ''
    }
  },
  methods: {
    async LookUp () {
      const { data: res } = await this.$http.post('search/lookup/', { image: this.test })
      if (res.code === 200) {
        emitter.emit('shop', { aim: res.data })
      }
    },
    SearchMap () {
      const file = document.querySelector('input[type=file]').files[0] // 上传的文件对象
      const reader = new FileReader()
      reader.readAsDataURL(file)
      reader.addEventListener('load', (e) => {
        const image = new Image() // //新建一个img标签（还没嵌入DOM节点)
        image.src = e.target.result
        image.addEventListener('load', () => {
          const canvas = document.createElement('canvas')
          const context = canvas.getContext('2d')
          const imageWidth = 224 // 压缩后图片的大小
          const imageHeight = 224
          let data = ''
          canvas.width = imageWidth
          canvas.height = imageHeight
          context.drawImage(image, 0, 0, imageWidth, imageHeight)
          data = canvas.toDataURL('image/jpeg')
          // 压缩完成
          this.test = data
        })
      })
    }
  }
}
</script>

<style scoped lang="less">
#main {
  width: 100%;
  height: 270px;
  #content {
    max-width: 1000px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    height: 100px;
    align-items: center;
    .logo {
      display: flex;
      align-items: center;
      li:first-child {
        display: flex;
        flex-direction: column;
        height: 70px;
        justify-content: space-between;
        align-items: center;
        span:first-child {
          font-size: 42px;
        }
        span {
          font-size: 12px;
          height: 20px;
        }
      }
      li {
        font-size: 14px;
        display: flex;
        align-items: center;
        margin-right: 20px;
        .icon {
          font-size: 20px;
        }
      }
    }
    .search {
      div {
        display: flex;
        justify-content: center;
        input {
          width: 270px;
          height: 38px;
          border: 1px solid #ff3701;
          border-left: 0;
          border-right: 0;
          outline: none;
          font-style: normal;
          font-weight: normal;
          font-stretch: normal;
          font-size: 14px;
          line-height: 38px;
          background-color: #fff;
        }
        img {
          height: 38px;
          border: 1px solid #ff3701;
          border-left: 0;
          border-right: 0;
          cursor: pointer;
        }
        span {
          border: 1px solid #ff3701;
          border-right: 0;
          height: 38px;
          width: 45px;
          text-align: center;
          line-height: 38px;
          border-bottom-left-radius: 3px;
          border-top-left-radius: 3px;
        }
        button {
          border: 0;
          width: 100px;
          height: 40px;
          background: linear-gradient(to right, #ff3701, #ff0b01);
          color: white;
          border-bottom-right-radius: 3px;
          border-top-right-radius: 3px;
        }
      }
      ul {
        display: flex;
        font-size: 12px;
        color: #999;
        padding: 0;
        margin: 5px 0 0 0;
        li {
          position: relative;
          padding: 0 7px;
          cursor: pointer;
          &:hover {
            color: #409eff;
          }
          &:after {
            content: '|';
            position: absolute;
            right: 0;
          }
        }
      }
    }
    #shop-cart {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 105px;
      height: 34px;
      padding: 0 5px;
      border: 1px solid #c3c3c3;
      border-radius: 3px;
      position: relative;
      overflow: hidden;
      cursor: pointer;
      margin-bottom: 15px;
      &:hover {
        background-color: #fff;
      }
      .one {
        font-size: 21px;
      }
      .two {
        font-size: 12px;
      }
      i {
        position: absolute;
        font-style: normal;
        top: 2px;
        left: 16px;
        display: block;
        width: 18px;
        height: 14px;
        border-radius: 7px;
        font-size: 5px;
        text-align: center;
        line-height: 14px;
        background-color: red;
        color: #fff;
      }
    }
  }
}
</style>
