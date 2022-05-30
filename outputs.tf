output "password" {
  value = azurerm_postgresql_server.mlflowserver.administrator_login_password
  sensitive = true
}