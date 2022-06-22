from matplotlib import pyplot as plt
from matplotlib impot style
style.use("ggplot")
plt.plot([2, 5, 7], [7, 14, 19], label="first", linewidth=2)
plt.scatter([2, 5, 7], [7, 14, 19], label="first", linewidth=2)
plt.hist([2, 5, 7], label="first", linewidth=2)
plt.legend()
plt.title("RandomBuggy's Data")
plt.ylabel("This is Y")
plt.xlabel("This is X")
plt.show()
