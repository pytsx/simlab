`pkg` nunca importa `src`

api → src     ✅
api → pkg     ✅
src → pkg     ✅
pkg → src     ❌
pkg → api     ❌
src → api     ❌