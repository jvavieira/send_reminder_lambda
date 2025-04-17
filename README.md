# WhatsApp Reminder com AWS Lambda + Twilio

Este projeto envia mensagens automáticas via WhatsApp para lembrar sobre medicamentos, utilizando AWS Lambda, Twilio e Secrets Manager.

## Tecnologias
- Python
- AWS Lambda
- AWS EventBridge (Scheduler)
- AWS Secrets Manager
- Twilio API (Sandbox)

## Como funciona
1. Lambda envia mensagem via Twilio
2. Secrets são protegidos com Secrets Manager
3. Executado automaticamente 3x por dia com agendamento via EventBridge

## Exemplo de mensagem
> "Oi, mo ❤️. Hora de tomar seu remédio!! ⏰"

## Autor
[Joao Victor](https://github.com/jvavieira)
