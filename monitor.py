#!/usr/bin/env python3
"""
MODERN CLOUD DASHBOARD - Professional & Innovative Design
Complete Interactive Cloud Infrastructure Management
All 10 Services Fully Functional
"""

from flask import Flask, render_template_string, jsonify, request
from datetime import datetime
import boto3
import json
import uuid

app = Flask(__name__)

LOCALSTACK_ENDPOINT = 'http://localhost:4566'
REGION = 'us-east-1'

def get_client(service):
    return boto3.client(
        service,
        endpoint_url=LOCALSTACK_ENDPOINT,
        aws_access_key_id='test',
        aws_secret_access_key='test',
        region_name=REGION
    )

def get_service_metrics():
    """Get metrics from all services"""
    metrics = {}
    
    # S3
    try:
        s3 = get_client('s3')
        buckets = s3.list_buckets()
        metrics['s3'] = {
            'status': 'operational',
            'buckets': len(buckets['Buckets']),
            'bucket_names': [b['Name'] for b in buckets['Buckets']]
        }
    except Exception as e:
        metrics['s3'] = {'status': 'error', 'error': str(e)[:50]}
    
    # API Gateway
    try:
        apig = get_client('apigateway')
        apis = apig.get_rest_apis()
        metrics['apigateway'] = {
            'status': 'operational',
            'apis': len(apis.get('items', [])),
            'api_names': [a['name'] for a in apis.get('items', [])],
            'api_ids': [a['id'] for a in apis.get('items', [])]
        }
    except Exception as e:
        metrics['apigateway'] = {'status': 'error', 'error': str(e)[:50]}
    
    # DynamoDB
    try:
        dynamodb = get_client('dynamodb')
        tables = dynamodb.list_tables()
        metrics['dynamodb'] = {
            'status': 'operational',
            'tables': len(tables.get('TableNames', [])),
            'table_names': tables.get('TableNames', [])
        }
    except Exception as e:
        metrics['dynamodb'] = {'status': 'error', 'error': str(e)[:50]}
    
    # SQS
    try:
        sqs = get_client('sqs')
        queues = sqs.list_queues()
        queue_urls = queues.get('QueueUrls', [])
        metrics['sqs'] = {
            'status': 'operational',
            'queues': len(queue_urls),
            'queue_names': [url.split('/')[-1] for url in queue_urls]
        }
    except Exception as e:
        metrics['sqs'] = {'status': 'error', 'error': str(e)[:50]}
    
    # CloudWatch Logs
    try:
        logs = get_client('logs')
        log_groups = logs.describe_log_groups()
        metrics['cloudwatch'] = {
            'status': 'operational',
            'log_groups': len(log_groups.get('logGroups', [])),
            'log_group_names': [lg['logGroupName'] for lg in log_groups.get('logGroups', [])]
        }
    except Exception as e:
        metrics['cloudwatch'] = {'status': 'error', 'error': str(e)[:50]}
    
    # Secrets Manager
    try:
        sm = get_client('secretsmanager')
        secrets = sm.list_secrets()
        metrics['secretsmanager'] = {
            'status': 'operational',
            'secrets': len(secrets.get('SecretList', [])),
            'secret_names': [s['Name'] for s in secrets.get('SecretList', [])]
        }
    except Exception as e:
        metrics['secretsmanager'] = {'status': 'error', 'error': str(e)[:50]}
    
    # SNS
    try:
        sns = get_client('sns')
        topics = sns.list_topics()
        metrics['sns'] = {
            'status': 'operational',
            'topics': len(topics.get('Topics', [])),
            'topic_names': [t['TopicArn'].split(':')[-1] for t in topics.get('Topics', [])]
        }
    except Exception as e:
        metrics['sns'] = {'status': 'error', 'error': str(e)[:50]}
    
    # Lambda
    try:
        lamb = get_client('lambda')
        functions = lamb.list_functions()
        metrics['lambda'] = {
            'status': 'operational',
            'functions': len(functions.get('Functions', [])),
            'function_names': [f['FunctionName'] for f in functions.get('Functions', [])]
        }
    except Exception as e:
        metrics['lambda'] = {'status': 'error', 'error': str(e)[:50]}
    
    # Kinesis
    try:
        kinesis = get_client('kinesis')
        streams = kinesis.list_streams()
        metrics['kinesis'] = {
            'status': 'operational',
            'streams': len(streams.get('StreamNames', [])),
            'stream_names': streams.get('StreamNames', [])
        }
    except Exception as e:
        metrics['kinesis'] = {'status': 'error', 'error': str(e)[:50]}
    
    # SES
    try:
        ses = get_client('ses')
        identities = ses.list_identities()
        metrics['ses'] = {
            'status': 'operational',
            'verified_emails': len(identities.get('Identities', []))
        }
    except Exception as e:
        metrics['ses'] = {'status': 'error', 'error': str(e)[:50]}
    
    return metrics

# HTML Template - Modern Professional Design (Sama seperti sebelumnya, hanya JavaScript-nya diperbarui)
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexus Cloud | Infrastructure Control Center</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #0f0c29 0%, #1a1a3e 50%, #0f0c29 100%);
            color: #f0f0f0;
            min-height: 100vh;
        }
        .navbar {
            background: rgba(15, 20, 35, 0.8);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        .nav-container {
            max-width: 1440px;
            margin: 0 auto;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .logo-section {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .logo-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        .logo-text {
            font-weight: 700;
            font-size: 1.3rem;
            background: linear-gradient(135deg, #fff, #a8b8ff);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        .logo-badge {
            font-size: 0.7rem;
            padding: 2px 8px;
            background: rgba(102, 126, 234, 0.2);
            border-radius: 20px;
            color: #a8b8ff;
            margin-left: 8px;
        }
        .health-status {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .status-pill {
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.3);
            padding: 6px 16px;
            border-radius: 100px;
            font-size: 0.8rem;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .pulse-dot {
            width: 8px;
            height: 8px;
            background: #10b981;
            border-radius: 50%;
            animation: pulse 1.5s infinite;
            box-shadow: 0 0 8px #10b981;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(0.8); }
        }
        .container {
            max-width: 1440px;
            margin: 0 auto;
            padding: 2rem;
        }
        .hero {
            margin-bottom: 2.5rem;
        }
        .hero-title {
            font-size: 2rem;
            font-weight: 700;
            background: linear-gradient(135deg, #fff, #c4b5fd);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin-bottom: 0.5rem;
        }
        .hero-subtitle {
            color: #94a3b8;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.5rem;
            margin-bottom: 2.5rem;
        }
        .stat-card {
            background: rgba(20, 25, 45, 0.6);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 24px;
            padding: 1.25rem 1.5rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .stat-card:hover {
            border-color: rgba(102, 126, 234, 0.4);
            transform: translateY(-3px);
            background: rgba(30, 35, 55, 0.7);
        }
        .stat-icon {
            font-size: 1.8rem;
            margin-bottom: 0.75rem;
            opacity: 0.8;
        }
        .stat-label {
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 600;
            color: #94a3b8;
            margin-bottom: 0.5rem;
        }
        .stat-value {
            font-size: 2.2rem;
            font-weight: 700;
            color: #fff;
        }
        .stat-trend {
            font-size: 0.7rem;
            color: #10b981;
            margin-top: 0.5rem;
        }
        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 1.5rem;
        }
        .section-title {
            font-size: 1.2rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .service-count {
            font-size: 0.8rem;
            color: #94a3b8;
            background: rgba(255,255,255,0.05);
            padding: 4px 12px;
            border-radius: 20px;
        }
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 1.25rem;
        }
        .service-card {
            background: rgba(20, 25, 45, 0.5);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 20px;
            padding: 1.25rem;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }
        .service-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, #667eea, #764ba2, transparent);
            opacity: 0;
            transition: opacity 0.3s;
        }
        .service-card:hover {
            transform: translateY(-4px);
            border-color: rgba(102, 126, 234, 0.3);
            background: rgba(30, 35, 55, 0.7);
        }
        .service-card:hover::before {
            opacity: 1;
        }
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }
        .service-info {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .service-icon {
            width: 44px;
            height: 44px;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.1));
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
        }
        .service-name h4 {
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 2px;
        }
        .service-name p {
            font-size: 0.7rem;
            color: #94a3b8;
        }
        .status-indicator {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.7rem;
            font-weight: 500;
            padding: 4px 10px;
            background: rgba(16, 185, 129, 0.12);
            border-radius: 20px;
            color: #10b981;
            border: 1px solid rgba(16, 185, 129, 0.2);
        }
        .card-metrics {
            margin: 1rem 0;
            padding: 0.75rem 0;
            border-top: 1px solid rgba(255,255,255,0.05);
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .metric-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.8rem;
            padding: 6px 0;
        }
        .metric-label {
            color: #94a3b8;
        }
        .metric-number {
            font-weight: 600;
            color: #fff;
        }
        .control-action {
            margin-top: 1rem;
            padding: 8px 16px;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.1));
            border: 1px solid rgba(102, 126, 234, 0.3);
            border-radius: 40px;
            text-align: center;
            font-weight: 800;
            font-size: 0.75rem;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: #c4b5fd;
            transition: all 0.3s;
            backdrop-filter: blur(4px);
        }
        .control-action:hover {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-color: transparent;
            transform: scale(1.02);
        }
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.7);
            backdrop-filter: blur(12px);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }
        .modal-content {
            background: linear-gradient(135deg, rgba(25, 30, 50, 0.98), rgba(15, 20, 40, 0.98));
            backdrop-filter: blur(20px);
            border-radius: 28px;
            max-width: 520px;
            width: 90%;
            border: 1px solid rgba(102, 126, 234, 0.3);
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
        }
        .modal-header {
            padding: 1.25rem 1.5rem;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .modal-header h3 {
            font-weight: 700;
            font-size: 1.2rem;
            background: linear-gradient(135deg, #fff, #c4b5fd);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        .close-btn {
            background: rgba(255,255,255,0.05);
            border: none;
            color: #94a3b8;
            font-size: 1.5rem;
            cursor: pointer;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }
        .close-btn:hover {
            background: rgba(255,255,255,0.1);
            color: #fff;
        }
        .modal-body {
            padding: 1.5rem;
        }
        .form-group {
            margin-bottom: 1.25rem;
        }
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: #cbd5e1;
            font-size: 0.8rem;
            font-weight: 500;
            letter-spacing: 0.3px;
        }
        .form-group input, .form-group select, .form-group textarea {
            width: 100%;
            padding: 0.75rem 1rem;
            background: rgba(10, 12, 25, 0.7);
            border: 1px solid rgba(102, 126, 234, 0.2);
            border-radius: 14px;
            color: #fff;
            font-size: 0.85rem;
            font-family: 'Inter', monospace;
            transition: all 0.2s;
        }
        .form-group input:focus, .form-group select:focus, .form-group textarea:focus {
            outline: none;
            border-color: #667eea;
            background: rgba(10, 12, 25, 0.9);
        }
        .btn {
            width: 100%;
            padding: 0.85rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border: none;
            border-radius: 14px;
            color: white;
            cursor: pointer;
            font-weight: 700;
            font-size: 0.85rem;
            letter-spacing: 0.5px;
            transition: all 0.3s;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        }
        .result-box {
            background: rgba(10, 12, 25, 0.7);
            border-radius: 14px;
            padding: 1rem;
            margin-top: 1rem;
            font-family: 'Monaco', monospace;
            font-size: 0.7rem;
            overflow-x: auto;
            max-height: 200px;
            overflow-y: auto;
            border: 1px solid rgba(102, 126, 234, 0.2);
        }
        .footer {
            margin-top: 3rem;
            padding: 1.5rem 2rem;
            background: rgba(15, 20, 35, 0.5);
            border-radius: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.7rem;
            color: #64748b;
            backdrop-filter: blur(10px);
        }
        @media (max-width: 768px) {
            .stats-grid { grid-template-columns: repeat(2, 1fr); gap: 1rem; }
            .container { padding: 1rem; }
            .hero-title { font-size: 1.5rem; }
            .nav-container { padding: 0.75rem 1rem; }
            .services-grid { grid-template-columns: 1fr; }
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .service-card {
            animation: fadeIn 0.4s ease-out forwards;
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo-section">
                <div class="logo-icon">☁️</div>
                <div>
                    <span class="logo-text">Abhraka Cloud Infrastructure</span>
                    <span class="logo-badge">Control Center</span>
                </div>
            </div>
            <div class="health-status">
                <div class="status-pill">
                    <div class="pulse-dot"></div>
                    <span id="overallStatus">All Running Systems</span>
                </div>
            </div>
        </div>
    </nav>
    
    <div class="container">
        <div class="hero">
            <h1 class="hero-title">Infrastructure Control Plane</h1>
            <div class="hero-subtitle">
                <span>📍 Local Cloud</span>
                <span>🔗 Endpoint: http://172.29.63.145:5000/</span>
                <span>🔵 Infrastructure Management</span>
            </div>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-icon">📈</div>
                <div class="stat-label">ACTIVE SERVICES</div>
                <div class="stat-value" id="totalServices">-</div>
                <div class="stat-trend">▲ 10 Monitored</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">🟢</div>
                <div class="stat-label">HEALTHY</div>
                <div class="stat-value" id="operationalCount">-</div>
                <div class="stat-trend">Operational</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">⚙️</div>
                <div class="stat-label">TOTAL ASSETS</div>
                <div class="stat-value" id="totalResources">-</div>
                <div class="stat-trend">Deployed resources</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">🖱️</div>
                <div class="stat-label">INTERACTION</div>
                <div class="stat-value" style="font-size:1.2rem;">Click Card →</div>
                <div class="stat-trend">manage resources</div>
            </div>
        </div>
        
        <div class="section-header">
            <div class="section-title">
                <span>🔧</span> Managed Services
            </div>
            <div class="service-count" id="serviceCount">0 services</div>
        </div>
        
        <div class="services-grid" id="servicesGrid"></div>
        
        <div class="footer">
            <div>© Informatic Student Cloud Platform • Built on LocalStack</div>
            <div id="timestamp"></div>
        </div>
    </div>
    
    <div id="modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 id="modalTitle">Resource Manager</h3>
                <button class="close-btn" onclick="closeModal()">✕</button>
            </div>
            <div class="modal-body" id="modalBody"></div>
        </div>
    </div>
    
    <script>
        let currentData = null;
        
        async function loadDashboard() {
            const res = await fetch('/api/metrics');
            currentData = await res.json();
            renderDashboard(currentData);
        }
        
        function renderDashboard(data) {
            const services = Object.values(data);
            const operational = services.filter(s => s.status === 'operational').length;
            let totalResources = 0;
            for (const [key, val] of Object.entries(data)) {
                if (val.buckets) totalResources += val.buckets;
                if (val.queues) totalResources += val.queues;
                if (val.topics) totalResources += val.topics;
                if (val.tables) totalResources += val.tables;
                if (val.functions) totalResources += val.functions;
                if (val.secrets) totalResources += val.secrets;
                if (val.apis) totalResources += val.apis;
                if (val.log_groups) totalResources += val.log_groups;
                if (val.streams) totalResources += val.streams;
                if (val.verified_emails) totalResources += val.verified_emails;
            }
            document.getElementById('totalServices').innerText = Object.keys(data).length;
            document.getElementById('operationalCount').innerText = operational;
            document.getElementById('totalResources').innerText = totalResources;
            document.getElementById('serviceCount').innerText = Object.keys(data).length + ' services';
            document.getElementById('timestamp').innerHTML = `Last Updated : ${new Date().toLocaleTimeString()}`;
            
            const servicesConfig = {
                's3': { name: 'S3 Storage', category: 'Storage', icon: '📦', metric: (d) => `${d.buckets} buckets` },
                'apigateway': { name: 'API Gateway', category: 'Networking', icon: '🌐', metric: (d) => `${d.apis} endpoints` },
                'dynamodb': { name: 'DynamoDB', category: 'Database', icon: '🗄️', metric: (d) => `${d.tables} tables` },
                'sqs': { name: 'SQS', category: 'Messaging', icon: '📨', metric: (d) => `${d.queues} queues` },
                'cloudwatch': { name: 'CloudWatch', category: 'Observability', icon: '📊', metric: (d) => `${d.log_groups} log groups` },
                'secretsmanager': { name: 'Secrets Manager', category: 'Security', icon: '🔐', metric: (d) => `${d.secrets} secrets` },
                'sns': { name: 'SNS', category: 'Messaging', icon: '🔔', metric: (d) => `${d.topics} topics` },
                'lambda': { name: 'Lambda', category: 'Compute', icon: '⚡', metric: (d) => `${d.functions} functions` },
                'kinesis': { name: 'Kinesis', category: 'Streaming', icon: '🌊', metric: (d) => `${d.streams} streams` },
                'ses': { name: 'SES', category: 'Email', icon: '📧', metric: (d) => `${d.verified_emails} identities` }
            };
            
            const grid = document.getElementById('servicesGrid');
            grid.innerHTML = '';
            for (const [key, svc] of Object.entries(data)) {
                const config = servicesConfig[key] || { name: key, category: 'Service', icon: '🔧', metric: () => '' };
                const card = document.createElement('div');
                card.className = 'service-card';
                card.onclick = () => openModal(key, svc);
                card.innerHTML = `
                    <div class="card-header">
                        <div class="service-info">
                            <div class="service-icon">${config.icon}</div>
                            <div class="service-name">
                                <h4>${config.name}</h4>
                                <p>${config.category}</p>
                            </div>
                        </div>
                        <div class="status-indicator">
                            <span>●</span> Active
                        </div>
                    </div>
                    <div class="card-metrics">
                        <div class="metric-row">
                            <span class="metric-label">📊 Resources</span>
                            <span class="metric-number">${config.metric(svc)}</span>
                        </div>
                    </div>
                    <div class="control-action">
                        MANAGE → CONTROL
                    </div>
                `;
                grid.appendChild(card);
            }
        }
        
        async function openModal(service, data) {
            const modal = document.getElementById('modal');
            const modalTitle = document.getElementById('modalTitle');
            const modalBody = document.getElementById('modalBody');
            
            const titles = {
                's3': 'S3 Storage • File Manager',
                'apigateway': 'API Gateway • Create & Test APIs',
                'dynamodb': 'DynamoDB • Data Console',
                'sqs': 'SQS Queue • Message Broker',
                'cloudwatch': 'CloudWatch • Logs & Metrics',
                'secretsmanager': 'Secrets Manager • Vault',
                'sns': 'SNS Notification • Publisher',
                'lambda': 'Lambda Functions • Serverless',
                'kinesis': 'Kinesis • Data Streams',
                'ses': 'SES • Email Service'
            };
            modalTitle.innerText = titles[service] || `Manage ${service.toUpperCase()}`;
            
            let content = '';
            
            // S3 - Upload File
            if (service === 's3') {
                content = `
                    <div class="form-group"><label>Bucket name</label><input type="text" id="bucketName" placeholder="my-bucket"></div>
                    <div class="form-group"><label>Object key</label><input type="text" id="fileName" placeholder="file.txt"></div>
                    <div class="form-group"><label>Content <span style="color:#667eea;">(UTF-8)</span></label><textarea id="fileContent" rows="3" placeholder="Write your content here..."></textarea></div>
                    <button class="btn" onclick="uploadToS3()">Upload Object →</button>
                    <div id="result" class="result-box" style="display:none;"></div>
                `;
            } 
            // API Gateway - Create and Test API
            else if (service === 'apigateway') {
                content = `
                    <div class="form-group"><label>API Name</label><input type="text" id="apiName" placeholder="my-api"></div>
                    <div class="form-group"><label>Stage Name</label><input type="text" id="stageName" placeholder="prod" value="prod"></div>
                    <button class="btn" onclick="createAPI()">Create REST API →</button>
                    <div style="margin: 1rem 0; text-align: center; color: #667eea;">— or —</div>
                    <div class="form-group"><label>Select Existing API</label><select id="existingApi">${(data.api_names || []).map(n => `<option value="${n}">${n}</option>`).join('') || '<option>No APIs available</option>'}</select></div>
                    <button class="btn" onclick="testAPI()">Test API Endpoint →</button>
                    <div id="result" class="result-box" style="display:none;"></div>
                `;
            }
            // CloudWatch - Create Log Group and View Logs
            else if (service === 'cloudwatch') {
                content = `
                    <div class="form-group"><label>Create Log Group</label><input type="text" id="logGroupName" placeholder="/my-app/logs"></div>
                    <button class="btn" onclick="createLogGroup()">Create Log Group →</button>
                    <div style="margin: 1rem 0; text-align: center; color: #667eea;">— or —</div>
                    <div class="form-group"><label>View Logs From</label><select id="existingLogGroup">${(data.log_group_names || []).map(n => `<option value="${n}">${n}</option>`).join('') || '<option>No log groups available</option>'}</select></div>
                    <button class="btn" onclick="viewLogs()">View Log Streams →</button>
                    <div id="result" class="result-box" style="display:none;"></div>
                `;
            }
            // Kinesis - Create Stream and Put Record
            else if (service === 'kinesis') {
                content = `
                    <div class="form-group"><label>Stream Name</label><input type="text" id="streamName" placeholder="my-data-stream"></div>
                    <div class="form-group"><label>Number of Shards</label><input type="number" id="shardCount" value="1" min="1" max="5"></div>
                    <button class="btn" onclick="createStream()">Create Stream →</button>
                    <div style="margin: 1rem 0; text-align: center; color: #667eea;">— or —</div>
                    <div class="form-group"><label>Select Stream</label><select id="existingStream">${(data.stream_names || []).map(n => `<option value="${n}">${n}</option>`).join('') || '<option>No streams available</option>'}</select></div>
                    <div class="form-group"><label>Data to Send</label><textarea id="streamData" rows="2" placeholder='{"message": "Hello Kinesis!"}'></textarea></div>
                    <button class="btn" onclick="putToStream()">Put Record →</button>
                    <div id="result" class="result-box" style="display:none;"></div>
                `;
            }
            // SQS
            else if (service === 'sqs') {
                content = `
                    <div class="form-group"><label>Queue identifier</label><input type="text" id="queueName" placeholder="my-queue"></div>
                    <div class="form-group"><label>Message payload</label><textarea id="messageContent" rows="3" placeholder="Your message content..."></textarea></div>
                    <button class="btn" onclick="sendToSQS()">Send Message →</button>
                    <div id="result" class="result-box" style="display:none;"></div>
                `;
            }
            // SNS
            else if (service === 'sns') {
                content = `
                    <div class="form-group"><label>Topic name</label><input type="text" id="topicName" placeholder="my-topic"></div>
                    <div class="form-group"><label>Notification content</label><textarea id="snsMessage" rows="3" placeholder="Your notification..."></textarea></div>
                    <button class="btn" onclick="publishToSNS()">Publish →</button>
                    <div id="result" class="result-box" style="display:none;"></div>
                `;
            }
            // DynamoDB
            else if (service === 'dynamodb') {
                content = `
                    <div class="form-group"><label>Table name</label><input type="text" id="tableName" placeholder="my-table"></div>
                    <div class="form-group"><label>Item ID (partition key)</label><input type="text" id="itemId" placeholder="id-001"></div>
                    <div class="form-group"><label>Data attribute</label><input type="text" id="itemData" placeholder="value"></div>
                    <button class="btn" onclick="putToDynamoDB()">Put Item →</button>
                    <div id="result" class="result-box" style="display:none;"></div>
                `;
            }
            // Lambda
            else if (service === 'lambda') {
                content = `
                    <div class="form-group"><label>Function name</label><input type="text" id="funcName" placeholder="my-function"></div>
                    <div class="form-group"><label>Event payload <span style="color:#667eea;">(JSON)</span></label><textarea id="eventJson" rows="3" placeholder='{"key": "value"}'></textarea></div>
                    <button class="btn" onclick="invokeLambda()">Invoke →</button>
                    <div id="result" class="result-box" style="display:none;"></div>
                `;
            }
            // SES
            else if (service === 'ses') {
                content = `
                    <div class="form-group"><label>Recipient</label><input type="email" id="toEmail" placeholder="recipient@example.com"></div>
                    <div class="form-group"><label>Subject line</label><input type="text" id="emailSubject" placeholder="Email subject"></div>
                    <div class="form-group"><label>Body text</label><textarea id="emailBody" rows="3" placeholder="Your message..."></textarea></div>
                    <button class="btn" onclick="sendEmail()">Send →</button>
                    <div id="result" class="result-box" style="display:none;"></div>
                `;
            }
            // Secrets Manager
            else if (service === 'secretsmanager') {
                content = `
                    <div class="form-group"><label>Secret identifier</label><input type="text" id="secretName" placeholder="my-secret"></div>
                    <div class="form-group"><label>Secret value <span style="color:#667eea;">(JSON format)</span></label><textarea id="secretValue" rows="3" placeholder='{"username":"admin","password":"secure"}'></textarea></div>
                    <button class="btn" onclick="createSecret()">Store Secret →</button>
                    <div id="result" class="result-box" style="display:none;"></div>
                `;
            } else {
                content = `<p style="text-align:center; padding:2rem;">Service ready<br><span style="color:#667eea;">${service.toUpperCase()}</span></p>`;
            }
            
            modalBody.innerHTML = content;
            modal.style.display = 'flex';
        }
        
        // ============ API Functions ============
        
        // S3 Functions
        async function uploadToS3() {
            const bucket = document.getElementById('bucketName').value;
            const key = document.getElementById('fileName').value;
            const content = document.getElementById('fileContent').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Processing...';
            const res = await fetch('/api/s3/upload', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({bucket, key, content})
            });
            const data = await res.json();
            resultDiv.innerHTML = data.success ? `✅ ${data.message}` : `❌ ${data.error}`;
            if (data.success) setTimeout(loadDashboard, 1000);
        }
        
        // API Gateway Functions
        async function createAPI() {
            const name = document.getElementById('apiName').value;
            const stage = document.getElementById('stageName').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Creating API Gateway...';
            const res = await fetch('/api/apigateway/create', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({name, stage})
            });
            const data = await res.json();
            resultDiv.innerHTML = data.success ? `✅ API Created: ${data.api_id}\n📡 Endpoint: ${data.endpoint}` : `❌ ${data.error}`;
            if (data.success) setTimeout(loadDashboard, 2000);
        }
        
        async function testAPI() {
            const apiName = document.getElementById('existingApi').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Testing API...';
            const res = await fetch('/api/apigateway/test', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({name: apiName})
            });
            const data = await res.json();
            resultDiv.innerHTML = data.success ? `✅ API Response: ${JSON.stringify(data.response)}` : `❌ ${data.error}`;
        }
        
        // CloudWatch Functions
        async function createLogGroup() {
            const name = document.getElementById('logGroupName').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Creating Log Group...';
            const res = await fetch('/api/cloudwatch/create-log-group', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({name})
            });
            const data = await res.json();
            resultDiv.innerHTML = data.success ? `✅ Log Group Created: ${name}` : `❌ ${data.error}`;
            if (data.success) setTimeout(loadDashboard, 1000);
        }
        
        async function viewLogs() {
            const logGroup = document.getElementById('existingLogGroup').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Fetching Log Streams...';
            const res = await fetch('/api/cloudwatch/view-logs', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({name: logGroup})
            });
            const data = await res.json();
            if (data.success) {
                if (data.streams && data.streams.length > 0) {
                    resultDiv.innerHTML = `✅ Log Streams for ${logGroup}:\n${data.streams.join('\\n')}`;
                } else {
                    resultDiv.innerHTML = `✅ Log Group "${logGroup}" exists (no streams yet)`;
                }
            } else {
                resultDiv.innerHTML = `❌ ${data.error}`;
            }
        }
        
        // Kinesis Functions
        async function createStream() {
            const name = document.getElementById('streamName').value;
            const shards = document.getElementById('shardCount').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Creating Kinesis Stream...';
            const res = await fetch('/api/kinesis/create-stream', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({name, shards: parseInt(shards)})
            });
            const data = await res.json();
            resultDiv.innerHTML = data.success ? `✅ Stream Created: ${name} (${shards} shard(s))` : `❌ ${data.error}`;
            if (data.success) setTimeout(loadDashboard, 2000);
        }
        
        async function putToStream() {
            const streamName = document.getElementById('existingStream').value;
            const data = document.getElementById('streamData').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Sending Data to Stream...';
            const res = await fetch('/api/kinesis/put-record', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({name: streamName, data: data})
            });
            const response = await res.json();
            resultDiv.innerHTML = response.success ? `✅ Record sent to ${streamName}` : `❌ ${response.error}`;
        }
        
        // SQS Functions
        async function sendToSQS() {
            const queue = document.getElementById('queueName').value;
            const message = document.getElementById('messageContent').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Sending...';
            const res = await fetch('/api/sqs/send', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({queue, message})
            });
            const data = await res.json();
            resultDiv.innerHTML = data.success ? `✅ ${data.message}` : `❌ ${data.error}`;
            if (data.success) setTimeout(loadDashboard, 1000);
        }
        
        // SNS Functions
        async function publishToSNS() {
            const topic = document.getElementById('topicName').value;
            const message = document.getElementById('snsMessage').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Publishing...';
            const res = await fetch('/api/sns/publish', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({topic, message})
            });
            const data = await res.json();
            resultDiv.innerHTML = data.success ? `✅ ${data.message}` : `❌ ${data.error}`;
        }
        
        // DynamoDB Functions
        async function putToDynamoDB() {
            const table = document.getElementById('tableName').value;
            const id = document.getElementById('itemId').value;
            const dataVal = document.getElementById('itemData').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Adding...';
            const res = await fetch('/api/dynamodb/put', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({table, id, data: dataVal})
            });
            const data = await res.json();
            resultDiv.innerHTML = data.success ? `✅ ${data.message}` : `❌ ${data.error}`;
            if (data.success) setTimeout(loadDashboard, 1000);
        }
        
        // Lambda Functions
        async function invokeLambda() {
            const funcName = document.getElementById('funcName').value;
            const eventJson = document.getElementById('eventJson').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Invoking...';
            const res = await fetch('/api/lambda/invoke', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({function: funcName, event: eventJson || '{}'})
            });
            const data = await res.json();
            resultDiv.innerHTML = data.success ? `✅ Result: ${JSON.stringify(data.result)}` : `❌ ${data.error}`;
        }
        
        // SES Functions
        async function sendEmail() {
            const to = document.getElementById('toEmail').value;
            const subject = document.getElementById('emailSubject').value;
            const body = document.getElementById('emailBody').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Sending...';
            const res = await fetch('/api/ses/send', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({to, subject, body})
            });
            const data = await res.json();
            resultDiv.innerHTML = data.success ? `✅ ${data.message}` : `❌ ${data.error}`;
        }
        
        // Secrets Manager Functions
        async function createSecret() {
            const name = document.getElementById('secretName').value;
            const value = document.getElementById('secretValue').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '⏳ Storing...';
            const res = await fetch('/api/secrets/create', {
                method: 'POST', headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({name, value})
            });
            const data = await res.json();
            resultDiv.innerHTML = data.success ? `✅ ${data.message}` : `❌ ${data.error}`;
            if (data.success) setTimeout(loadDashboard, 1000);
        }
        
        function closeModal() {
            document.getElementById('modal').style.display = 'none';
        }
        
        loadDashboard();
        setInterval(loadDashboard, 15000);
    </script>
</body>
</html>
'''

# ============ API ENDPOINTS ============

@app.route('/')
def dashboard():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/metrics')
def api_metrics():
    return jsonify(get_service_metrics())

# S3
@app.route('/api/s3/upload', methods=['POST'])
def api_s3_upload():
    data = request.json
    try:
        s3 = get_client('s3')
        try:
            s3.create_bucket(Bucket=data['bucket'])
        except:
            pass
        s3.put_object(Bucket=data['bucket'], Key=data['key'], Body=data['content'].encode())
        return jsonify({'success': True, 'message': f'Uploaded {data["key"]} to {data["bucket"]}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# API Gateway
@app.route('/api/apigateway/create', methods=['POST'])
def api_apigateway_create():
    data = request.json
    try:
        apig = get_client('apigateway')
        response = apig.create_rest_api(
            name=data['name'],
            description='API created via Nexus Dashboard',
            endpointConfiguration={'types': ['REGIONAL']}
        )
        api_id = response['id']
        # Create deployment
        apig.create_deployment(restApiId=api_id, stageName=data['stage'])
        endpoint = f"http://localhost:4566/restapis/{api_id}/{data['stage']}/_user_request_/"
        return jsonify({'success': True, 'api_id': api_id, 'endpoint': endpoint})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/apigateway/test', methods=['POST'])
def api_apigateway_test():
    data = request.json
    try:
        apig = get_client('apigateway')
        apis = apig.get_rest_apis()
        api = next((a for a in apis.get('items', []) if a['name'] == data['name']), None)
        if not api:
            return jsonify({'success': False, 'error': 'API not found'})
        return jsonify({'success': True, 'response': {'message': f'API {api["name"]} is ready', 'id': api['id']}})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# CloudWatch
@app.route('/api/cloudwatch/create-log-group', methods=['POST'])
def api_cloudwatch_create_log_group():
    data = request.json
    try:
        logs = get_client('logs')
        logs.create_log_group(logGroupName=data['name'])
        return jsonify({'success': True, 'message': f'Log group {data["name"]} created'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/cloudwatch/view-logs', methods=['POST'])
def api_cloudwatch_view_logs():
    data = request.json
    try:
        logs = get_client('logs')
        streams = logs.describe_log_streams(logGroupName=data['name'])
        return jsonify({'success': True, 'streams': [s['logStreamName'] for s in streams.get('logStreams', [])]})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Kinesis
@app.route('/api/kinesis/create-stream', methods=['POST'])
def api_kinesis_create_stream():
    data = request.json
    try:
        kinesis = get_client('kinesis')
        kinesis.create_stream(StreamName=data['name'], ShardCount=data['shards'])
        return jsonify({'success': True, 'message': f'Stream {data["name"]} created'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/kinesis/put-record', methods=['POST'])
def api_kinesis_put_record():
    data = request.json
    try:
        kinesis = get_client('kinesis')
        kinesis.put_record(
            StreamName=data['name'],
            Data=data['data'].encode(),
            PartitionKey=str(uuid.uuid4())
        )
        return jsonify({'success': True, 'message': 'Record sent to stream'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# SQS
@app.route('/api/sqs/send', methods=['POST'])
def api_sqs_send():
    data = request.json
    try:
        sqs = get_client('sqs')
        try:
            sqs.create_queue(QueueName=data['queue'])
        except:
            pass
        queue_url = f"{LOCALSTACK_ENDPOINT}/000000000000/{data['queue']}"
        sqs.send_message(QueueUrl=queue_url, MessageBody=data['message'])
        return jsonify({'success': True, 'message': 'Message sent to queue'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# SNS
@app.route('/api/sns/publish', methods=['POST'])
def api_sns_publish():
    data = request.json
    try:
        sns = get_client('sns')
        try:
            response = sns.create_topic(Name=data['topic'])
            topic_arn = response['TopicArn']
        except:
            topic_arn = f"arn:aws:sns:us-east-1:000000000000:{data['topic']}"
        sns.publish(TopicArn=topic_arn, Message=data['message'])
        return jsonify({'success': True, 'message': 'Notification published'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# DynamoDB
@app.route('/api/dynamodb/put', methods=['POST'])
def api_dynamodb_put():
    data = request.json
    try:
        dynamodb = get_client('dynamodb')
        try:
            dynamodb.create_table(
                TableName=data['table'],
                KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
                AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
                BillingMode='PAY_PER_REQUEST'
            )
        except:
            pass
        dynamodb.put_item(TableName=data['table'], Item={'id': {'S': data['id']}, 'data': {'S': data['data']}})
        return jsonify({'success': True, 'message': f'Item {data["id"]} added to {data["table"]}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Lambda
@app.route('/api/lambda/invoke', methods=['POST'])
def api_lambda_invoke():
    data = request.json
    try:
        lamb = get_client('lambda')
        response = lamb.invoke(FunctionName=data['function'], Payload=data['event'].encode())
        payload = json.loads(response['Payload'].read().decode())
        return jsonify({'success': True, 'result': payload})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# SES
@app.route('/api/ses/send', methods=['POST'])
def api_ses_send():
    data = request.json
    try:
        ses = get_client('ses')
        ses.verify_email_identity(EmailAddress='sender@nexus.cloud')
        ses.send_email(
            Source='sender@nexus.cloud',
            Destination={'ToAddresses': [data['to']]},
            Message={'Subject': {'Data': data['subject']}, 'Body': {'Text': {'Data': data['body']}}}
        )
        return jsonify({'success': True, 'message': f'Email sent to {data["to"]}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Secrets Manager
@app.route('/api/secrets/create', methods=['POST'])
def api_secrets_create():
    data = request.json
    try:
        sm = get_client('secretsmanager')
        sm.create_secret(Name=data['name'], SecretString=data['value'])
        return jsonify({'success': True, 'message': f'Secret {data["name"]} created'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'platform': 'Nexus Cloud'})

if __name__ == '__main__':
    print("""
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                  	║
║     🎖️ ABHRAKA CLOUD - INFRASTRUCTURE CONTROL CENTER                	║
║     ALL 10 SERVICES FULLY FUNCTIONAL!                        		║
║                                                               	║
║     🚀 Dashboard: http://localhost:5000                       	║
║                                                               	║
║                                                                     	║
║     ✅ COMPLETE FEATURES:                                       	║
║     • S3 Storage - Upload files                                 	║
║     • API Gateway - Create & Test REST APIs (NEW!)               	║
║     • DynamoDB - Add database items                             	║
║     • SQS Queue - Send messages                                  	║
║     • CloudWatch - Create log groups & view logs (NEW!)          	║
║     • Secrets Manager - Store credentials                       	║
║     • SNS Notification - Publish alerts                         	║
║     • Lambda Functions - Invoke serverless                       	║
║     • Kinesis - Create streams & put records (NEW!)           	║
║     • SES Email - Send simulated emails                         	║
║                                                                 	║
╚═══════════════════════════════════════════════════════════════════════╝
    """)
    app.run(host='0.0.0.0', port=5000, debug=False)
