#!/usr/bin/env ghci

--PROBLEM: 000
--AUTHOR:  Dirk Meijer
--STATUS:  {experimentation, in-progress, needs-optimization, done}
--EXPLANATION:
--    <explanation here>

import Data.List

chain :: Integer -> Integer
chain 1 = 0
chain n 
    | even n    = 1 + chain (quot n 2)
    | otherwise = 1 + chain (3*n+1)


main :: IO()
main = print $ maximumBy (\x y -> compare (chain x) (chain y)) [1..999999]
