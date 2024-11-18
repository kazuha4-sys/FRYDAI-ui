#!/bin/bash

USERNAME="kauanCybis"
PASSWORD="kakadudu"

# Função de login
function login() {
    echo -n "Nome de usuario: "
    read input_user

    echo -n "Senha: "
    read -s input_pass
    echo 

    # Verificar se as credenciais estão corretas
    if [[ "$input_user" == "$USERNAME" && "$input_pass" == "$PASSWORD" ]]; then
        echo "Login bem-sucedido!"
        welcome_screen
    else
        echo "Login falhou. Tente novamente."
        login
    fi
}

# Função de boas-vindas
function welcome_screen() {
    clear
    sleep 1
    echo "Iniciando interface..."
    sleep 0.5
    echo "Iniciando Frydai..."
    sleep 0.5
    echo "Iniciando sistema..."
    sleep 1

    # Exibição dos serviços com tempo de carregamento simulado
    echo "Starting System Logger and Monitoring Services for Extended Logging Capabilities"
    echo "Loading Essential Kernel Modules and Device Drivers for Hardware Compatibility"
    echo "Performing Filesystem Integrity Checks to Ensure Data Consistency and Reliability"
    echo "Setting Up Hostname and Local DNS Services for Networked Communication"
    echo "Synchronizing System Clock with Network Time Protocol (NTP) for Accurate Timing"
    sleep 2
    echo "Bringing Up Network Interfaces and Configuring IP Addresses via DHCP"
    echo "Activating Firewall Services and Security Policies for Enhanced Protection"
    echo "Mounting Local and Remote Filesystems to Ensure Accessibility of Critical Data"
    echo "Cleaning Temporary Files and Cache Directories to Optimize Storage Utilization"
    echo "Initializing System Security Services and Authentication Modules for Access Control"
    echo "Starting Apache Web Server to Serve Web Content and Manage HTTP Requests"
    echo "Starting MySQL Database Server for Data Storage and Management Solutions"
    echo "Initializing Network Management Daemon for Dynamic Network Configuration"
    echo "Checking Disk Space, Monitoring Partitions, and Enforcing Disk Quotas for Stability"
    echo "Loading Security Policies and Applying System-wide Permissions for All Users"
    echo "Starting SSH Daemon for Secure Remote Access and Administration Capabilities"
    echo "Launching User Management Services and Verifying User Profiles and Permissions"
    echo "Setting Up Graphical User Interface with Default Window Manager Configuration"
    echo "Initializing Display Manager and Loading Desktop Environment Preferences"
    echo "Checking for System Updates and Applying Necessary Patches for Enhanced Security"
    sleep 2
    echo "Applying User-specific Customizations and Environment Variables"
    echo "Loading Virtual Memory Management and Allocating Swap Space for System Resources"
    echo "Configuring System Services Based on Profile Settings and Dependency Requirements"
    echo "Starting Email Services and Managing Inbound and Outbound Message Queues"
    sleep 1

    # Segunda lista de serviços com barra de progresso
    services=(
        "Initializing System Logging and Diagnostics for Error Tracking and Troubleshooting"
        "Loading GPU Drivers and Configuring Hardware Acceleration for Graphics Processing"
        "Applying Power Management Settings to Optimize Performance and Battery Usage"
        "Starting Cron Daemon for Scheduled Task Execution and System Automation"
        "Starting Print Services and Configuring Local and Networked Printers"
        "Starting Sound Services and Initializing Audio Drivers for Multimedia Playback"
        "Loading Application Frameworks and Libraries for Enhanced Compatibility"
        "Starting Bluetooth Services and Configuring Device Pairing and Communication"
        "Starting Clipboard Services and Enabling Shared Data Management"
        "Mounting Network Shares for Access to Remote Files and Directories"
    )

    # Loop para simular carregamento com barra de progresso
    for service in "${services[@]}"; do
        echo -n "$service ... "
        
        # Simula a barra de progresso com delay
        for i in {1..3}; do
            echo -n "["
            sleep 0.1
            echo -n "------------------"
            sleep 0.1
            echo "]"
            sleep 0.2
        done
        echo " [  OK  ]"
        sleep 0.2
    done

    # Mensagem de boas-vindas
    clear
    echo "-----------------------------------------"
    echo "            BEM-VINDO AO FRYDAI-UI       "
    echo "-----------------------------------------"
    sleep 1

    # Barra de carregamento
    echo "Carregando interface... [█████-----]"
    sleep 0.5
    clear
    echo "Carregando interface... [████████--]"
    sleep 0.5
    clear
    echo "Carregando interface... [██████████]"
    sleep 0.5
    clear

    echo "Interface do sistema carregada!"
    sleep 1
    clear

    # Informações de status do sistema
    echo "-----------------------------------------"
    echo "         FRYDAI-UI Sistema Ativo         "
    echo "-----------------------------------------"
    echo "Data e Hora: $(date)"
    echo "Usuário Atual: $USERNAME"
    echo "Hostname: $HOSTNAME"
    echo "Uptime: $(uptime -p)"
    echo "-----------------------------------------"
    echo ""
    read -r 
    clear
    # Exibe o ASCII art de boas-vindas
    ascii_art

    # Função para abrir os arquivos HTML
    open_html_files

    # Manter o terminal aberto até o usuário pressionar Enter
    echo "Pressione Enter para continuar..."
    read -r  # Aguarda o usuário pressionar Enter
}

open_html_files() {
    # abrir arquivo de inicialização chamada teste.html
    explore.exe tetse.html
}

open_python(){
    python f11.py
}

# Função ASCII Art
function ascii_art() {
    echo " _______  ______ __   __ ______  _______ _____     _     _ _____"
    echo " |______ |_____/   \_/   |     \ |_____|   |   ___ |     |   |  "
    echo " |       |    \_    |    |_____/ |     | __|__     |_____| __|__"
    echo "                                                                "
}

# Executa o login
login
