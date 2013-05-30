#lang racket
(require test-engine/racket-tests)
(provide (all-defined-out))

;; pvec are of the form #(a b c) where:
;; a is the piece in UL
;; b is the piece in UR
;; c is the piece in DR
;; 0 = UL, 1 = UR, 2 = DR
;; for a 2x2x1 where DL is fixed.
(define U #(1 0 2))
(define R #(0 2 1))

;; apply-move: nat pvec pvec -> vec
;; Applies pvec1 to pvec2 on a puzzle with n pieces.
(define (apply-move n pvec1 pvec2)
  (build-vector n (lambda (x) (vector-ref pvec2 (vector-ref pvec1 x)))))
;; Tests:
(check-expect (apply-move 3 U #(2 1 0)) #(1 2 0))
(check-expect (apply-move 3 R #(2 1 0)) #(2 0 1))
(check-expect (apply-move 3 R #(0 1 2)) #(0 2 1))
(test)