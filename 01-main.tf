resource "digitalocean_kubernetes_cluster" "barckcode" {
    name    = "barckcode"
    region  = "fra1"
    version = "1.18.8-do.1"

    node_pool {
        name       = "barckcode-nodes"
        size       = "s-2vcpu-4gb"
        node_count = 1
    }
}