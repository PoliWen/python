import matplotlib.pyplot as plt
labels = ['Major Match', 'no match']
sizes = [273, 727]
colors = ['#E2E2E2', '#6392BF']
explode = (0, 0.08)
plt.figure(figsize=(7, 7))
plt.pie(sizes,
        labels=labels,
        explode=explode,
        autopct='%1.1f%%',
        colors=colors,
        startangle=270,
        shadow=True)
plt.savefig('major-match-job.png', transparent=True)
plt.show()
