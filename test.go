package big_test

import (
	"fmt"
	"log"
	"math"
	"math/big"
	"fmt"
        "os"
       )

type form struct 
{
    
	a Int
	b Int
	c Int
	d Int 	
}

func main() 
{
	if len(os.Args) > 1 
	{
		discriminant := os.Args[1]
		initialize() 	   
		generator()
		square()   
        } 
	else 
	{
		// No arguments were specified!
    		fmt.Println("No Parameters given.... Exiting!!!")
   	}
}

func initialize()
{
	Neg_A, r, denom, old_a, old_b, ra, s, x, g, d, e, q, w, m,
        u, a, b, k, mu, v, sigma, lambda, f3.a, f3.b, f3.c, f3.d := big.NewInt(0), big.NewInt(0), big.NewInt(0),
	big.NewInt(0), big.NewInt(0), big.NewInt(0), big.NewInt(0), big.NewInt(0), big.NewInt(0), big.NewInt(0),
	big.NewInt(0), big.NewInt(0)
	
}

func generator()
{
	form.a.SetUint64(2) 
	form.b.SetUint64(1)
	form.c.SetUint64(0)
	form.d.SetUint64(discriminant)
	
}

