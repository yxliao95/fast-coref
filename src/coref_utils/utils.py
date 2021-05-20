
def get_mention_to_cluster(clusters, threshold=1):
    clusters = [tuple(tuple(mention) for mention in cluster)
                for cluster in clusters if len(cluster) >= threshold]
    mention_to_cluster_dict = {}
    for cluster in clusters:
        for mention in cluster:
            mention_to_cluster_dict[mention] = cluster
    return clusters, mention_to_cluster_dict


def get_mention_to_cluster_idx(clusters, threshold=1):
    clusters = [tuple(tuple(mention) for mention in cluster)
                for cluster in clusters if len(cluster) >= threshold]
    mention_to_cluster_dict = {}
    for cluster_idx, cluster in enumerate(clusters):
        for mention in cluster:
            mention_to_cluster_dict[mention] = cluster_idx
    return mention_to_cluster_dict


def get_ordered_mentions(clusters):
    """Order all the mentions in the doc w.r.t. span_start and in case of ties span_end."""
    all_mentions = []
    for cluster in clusters:
        all_mentions.extend(cluster)

    # Span start is the main criteria, and span end is used to break ties
    all_mentions = sorted(all_mentions, key=lambda x: x[0] + 1e-5 * x[1])
    return all_mentions


def remove_singletons(data, key="clusters"):
    data_without_singletons = []
    for instance in data:
        instance[key] = [cluster for cluster in instance[key] if len(cluster) > 1]
        data_without_singletons.append(instance)

    return data_without_singletons


def is_aligned(span1, span2):
    if span1[0] >= span2[0] and span1[1] <= span2[1]:
        return True
    if span2[0] >= span1[0] and span2[1] <= span1[1]:
        return True
    return False
