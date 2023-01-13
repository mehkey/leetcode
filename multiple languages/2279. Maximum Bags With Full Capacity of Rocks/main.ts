function maximumBags(capacity: number[], rocks: number[], additionalRocks: number): number {

    let diff : number[] = new Array();

    for ( let i = 0; i < capacity.length; i++){
        diff[i] = capacity[i] - rocks[i];
    }

    diff.sort( (a:number,b:number) => a-b );

    //console.log(diff);

    for ( let i = 0; i < diff.length; i++ ){

        if (diff[i] > additionalRocks || additionalRocks === 0){
            return i ;
        }
        additionalRocks = additionalRocks - diff[i];
    }

    return diff.length;
};