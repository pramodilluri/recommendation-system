# recommendation-system

Criteria :

If age exactly matches in training data :

    # Returns up to the requested number of recommended movies, in the order of highest rating first (5 -> 4 -> 3)
    # Rating less than or equal to 2 are considered to be disliked and not recommended.
    
  
If age doesn't have exact match in training data set :

    # Create age groups 
    # 4 age buckets in this program : (,18] ; (18, 35] ; (36, 50] ; (50, )
    # Return highest rated movies in the age bucket in the order of highest rating first (5 -> 4 -> 3) 
   
   
If training set doesn't have any data for the age group requested

    # Returns empty list
    # No recommendations suggested.
  
  
  
