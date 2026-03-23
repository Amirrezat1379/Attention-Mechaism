import os
import numpy as np
import matplotlib.pyplot as plt

folder_path = "captures"
files = os.listdir(folder_path)
datas = {}

for file in files:
    if file.endswith(".txt"):
        file_path = os.path.join(folder_path, file)

        with open(file_path, 'r') as f:
            data = f.read()
            # Process the data as needed
            # print(f"File: {file}\nData:\n{data}\n{'=' * 30}")
            # data = dict(data)
            di = {}
            data = data.split("{")[1].split("}")[0].split(",")
            for d in data:
                elements = d.split(":")
                di[elements[0].replace(" ", "").replace("'", "")] = float(eval(elements[1]))
            data = di
            datas[f'{file.split(" ")[0][0]} {file.split(" ")[3]}'] = data
datas = {k: v for k, v in sorted(datas.items(), key=lambda item: int(eval(item[0][2:])))}
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(14, 6))
fig1.suptitle("Time and Memory")
fig2.suptitle("Accuracy and Perplexity")
keys = list(datas.keys())
values = list(datas.values())
datas = {"Original LLAMA":{'Perplexity':[], 'Seq_Len':[], 'AvgLatency(ms)':[], 'MemoryAllocated(GB)':[], 'Accuracy(%)':[]},
         "Unfine-tunned Performer LLAMA": {'Perplexity':[], 'Seq_Len':[], 'AvgLatency(ms)':[], 'MemoryAllocated(GB)':[], 'Accuracy(%)':[]},
         "Fine-tunned Performer LLAMA": {'Perplexity':[], 'Seq_Len':[], 'AvgLatency(ms)':[], 'MemoryAllocated(GB)':[], 'Accuracy(%)':[]}}
for i in range(len(values)):
    if keys[i][0] == 'o':
        datas['Original LLAMA']['Seq_Len'].append(int(eval(keys[i][2:])))
        datas['Original LLAMA']['AvgLatency(ms)'].append(values[i]['AvgLatency(ms)'])
        datas['Original LLAMA']['MemoryAllocated(GB)'].append(values[i]['MemoryAllocated(GB)'])
        datas['Original LLAMA']['Accuracy(%)'].append(values[i]['Accuracy(%)'])
        datas['Original LLAMA']['Perplexity'].append(values[i]['Perplexity'])
    elif keys[i][0] == 'u':
        datas['Unfine-tunned Performer LLAMA']['Seq_Len'].append(int(eval(keys[i][2:])))
        datas['Unfine-tunned Performer LLAMA']['AvgLatency(ms)'].append(values[i]['AvgLatency(ms)'])
        datas['Unfine-tunned Performer LLAMA']['MemoryAllocated(GB)'].append(values[i]['MemoryAllocated(GB)'])
        datas['Unfine-tunned Performer LLAMA']['Accuracy(%)'].append(values[i]['Accuracy(%)'])
        datas['Unfine-tunned Performer LLAMA']['Perplexity'].append(values[i]['Perplexity'])
    else:
        datas['Fine-tunned Performer LLAMA']['Seq_Len'].append(int(eval(keys[i][2:])))
        datas['Fine-tunned Performer LLAMA']['AvgLatency(ms)'].append(values[i]['AvgLatency(ms)'])
        datas['Fine-tunned Performer LLAMA']['MemoryAllocated(GB)'].append(values[i]['MemoryAllocated(GB)'])
        datas['Fine-tunned Performer LLAMA']['Accuracy(%)'].append(values[i]['Accuracy(%)'])
        datas['Fine-tunned Performer LLAMA']['Perplexity'].append(values[i]['Perplexity'])

keys = list(datas.keys())
values = list(datas.values())
print(values)
for i in range(len(values)):
    ax1.plot(values[i]['Seq_Len'], values[i]['AvgLatency(ms)'], marker='o', label=keys[i])
    ax2.plot(values[i]['Seq_Len'], values[i]['MemoryAllocated(GB)'], marker='o', label=keys[i])
    ax3.plot(values[i]['Seq_Len'], values[i]['Accuracy(%)'], marker='o', label=keys[i])
    ax4.plot(values[i]['Seq_Len'], values[i]['Perplexity'], marker='o', label=keys[i])

ax1.set_title('Time Usage: Avg Latency vs. Seq Length')
ax1.set_xlabel('Sequence Length')
ax1.set_ylabel('Latency (ms)')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.6)
    
    # Formatting Memory Plot
ax2.set_title('Memory Usage: Allocated GB vs. Seq Length')
ax2.set_xlabel('Sequence Length')
ax2.set_ylabel('Memory (GB)')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.6)

ax3.set_title('Accuracy: % vs. Seq Length')
ax3.set_xlabel('Sequence Length')
ax3.set_ylabel('Accuracy (%)')
ax3.legend()
ax3.grid(True, linestyle='--', alpha=0.6)

ax4.set_title('Perplexity vs. Seq Length')
ax4.set_xlabel('Sequence Length')
ax4.set_ylabel('Perplexity')
ax4.legend()
ax4.grid(True, linestyle='--', alpha=0.6)
    
fig1.savefig("Time and Memory")
fig2.savefig("Accuracy and Perplexity")
plt.tight_layout()
plt.show()