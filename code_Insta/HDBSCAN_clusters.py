import pandas as pd
import numpy as np
import hdbscan
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA




def hdbscan_clustering(df):
    # PCA and clustering
    latent_matrix = np.stack(df['latent_vector'].values)
    pca = PCA(n_components=min(100, len(df), latent_matrix.shape[1]))
    latent_pca = pca.fit_transform(latent_matrix)

    df_features = pd.DataFrame(latent_pca, columns=[f'pca_{i}' for i in range(latent_pca.shape[1])])
    df_features["likes"] = df["likes"]
    df_features["comments_count"] = df["comments_count"]
    df_features["positive_comments"] = df["positive_comments"]
    df_features["negative_comments"] = df["negative_comments"]
    df_features["neutral_comments"] = df["neutral_comments"]
    # === Test parameter combinations ===
    results = []
    param_combinations = [
        (30, 10, 0.0),
        (40, 20, 0.01),
        (50, 25, 0.02),
        (60, 30, 0.05),
        (80, 30, 0.05),
        (100, 50, 0.1),
    ]

    for min_cluster_size, min_samples, eps in param_combinations:
        clusterer = hdbscan.HDBSCAN(
            min_cluster_size=min_cluster_size,
            min_samples=min_samples,
            cluster_selection_epsilon=eps,
            cluster_selection_method='eom'
        )
        labels = clusterer.fit_predict(df_features)
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise = np.sum(labels == -1)
        results.append({
            "min_cluster_size": min_cluster_size,
            "min_samples": min_samples,
            "epsilon": eps,
            "n_clusters": n_clusters,
            "n_noise": n_noise
        })
        print(f"Tested: min_cluster_size={min_cluster_size}, min_samples={min_samples}, epsilon={eps} ➤ {n_clusters} clusters, {n_noise} noise")

    # === Display results ===
    results_df = pd.DataFrame(results)
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(results_df["n_clusters"], results_df["n_noise"], c=range(len(results_df)), cmap='viridis')
    for i, row in results_df.iterrows():
        label = f"{i}: size={row['min_cluster_size']}, samp={row['min_samples']}, eps={row['epsilon']}"
        plt.annotate(label, (row["n_clusters"], row["n_noise"]), fontsize=8)
    plt.xlabel("Number of Clusters")
    plt.ylabel("Number of Noise Points")
    plt.title("HDBSCAN Hyperparameter Effects")
    plt.grid(True)
    plt.show()

    # === Ask user to choose ===
    print("\nAvailable parameter sets:")
    for i, row in results_df.iterrows():
        print(f"[{i}] min_cluster_size={row['min_cluster_size']}, min_samples={row['min_samples']}, epsilon={row['epsilon']} ➤ {row['n_clusters']} clusters, {row['n_noise']} noise")

    choice = int(input("\nEnter the index of the preferred parameter combination: "))
    selected_params = results_df.iloc[choice]

    # === Retrain with chosen parameters ===
    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=int(selected_params["min_cluster_size"]),
        min_samples=int(selected_params["min_samples"]),
        cluster_selection_epsilon=float(selected_params["epsilon"]),
        cluster_selection_method='eom'
    )
    df_features["cluster"] = clusterer.fit_predict(df_features)
    labels = clusterer.labels_
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = np.sum(labels == -1)

    print(f"\n✅ Final model: {n_clusters} clusters, {n_noise} noise points")

    # === Merge and Save ===
    df_result = df.copy()
    df_result["cluster"] = df_features["cluster"]