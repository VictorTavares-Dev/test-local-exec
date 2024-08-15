resource "terraform_data" "test" {
  # Defines when the provisioner should be executed
  triggers_replace = [timestamp()]

  provisioner "local-exec" {
    command = "sh run.sh"
  }

}