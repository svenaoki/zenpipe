// deploy resource group
resource "azurerm_resource_group" "rg" {
  name     = "${random_pet.name.id}rg"
  location = "West Europe"
}
provider "azurerm" {
  features {}
}

// deploy storage account
resource "azurerm_storage_account" "sa" {
  name                     = "${random_pet.name.id}sa"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  tags = {
    key = "value"
  }
}

// deploy blob storage
resource "azurerm_storage_container" "sc" {
  name                  = "${random_pet.name.id}sc"
  storage_account_name  = azurerm_storage_account.sa.name
  container_access_type = "private"
}


// kubernetes server
resource "azurerm_kubernetes_cluster" "kc" {
  name                = "${random_pet.name.id}aks"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "${random_pet.name.id}ks"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_D2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Production"
  }
}

resource "azurerm_container_registry" "acr" {
  name                = "${random_pet.name.id}acr"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = false
}

# // deploy postgresdb server 
# resource "azurerm_postgresql_server" "mlflowserver" {
#   name                = "${random_pet.name.id}-mlflow-server"
#   location            = "eastus"
#   resource_group_name = azurerm_resource_group.rg.name

#   sku_name = "B_Gen5_2"

#   storage_mb                   = 5120
#   backup_retention_days        = 7
#   geo_redundant_backup_enabled = false
#   auto_grow_enabled            = true

#   administrator_login          = "adminroot"
#   administrator_login_password = random_password.password.result
#   version                      = "9.5"
#   ssl_enforcement_enabled      = true
# }

# // deploy postgresdb database
# resource "azurerm_postgresql_database" "mlflowdb" {
#   name                = "${random_pet.name.id}-mlflow-db"
#   resource_group_name = azurerm_resource_group.rg.name
#   server_name         = azurerm_postgresql_server.mlflowserver.name
#   charset             = "UTF8"
#   collation           = "English_United States.1252"
#}
