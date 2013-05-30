#lang racket
(require test-engine/racket-tests)
(provide (all-defined-out))

;; perm->index: nat perm -> index
;; Changes a permutation vector into an index.
(define (perm->index n perm1)
  (local
    [(define t 0)
     (define n (vector-length perm1))]
    (begin
      (for ([i (- n 1)])
        (set! t (* t (- n i)))
        (for ([j (in-range (+ i 1) n)])
          (cond [(> (vector-ref perm1 i) (vector-ref perm1 j))
                 (set! t (+ t 1))])))
      t)))
;; Tests:
(check-expect (perm->index 3 #(0 1 2)) 0)
(check-expect (perm->index 3 #(0 2 1)) 1)
(check-expect (perm->index 3 #(1 0 2)) 2)
(check-expect (perm->index 3 #(1 2 0)) 3)
(check-expect (perm->index 3 #(2 0 1)) 4)
(check-expect (perm->index 3 #(2 1 0)) 5)

;; index->perm: nat index -> perm
;; Changes an index into a permutation vector of n pieces.
(define (index->perm n ind1)
  (local
    [(define perm1 (make-vector n))
     (define t ind1)]
    (begin
      (for ([i (- n 1)])
        (vector-set! perm1 (- (- n 2) i) (modulo t (+ i 2)))
        (set! t (quotient t (+ i 2)))
        (for ([j (in-range (- (- n 1) i) n)])
          (cond [(>= (vector-ref perm1 j) (vector-ref perm1 (- (- n 2) i)))
                 (vector-set! perm1 j (+ (vector-ref perm1 j) 1))])))
      perm1)))

(check-expect (index->perm 3 0) #(0 1 2))
(check-expect (index->perm 3 1) #(0 2 1))
(check-expect (index->perm 3 2) #(1 0 2))
(check-expect (index->perm 3 3) #(1 2 0))
(check-expect (index->perm 4 12) #(2 0 1 3))
(test)