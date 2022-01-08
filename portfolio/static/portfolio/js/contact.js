document.getElementById('contact-form').addEventListener('submit',()=>{
    let timerInterval
Swal.fire({
  title: 'Your Email will be sent in moments',
  html: '<b></b>',
  timer: 1000,
  timerProgressBar: true,
  didOpen: () => {
    Swal.showLoading()
    const b = Swal.getHtmlContainer().querySelector('b')
    timerInterval = setInterval(() => {
      b.textContent = ''
    }, 100)
  },
  willClose: () => {
    clearInterval(timerInterval)
  }
})
})