# %%
jhon_doe = {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}
jess_doe = {'Alice', 'Bob',  'Frank', 'Grace'}

if len(jhon_doe.intersection(jess_doe)):
    print("Tienen amigos en común")
    print(jhon_doe.intersection(jess_doe))
else:
    print("No tienen amigos en común")