<?php
    function isPrime($num) {
        $prime = 1;
        
        for($dividing = 2; $dividing <= sqrt($num); $dividing++) {
            if($num % $dividing == 0) {
                $prime = 0;
                break;
            }
        }

        if($prime == 1 && $num > 1) {
            return true;
        }

        return false;
    }

    function findQuadraticPrimes() {
        $maxPrimeCount = 0;
        $maxAxB = 0;

        for($a = -999; $a <= 999; $a++) {
            for($b = -1000; $b <= 1000; $b++) {
                for($n = 0; $n < $n + 1; $n++) {
                    $num = $n * $n + $a * $n + $b;
                    
                    if(!isPrime($num)) {
                        if($n > $maxPrimeCount) {
                            $maxPrimeCount = $n;
                            $maxAxB = $a * $b;
                        }
                        break;
                    }
                }
            }
        }
        
        return $maxAxB;
    }

    echo findQuadraticPrimes();
?>
