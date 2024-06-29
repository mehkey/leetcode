import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort the rows based on id (Ascending order)
    person.sort_values(by='id',ascending=True,inplace=True)
    # Drop the duplicates based on email.
    person.drop_duplicates(subset='email', keep='first', inplace=True)


# Write your MySQL query statement below
delete pp from person pp where pp.id in (SELECT p1.id from person p1 where p1.email in (SELECT p.email from person p where p.id <> p1.id and p.email = p1.email ))

#delete p1 from person p1,person p2 
#where p1.email=p2.email and p1.id>p2.id;

