#lang racket

;; Forte-expect:
(define (expect teststring testresult expected)
    (if (= testresult expected)
        (printf "PASSED\n")
        (printf "FAILED: ~a returned ~a instead of ~a\n"
              teststring
              testresult
              expected)))

;; General y-combinator:
(define Y
  (lambda (f)
    ((lambda (x) (f (lambda (v) ((x x) v))))
     (lambda (x) (f (lambda (v) ((x x) v)))))))

;; Factorial:
(define fact
  (Y (lambda (f)
       (lambda (n)
         (if (= n 0)
             1
             (* n (f (- n 1))))))))

(expect "(fact 4)" (fact 4) 24)

;; sum-list adds up all elements of a list.
(define sum-list
  (Y (lambda (f)
       (lambda (lst)
         (if (empty? lst)
             0
             (+ (first lst) (f (rest lst))))))))

(expect "(sum-list '(1 2 3 4))" (sum-list '(1 2 3 4)) 10)

;; my-foldr:
(define my-foldr
  (Y (lambda (f)
       (lambda (combine base lst)
         (if (empty? lst)
             base
             (combine (first lst) (f combine base (rest lst))))))))

(expect "(my-foldr cons '(4 5 6) '(1 2 3))"
        (my-foldr cons '(4 5 6) '(1 2 3))
        '(1 2 3 4 5 6))
