function availableMoves(position) {
  if (typeof(position) !== "string" || position.length !== 2) {
    return [];
  }
  var x = position[0];
  var y = position[1];
  if (x < 'A' || x > 'H' || y < 1 || y > 8) {
    return [];
  }
  var ret = [];
  var letterDelta = 'A'.charCodeAt(0) - 1;
  //var diff = (x.charCodeAt(0) - letterDelta) - (y-0);
  for (var i = 1; i <= 8; i++) {
    // same column:
    if (i != y) {
      ret.push(x + i.toString());
    }
    // same row:
    if (i != x.charCodeAt(0) - letterDelta) {
      ret.push(String.fromCharCode(letterDelta + i) + y);
    }
  }
  for (var d = -7; d <= 7; d++) {
    var l = String.fromCharCode(x.charCodeAt(0) + d);
    if (d != 0 && l >= 'A' && l <= 'H') {
      // upper left to bottom right diagonal:
      if ((y-0) + d > 0 && (y-0) + d <= 8) {
        ret.push(l + ((y-0) + d));
      }
      // bottom left to upper right diagonal:
      if ((y-0) > d && (y-0) <= d + 8) {
        ret.push(String.fromCharCode(x.charCodeAt(0) + d) + ((y-0) - d));
      }
    }
  }
  ret.sort(); // alphabetic
  return ret;
}
