#lang racket

#|
(define (apply fn list1)
    (
|#

(define (foo1)
  (values 1 2 3))
 
(let-values (((a b c) (foo1)))
  (display (list a b c))
  (newline))

(define (f . x)
  (first x))

(and 4 "string")