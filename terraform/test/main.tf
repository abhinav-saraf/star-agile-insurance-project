provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "test" {
  ami           = "ami-020cba7c55df1f615"
  instance_type = "t2.micro"
  key_name      = "id_rsa"
  associate_public_ip_address = true

  tags = {
    Name = "InsureMe-Test-Server"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install docker.io -y"
    ]
    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("~/.ssh/id_rsa")
      host        = self.public_ip
    }
  }
}

output "test_instance_ip" {
  value = aws_instance.app_server.public_ip
}
