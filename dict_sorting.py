
scores = [
    {
        'timestamp': '15:28:29 6/7/2020',
        'points': '9',
        'run_length': '50'
        
    },
    {
        'timestamp': '15:27:29 9/7/2019',
        'points': '0',
        'run_length': '0'
        
    },
      {
        'timestamp': '15:27:29 9/7/2019',
        'points': '5',
        'run_length': '20'
        
    }
]

sort_key="run_length"

sorted_scores=sorted(scores, key=lambda x: x[sort_key], reverse=True)


for score in sorted_scores:
    print(score)

