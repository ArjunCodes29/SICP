# Doing in scheme
# (define (cube-iter guess x)
#   (if (good-enough? guess x)
#       guess
#       (cube-iter (improve guess x)
#                   x)))
# (define (improve guess x)
#   (/ (+(/ x (* guess guess)) (* 2 guess)) 3))
# 
# (define (good-enough? guess x)
# (=(improve guess x )guess))
# (define (cbrt x)
#  (cube-iter 1.0 x))

# this is fine correct

(define (sqrt-iter guess x)
  (new-if (good-enough? guess x) guess (sqrt-iter (improve guess x) x)))
                     
          
          