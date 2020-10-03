data "digitalocean_kubernetes_versions" "data_versions" {
    version_prefix = "1.18."
}


resource "digitalocean_kubernetes_cluster" "barckcode" {
    name    = "barckcode"
    region  = "fra1"
    auto_upgrade = true
    version = data.digitalocean_kubernetes_versions.data_versions.latest_version

    node_pool {
        name       = "barckcode-nodes"
        size       = "s-2vcpu-4gb"
        node_count = 1
    }
}