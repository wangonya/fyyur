deleteVenue = id => {
  return fetch(`/venues/${id}`, {
    method: 'DELETE'
  }).then(() => window.location = '/venues')
      .catch(e => console.log('error deleting', e))
}