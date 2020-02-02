## 참고 링크 (https://www.youtube.com/watch?v=Qu3dThVy6KQ)

import itertools

squares = map(pow, range(10), itertools.repeat(3))
print(list(squares))

s2 = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2), (3, 4)])
print(list(s2))