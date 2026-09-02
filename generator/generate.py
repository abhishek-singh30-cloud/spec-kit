import yaml
import os

with open("specs/prod/network.yaml") as f:
    spec = yaml.safe_load(f)

rg = spec["resourceGroup"]["name"]
location = spec["resourceGroup"]["location"]

vnet = spec["vnet"]["name"]
address_space = spec["vnet"]["address_space"][0]

terraform = f'''
terraform {{
  required_providers {{
    azurerm = {{
      source  = "hashicorp/azurerm"
      version = "~>4.0"
    }}
  }}
}}

provider "azurerm" {{
  features {{}}
}}

resource "azurerm_resource_group" "rg" {{
  name     = "{rg}"
  location = "{location}"
}}

module "vnet" {

  source = "Azure/avm-res-network-virtualnetwork/azurerm"

  name = "{vnet}"

  address_space = [
    "{address_space}"
  ]
}

os.makedirs("generated", exist_ok=True)

with open("generated/main.tf", "w") as f:
    f.write(terraform)

print("Terraform generated using AVM")
