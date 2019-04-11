#!/usr/bin/env ghci

--PROBLEM: 014
--AUTHOR:  Dirk Meijer
--STATUS:  done
--EXPLANATION:
--    built-in memoization (because no side effects) and proper tail calls. 
--    can undoubtedly be improved.

import Data.List

chain :: Integer -> Integer
chain 1 = 0
chain n 
    | even n    = 1 + chain (quot n 2)
    | otherwise = 1 + chain (3*n+1)


main :: IO()
main = print $ maximumBy (\x y -> compare (chain x) (chain y)) [1..999999]
