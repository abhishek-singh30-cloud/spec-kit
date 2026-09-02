resource "azurerm_resource_group" "rg" {
  name     = "rg-demo-prod"
  location = "eastus"
}

module "vnet" {

  source = "Azure/avm-res-network-virtualnetwork/azurerm"

  name = "vnet-demo"

  resource_group_name =
  azurerm_resource_group.rg.name

  location =
  azurerm_resource_group.rg.location

  address_space = [
    "10.0.0.0/16"
  ]
}
