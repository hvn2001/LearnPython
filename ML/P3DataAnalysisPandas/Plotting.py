import pandas as pd
import matplotlib.pyplot as plt

print('------A. Basics------')

df = pd.DataFrame({
    'teamID': ['BOS', 'SEA', 'SEA', 'BOS', 'SEA'],
    'HR': [31, 39, 43, 38, 39],
    'SO': [31, 39, 43, 38, 39],
    'RBI': [80, 100, 12, 16, 18]})
print('{}\n'.format(df))

df.plot()
plt.show()

print('------A. plt.savefig ------')
# predefined df
print('{}\n'.format(df))

df.plot()
plt.savefig('df.png')  # save to PNG file

print('------A. set the plot''s title and axis labels using the pyplot API ------')
# predefined df
print('{}\n'.format(df))

df.plot()
plt.title('HR vs. Year')
plt.xlabel('Year')
plt.ylabel('HR Count')
plt.show()

print('------B. Other plots------')
# predefined df
print('{}\n'.format(df))

df.plot(kind='hist')
df.plot(kind='box')
plt.show()

print('------C. Multiple features------')
# predefined df
print('{}\n'.format(df))

df.plot()
df.plot(kind='box')
plt.show()
