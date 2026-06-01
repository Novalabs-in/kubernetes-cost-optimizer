import pandas as pd
import numpy as np

class K8sCostOptimizer:
    """
    Kubernetes Cluster Cost Optimization Engine
    Monitors CPU/Memory resource metrics and flags overallocation limits.
    """
    def __init__(self):
        pass

    def analyze_node_utilization(self, utilization_log):
        df = pd.DataFrame(utilization_log)
        df['CPU_Overallocated'] = np.where(df['Allocated_CPU'] > df['Used_CPU'] * 2.0, True, False)
        
        waste = df[df['CPU_Overallocated'] == True]
        savings = len(waste) * 45.0 # Assume $45 savings per node per month
        return savings, waste

if __name__ == "__main__":
    metrics = {
        "Node": ["Node-A", "Node-B", "Node-C"],
        "Allocated_CPU": [8.0, 8.0, 4.0],
        "Used_CPU": [2.1, 7.5, 1.0]
    }
    optimizer = K8sCostOptimizer()
    savings, waste = optimizer.analyze_node_utilization(metrics)
    print(f"Optimal Cluster Savings Recommendation: ${savings:.2f}/month")
    print("Overallocated Waste Nodes:")
    print(waste)
