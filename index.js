snail = function(gridArray) {
   //find nxn is true
   snailArray=[]
   tempFrontSnail= []
   reducedGridArrayLength= gridArray.length
   console.log(gridArray)
   console.log(reducedGridArrayLength)

   

   while (reducedGridArrayLength>1){
    gridArray.forEach((element,index) => {
        if (element.length==gridArray.length){
            //grid is confirmed square
            if(index===0){
                snailArray= snailArray.concat(element)
            }
            else if(index !== element.length-1){
                snailArray= snailArray.concat(element[element.length-1])
                tempFrontSnail.push(element[0])
            }
            else if(index === element.length-1){
                snailArray= snailArray.concat(element.reverse())
                snailArray= snailArray.concat(tempFrontSnail)
            }
            
    
        }
       });
    reducedGridArray= gridArray.map(arr => arr.slice(1, -1))
    reducedGridArray.pop()
    reducedGridArray.shift()
    reducedGridArrayLength = reducedGridArray.length
    // console.log("GridArray ="+gridArray)
    console.log(reducedGridArray)
   }
   if (reducedGridArrayLength==1){


   }


  }



  testArray= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  testAnswer= [1, 2, 3, 6, 9, 8, 7, 4, 5]

snail(testArray)
// console.log(snailArray)