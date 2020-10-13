resource "local_file" "kubernetes_config" {
    content = digitalocean_kubernetes_cluster.barckcode.kube_config.0.raw_config
    filename = "kube_config.yaml"
}