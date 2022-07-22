// https://franklinta.com/2014/09/08/computing-css-matrix3d-transforms/

const getTransform = function(from, to) {
  console.assert(from.length == 4, 'from is not four points')
  console.assert(to.length == 4, 'to is not four points')

  var A, H, b, h, i, k, k_i, l, lhs, m, ref, rhs;
  A = []; // 8x8
  for (i = k = 0; k < 4; i = ++k) {
    A.push([from[i][0], from[i][1], 1, 0, 0, 0, -from[i][0] * to[i][0], -from[i][1] * to[i][0]]);
    A.push([0, 0, 0, from[i][0], from[i][1], 1, -from[i][0] * to[i][1], -from[i][1] * to[i][1]]);
  }
  b = []; // 8x1
  for (i = l = 0; l < 4; i = ++l) {
    b.push(to[i][0]);
    b.push(to[i][1]);
  }
  // Solve A * h = b for h
  h = numeric.solve(A, b);
  H = [[h[0], h[1], 0, h[2]], [h[3], h[4], 0, h[5]], [0, 0, 1, 0], [h[6], h[7], 0, 1]];
  // Sanity check that H actually maps `from` to `to`
  for (i = m = 0; m < 4; i = ++m) {
    lhs = numeric.dot(H, [from[i][0], from[i][1], 0, 1]);
    k_i = lhs[3];
    rhs = numeric.dot(k_i, [to[i][0], to[i][1], 0, 1]);
    console.assert(numeric.norm2(numeric.sub(lhs, rhs)) < 1e-9, "Not equal:", lhs, rhs);
  }
  return H;
};

const matrixToString = function(M) {
  const results = [];
  for(const row of M) {
    for(const x of row) {
      results.push(x.toFixed(20));
    }
  }
  return results.join(',');
}

export {matrixToString, getTransform}
