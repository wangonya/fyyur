document.getElementById('venue_form').onsubmit = e => {
  e.preventDefault()
  fetch('/venues/create', {
    method: 'POST',
    body: JSON.stringify({
      'name': document.getElementById('name').value,
      'city': document.getElementById('city').value,
      'state': document.getElementById('state').value,
      'address': document.getElementById('address').value,
      'phone': document.getElementById('phone').value,
      'image_link': document.getElementById('image_link').value,
      'facebook_link': document.getElementById('facebook_link').value,
      'genres': getSelected(document.getElementById('genres')),
      'website': document.getElementById('website').value,
      'seeking_talent': document.getElementById('seeking_talent').checked,
      'seeking_description': document.getElementById('seeking_description').value,
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  })
}