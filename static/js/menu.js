
  // const nav = document.querySelector('.nav');
  // document.querySelector('.toggle').onclick = function(){
  //   this.classList.toggle('active');
  //   nav.classList.toggle('active');
  // }


  const cartButtons = document.querySelectorAll('.add-cart')
  cartButtons.forEach(button => button.addEventListener('click', function (event) {
    event.target.classList.toggle('added')
    if (event.target.classList.contains('added')){
      event.target.innerText = 'Добавлено'
    }
    else {
      event.target.innerText = 'В корзину'
    }
  }))

