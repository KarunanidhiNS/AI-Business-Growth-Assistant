const ctx =
document.getElementById(
    'sentimentChart'
);

if(ctx){

new Chart(ctx, {

type:'pie',

data:{

labels:[
'Positive',
'Negative',
'Neutral'
],

datasets:[{

data:[
positiveCount,
negativeCount,
neutralCount
]

}]

}

});

}