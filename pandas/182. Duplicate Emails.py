import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
      return pd.DataFrame(person[person.duplicated(subset='email')].email).drop_duplicates()

    #results = pd.DataFrame()

    results = person.loc[person.duplicated(subset=['email']), ['email']]
    
    return results.drop_duplicates()
    
    return person[person.duplicated(['email'])][['email']].drop_duplicates()

    '''
    v = person.groupby("email", as_index=False).count()
    print(v)
    return v[v["id"] > 1][['email']]
    '''
    # Write your MySQL query statement below
SELECT P.email
FROM Person P
GROUP BY P.email
HAVING COUNT(*) > 1


#SELECT DISTINCT p.email 
#FROM Person p
#WHERE p.email in (SELECT email from Person where p.id <> id)