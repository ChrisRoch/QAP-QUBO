import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


num_instances = 6
solvers = ['quantum_annealing', 'simulated_annealing', 'qbsolv']
instances = [str(i) for i in range(num_instances)]
data = {}
for solver in solvers:
    for j in range(num_instances):
        results_loaded = np.load('./results/test_instance_' + str(j+4) + '_' + solver + '.npy', allow_pickle=True)
        all_runs = results_loaded.item().get('all_runs')
        energies = []
        for i in range(len(all_runs)):
            energies.append(all_runs[i][0][1])
        data[(str(j), solver)] = energies


sns.set_style("whitegrid")
sns.set_context({"figure.figsize": (12, 5)})
fig, axes = plt.subplots(ncols=6)
fig.subplots_adjust(wspace=1.5)
colors = ['tab:blue', 'tab:green', 'tab:red'] # 'green', 'blue'
for ax, instance in zip(axes, instances):
    bp = ax.boxplot([data[(instance, solver)] for solver in solvers], widths=0.5, patch_artist=True)
    ax.set_ylim([max([max(data[(instance, solver)]) for solver in solvers]) + 50, min([min(data[(instance, solver)])
                                                                                       for solver in solvers]) - 50])
    ax.set_yscale('linear')
    ax.tick_params(labelleft=True)
    ax.set(xlabel=instance)
    ax.set_xticklabels(labels=['QA', 'SA', 'QBSolv'], rotation=45)
    ax.margins(0.05)
    ax.yaxis.grid(True)
    ax.xaxis.grid(False)
    for patch, color in zip(bp['boxes'], colors):
        patch.set(facecolor=color)
axes[0].set_ylabel('Energy')
plt.tight_layout()
# plt.show()
plt.savefig('./results/result_plot.pdf', dpi=300)
