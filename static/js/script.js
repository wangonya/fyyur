window.parseISOString = function parseISOString(s) {
  var b = s.split(/\D+/);
  return new Date(Date.UTC(b[0], --b[1], b[2], b[3], b[4], b[5], b[6]));
};

getSelected = value => {
  const selected = []
  for (let i = 0; i < value.length; i++) {
    if (value.options[i].selected) selected.push(value.options[i].value);
  }
  console.log('selected ==>', selected)
  return selected
}