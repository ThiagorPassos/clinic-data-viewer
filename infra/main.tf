# 1. Variáveis
variable "aws_region" {
  description = "Região da AWS onde a infraestrutura será criada"
  default     = "us-east-1"
}

variable "projeto_nome" {
  description = "Nome do projeto para as tags de identificação"
  default     = "clinic-data-viewer"
}

# 2. Provedor AWS
provider "aws" {
  region = var.aws_region
  
}

# 3. Provisionamento da Instância EC2
resource "aws_instance" "app_server" {
  ami           = "ami-007855ac798b5175e" # Ubuntu 22.04 LTS 
  instance_type = "t2.micro"

  tags = {
    Name        = "${var.projeto_nome}-ec2"
    Environment = "Desenvolvimento"
    ManagedBy   = "Terraform"
    Owner       = "Thiago Passos"
  }
}
